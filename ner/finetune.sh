python run_ner.py \
  --model_name_or_path "allenai/scibert_scivocab_uncased" \
  --dataset_name ../our_data \
  --output_dir tmp \
  --num_train_epochs 5 \
  --per_device_train_batch_size 32 \
  --learning_rate 2e-5 \
  --do_train \
  --do_eval \
  --do_predict
