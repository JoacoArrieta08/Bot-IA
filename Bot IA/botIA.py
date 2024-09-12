import discord
from discord.ext import commands 
from model import get_class

intents = discord.Intents.default() # permisos que tiene el bot por default
intents.message_content = True 

bot = commands.Bot(command_prefix = "!", intents=intents)

@bot.event
async def on_ready():
    print(f"Se inicio el bot {bot.user}")

@bot.command()
async def check(ctx): # el ctx es para mandar y recibir los msj
    if ctx.message.attachments: #devuelve una lista de archivos adjuntos en el msj recibido por el bot
        for attachment in ctx.message.attachments:
            file_name = attachment.filename
            file_path = f"./{file_name}"
            await attachment.save(file_path)
            result = get_class(model_path="./keras_model.h5", labels_path="./labels.txt", image_path=file_path)
            await ctx.send(result)
    else: 
        await ctx.send(f"Olvido subir una imagen")


bot.run("MTI3OTg5ODE1NTM3MDAyNTA2Mg.GHvrQe.gD0LCOJr89_ZdX-U5Hkc4jHmlRDzJew613pt5M")