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
python ner/finetune.sh
```
