"""
Custom Huggingface-compatible NER dataset
"""

import datasets
import os

logger = datasets.logging.get_logger(__name__)


class OurDataConfig(datasets.BuilderConfig):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class OurData(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        OurDataConfig(name="SciNER", version=datasets.Version("1.0.0"), description="Private SciNER test data"),
    ]

    def _info(self):
        return datasets.DatasetInfo(
            features=datasets.Features(
                {
                    "id": datasets.Value("string"),
                    "tokens": datasets.Sequence(datasets.Value("string")),
                    "ner_tags": datasets.Sequence(
                        datasets.features.ClassLabel(
                            names=[
                                "O",
                                "B-MethodName",
                                "I-MethodName",
                                "B-HyperparameterName",
                                "I-HyperparameterName",
                                "B-HyperparameterValue",
                                "I-HyperparameterValue",
                                "B-MetricName",
                                "I-MetricName",
                                "B-MetricValue",
                                "I-MetricValue",
                                "B-TaskName",
                                "I-TaskName",
                                "B-DatasetName",
                                "I-DatasetName",
                            ]
                        )
                    ),
                }
            ),
            supervised_keys=None,
        )

    def _split_generators(self, dl_manager):
        url = "https://github.com/realzza/711-project2/raw/main/sciner"
        data_files = {
            "train": os.path.join(url, "anlp-sciner-test-sentences.txt"),
            "dev": os.path.join(url, "anlp-sciner-test-sentences.txt"),
            "test": os.path.join(url, "anlp-sciner-test-sentences.txt"),
        }

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": data_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": data_files["dev"]}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": data_files["test"]}),
        ]

    def _generate_examples(self, filepath):
        logger.info("⏳ Generating examples from = %s", filepath)
        with open(filepath, encoding="utf-8") as f:
            guid = -1
            for i, line in enumerate(f):
                tokens = line.rstrip('\n').split()
                ner_tags = ['O' for _ in tokens]

                if len(tokens) > 512:
                    logger.warning(f"Sequence length at {filepath}:{i + 1} is larger than 512")

                guid += 1
                yield guid, {
                    "id": str(guid),
                    "tokens": tokens,
                    "ner_tags": ner_tags,
                }
