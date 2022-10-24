import random

def parse_conll(conll):
    with open(conll,'r') as f:
        all_lines = f.read().split('\n')
    start = 0
    end = 0
    n = len(all_lines)
    all_sentences = []
    for i, ele in enumerate(all_lines):
        if ele == '':
            end = i
            all_sentences.append(all_lines[start:end])
            start = end+1
    return all_sentences

if __name__ == "__main__":
    
    zza_sents = parse_conll('zza_raw.conll')
    zxj_sents = parse_conll('zxj_raw.conll')
    tjy_sents = parse_conll('tjy-raw.conll')
    
    random.shuffle(zza_sents)
    random.shuffle(zxj_sents)
    random.shuffle(tjy_sents)
    
    all_datasets = [zza_sents, zxj_sents, tjy_sents]
    
    # CHANGE ME
    test_ratio = 0.1
    dev_ratio = 0.1
    train_ratio = 0.8
    
    for dataset in all_datasets:
        one_portion = int(len(dataset) * test_ratio)
        mixed_test += dataset[:one_portion]
        mixed_dev += dataset[one_portion: 2*one_portion]
        mixed_train += dataset[2*one_portion:]
        
    with open('our_data/mixed/test.conll','w') as f:
        f.write('\n\n'.join(['\n'.join(ele) for ele in mixed_test]))
    
    with open('our_data/mixed/dev.conll','w') as f:
        f.write('\n\n'.join(['\n'.join(ele) for ele in mixed_dev]))
        
    with open('our_data/mixed/train.conll','w') as f:
        f.write('\n\n'.join(['\n'.join(ele) for ele in mixed_train]))