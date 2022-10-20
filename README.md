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