
import openai

openai.api_key = "SUA_CHAVE_API" #sua chave da API

model_engine = "text-davinci-003" #modelo utilizado
prompt = input() #pergunta a ser feita

completion = openai.Completion.create( # completion é um termo usado para OpenAI que define a comunicação com a API da linguagem
    engine= model_engine,
    prompt = prompt,
    max_tokens = 1024, #tamanho máximo da resposta
    n=1, #quantidade de respostas
    stop= None, #regras para parar
    temperature = 0.5, # parametro de aleatoriedade das respostas
)

response = completion.choices[0].text # matriz da qual pegamos o primeiro elemento
print(response)

