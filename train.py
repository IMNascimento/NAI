from datasets import Dataset
from transformers import GPT2Tokenizer, GPT2LMHeadModel, Trainer, TrainingArguments
from config.config import Config
from utils import data_loader, training_utils

# Carregar os dados de treinamento
data = data_loader.load_data(Config.TRAIN_DATA_PATH)
dataset = Dataset.from_dict(data)

# Nome do modelo pré-treinado
model_name = Config.MODEL_NAME

# Carregar o tokenizer e o modelo
tokenizer = GPT2Tokenizer.from_pretrained(model_name)
model = GPT2LMHeadModel.from_pretrained(model_name)

# Tokenizar o conjunto de dados
tokenized_datasets = dataset.map(training_utils.tokenize_function(tokenizer), batched=True)

# Configurar argumentos de treinamento
training_args = TrainingArguments(
    output_dir=Config.RESULT_DIR,
    num_train_epochs=3,
    per_device_train_batch_size=2,
    per_device_eval_batch_size=2,
    warmup_steps=10,
    weight_decay=0.01,
    logging_dir=Config.LOG_DIR,
    logging_steps=10,
)

# Criar um objeto Trainer
trainer = Trainer(
    model=model,
    args=training_args,
    train_dataset=tokenized_datasets,
)

# Treinar o modelo
trainer.train()

# Salvar o modelo treinado
model.save_pretrained(Config.MODEL_PATH)
tokenizer.save_pretrained(Config.MODEL_PATH)