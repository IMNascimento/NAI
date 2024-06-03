class Config:
    MODEL_NAME = "pierreguillou/gpt2-small-portuguese"
    MODEL_PATH = "./models/gpt2_small_portuguese"
    TRAIN_DATA_PATH = "./data/train_data.json"
    LOG_DIR = "./logs"
    RESULT_DIR = "./results"
    WHATSAPP_SID = 'your_twilio_sid'
    WHATSAPP_AUTH_TOKEN = 'your_twilio_auth_token'
    WHATSAPP_FROM = 'whatsapp:+14155238886'