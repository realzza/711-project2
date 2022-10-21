import os
import json
import spacy
import argparse
from tqdm import tqdm
from PyPDF2 import PdfReader

def parse_args():
    desc="parse paper pdfs"
    parser = argparse.ArgumentParser(description=desc)
    parser.add_argument('--paper-dir', '-d', type=str, required=True)
    parser.add_argument('--output', '-o', type=str, default="prepared_text.json")
    return parser.parse_args()

if __name__ == '__main__':

    args = parse_args()
    assert args.output.endswith('.json'), "output file is a [json] file, please fix file type"
    pdf_dir = args.paper_dir
    all_pdfs = [os.path.join(pdf_dir, paper) for paper in os.listdir(pdf_dir) if paper.endswith('.pdf')]
    all_sentence = []
    nlp = spacy.load("en_core_web_sm")
    for pdf in all_pdfs:
        pdf_name = '-'.join(pdf.split('/')[-1].split('.')[:-1])
        pdf_reader = PdfReader(pdf)
        n_pages = len(pdf_reader.pages)
        pdf_pages = pdf_reader.pages
        page_indicator = 1
        for i in tqdm(range(n_pages), desc="[%s]"%(pdf_name)):
            curr_page = pdf_pages[i]
            curr_text = curr_page.extract_text()
            tokenized_page = [nlp(line) for line in ' '.join(curr_text.encode("ascii", "ignore").decode().replace('\x03','').split('\n')).split('. ')]
            pdf_page_sentence = [{'text':(' '.join([w.text for w in line])).replace(' - ','[SSUUBB]').replace('- ','').replace('[SSUUBB]',' - ').replace(' %','%').replace(' ne - ', ' fine - ')+' . ','paperid':pdf_name} for line in tokenized_page]
            all_sentence += pdf_page_sentence
            page_indicator += 1
    
    with open(args.output,'w') as f:
        json.dump(all_sentence, f)