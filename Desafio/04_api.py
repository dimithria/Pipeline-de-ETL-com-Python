import openai
# sua chave api 
openai = "SUA-CHAVE-API"
openai.api_key = openai_api_key

def generate_ai_news(employee):
  completion = openai.ChatCompletion.create(
      model="gpt-4",
      massage=[
          {"role": "system", "content": "Você é o CEO de uma empresa de alta tecnologia."},

          {"role": "user", "content": f"Crie uma mensagem de boas-vindas para {employee['nome']} sobre sua entrada em uma empresa de alta tecnologia (máximo de 100 caracteres)"}
      ]
  )
  return completion.choices[0].message.content.strip('\"')

for employee in listaFuncionarios:
  news = generate_ai_news(employee)
  print(news)

## LOAD
from requests import request
def update_user(employee):
  response = request.put(f"{employee_id}/listaFuncionarios/{employee['ID']}", json=employee)
  return True if response.status_code == 200 else False

for employee in listaFuncionarios:
  sucess = update_user(employee)
  print(f"User {employee['Nome']} update? {sucess}!")