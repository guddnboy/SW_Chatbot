# chatbot/chatbot_logic.py

from django.http import JsonResponse
import pickle
from ChabotEngine.predict import *
from ChabotEngine.train import *
from ChabotEngine.transforemer import *
from tensorflow import keras

model_path = r'C:\Users\AISELab\SW_Chatbot\ChabotEngine\saved_transformer_model'
token_path = r'C:\Users\AISELab\SW_Chatbot\ChabotEngine\토큰_및_토크나이저.pkl'

# 필요한 데이터 및 모델 로드
with open(token_path, 'rb') as file:
    loaded_data = pickle.load(file)

start_token = loaded_data['start_token']
end_token = loaded_data['end_token']
tokenizer = loaded_data['tokenizer']

custom_objects = {
    'PositionalEncoding': PositionalEncoding,
    'MultiHeadAttention': MYMultiHeadAttention,
    'CustomSchedule': CustomSchedule,
    'loss_function': loss_function
}

# 실제 모델 가져오기로 대체할 때 해당 모델의 import를 해야 합니다.
model = keras.models.load_model(model_path, custom_objects=custom_objects)

def get_chatbot_response(user_input):
    response = sentence_generation(user_input, start_token, end_token, tokenizer, model)
    return response