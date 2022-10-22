python run_ner.py \
  --model_name_or_path "allenai/scibert_scivocab_uncased" \
  --dataset_name ../our_data \
  --output_dir tmp \
  --do_train \
  --do_eval \
  --do_predict
