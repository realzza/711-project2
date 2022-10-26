# 711-project2

## Download papers

```
cd papers/
wget -i your_portion.txt -P your_papers/
```

## Setup Environment

```
bash setup.sh
```

## Prepare Input

```
usage: prepare_text.py [-h] --paper-dir PAPER_DIR [--output OUTPUT]

parse paper pdfs

optional arguments:
  -h, --help            show this help message and exit
  --paper-dir PAPER_DIR, -d PAPER_DIR
  --output OUTPUT, -o OUTPUT
```

Save your paper pdfs under a directory `papers/`, and save output json file in `prepared.json`

```
python prepare_text.py -d papers -o prepared.json
```

## Annotate Data Using Label Studio

See https://github.com/neubig/nlp-from-scratch-assignment-2022/blob/main/annotation_interface.md

**For finetuning, use the file exported by Label Studio directly (containing 4 columns)**

Otherwise, use `clean_conll.py` to remove the middle two columns.

## Finetune SciBERT on Annotated Data

```bash
# in ner/
python finetune.sh
```

## Run prediction on SciNER

```bash
# in ner/
python test_sciner.sh
```

## Submit to Explainaboard

```bash
# in ner/
pred_file=test_sciner/predictions.conll
submit_file=submission/submission.conll

# Convert sentence submission to paragraphs:
python ../sentence2paragraph.py -i $pred_file -d ../sciner/anlp-sciner-test-empty.conll -o $submit_file || exit 1

python -m explainaboard_client.cli.evaluate_system \
  --username $EB_USERNAME \
  --api-key $EB_API_KEY \
  --task named-entity-recognition \
  --system-name anlp_andrewid_scibert \
  --dataset cmu_anlp \
  --sub-dataset sciner \
  --split test \
  --system-output-file "$submit_file" \
  --system-output-file-type conll \
  --shared-users neubig@gmail.com \
  --source-language en
```
