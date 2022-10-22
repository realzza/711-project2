"""
Custom Huggingface-compatible NER dataset
"""

from datasets import load_metric
import datasets
import os

metric = load_metric("seqeval")
logger = datasets.logging.get_logger(__name__)


class OurDataConfig(datasets.BuilderConfig):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)


class OurData(datasets.GeneratorBasedBuilder):
    BUILDER_CONFIGS = [
        OurDataConfig(name="OurData", version=datasets.Version("1.0.0"), description="Our NLP NER dataset"),
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
        url = "https://github.com/realzza/711-project2/raw/main/our_data"
        data_files = {
            # FIXME: data splits
            "train": os.path.join(url, "tjy-raw.conll"),
            "dev": os.path.join(url, "tjy-raw.conll"),
            "test": os.path.join(url, "tjy-raw.conll"),
        }

        return [
            datasets.SplitGenerator(name=datasets.Split.TRAIN, gen_kwargs={"filepath": data_files["train"]}),
            datasets.SplitGenerator(name=datasets.Split.VALIDATION, gen_kwargs={"filepath": data_files["dev"]}),
            datasets.SplitGenerator(name=datasets.Split.TEST, gen_kwargs={"filepath": data_files["test"]}),
        ]

    def _generate_examples(self, filepath):
        logger.info("⏳ Generating examples from = %s", filepath)
        with open(filepath, encoding="utf-8") as f:
            guid = 0
            tokens = []
            ner_tags = []
            for line in f:
                if line.startswith("-DOCSTART-") or line == "" or line == "\n":
                    if tokens:
                        yield guid, {
                            "id": str(guid),
                            "tokens": tokens,
                            "ner_tags": ner_tags,
                        }
                        guid += 1
                        tokens = []
                        ner_tags = []
                else:
                    # conll2003 tokens are space separated
                    splits = line.split(" ")
                    tokens.append(splits[0])
                    ner_tags.append(splits[3].rstrip())
            # last example
            if tokens:
                yield guid, {
                    "id": str(guid),
                    "tokens": tokens,
                    "ner_tags": ner_tags,
                }
