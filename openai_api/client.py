from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()

client = OpenAI(
  api_key=os.getenv('OPENAI_API_KEY')
)

def get_car_ai_bio(model, brand, year):
  prompt = f'''
  Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 200 caracteres. Falei coisas específicas desse modelo de carro.
'''
  response = client.chat.completions.create(
    model='gpt-3.5-turbo',
    messages=[
      {
        'role': 'user',
        'content': prompt
      }
    ],
    max_tokens=1000
  )
  return response.choices[0].message.content.strip()