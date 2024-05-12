'''  Bot amigavel
Autor: vítor F M
Data: 11/05/2024
Descrição: um bot de discord conectado com o gemini IA para agir como seu amigo, sendo um apoio para os momento que está sosinho.
'''

#Bibliotecas:
import discord
from discord.ext import commands
import google.generativeai as genai

#APIs:
API_Gemini = "API_do_Gemini"
API_Discord = "API_do_discord"

#configurações do modelo:
genai.configure(api_key=API_Gemini)
Configuracao = { 
    "candidate_count": 1,
    "temperature": 0.5, 
}

Seguraca = {
    "HARASSMENT": "BLOCK_NONE",
    "HATE": "BLOCK_NONE",
    "SEXUAL": "BLOCK_NONE",
    "DANGEROUS": "BLOCK_NONE",
}

modelo = genai.GenerativeModel(model_name='gemini-1.0-pro',generation_config=Configuracao,safety_settings=Seguraca) #inicia o modelo
intents = discord.Intents.all()


#Personalidade do bot:
chat = modelo.start_chat(history=[]) 
chat.send_message("A partir de agora me responda como se fosse meu amigo, sempre de forma casual e informal")

#Configuração do bot no discord
bot = commands.Bot(command_prefix='!', intents=intents)

#Bot ficou ON:
@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

#Comandos:
@bot.command()
async def e(ctx, *, message: str):
  resposta = chat.send_message(message)
  await ctx.send(resposta.text)

#incio da aplicação
bot.run(API_Discord)
