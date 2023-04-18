import os
import openai
from dotenv import load_dotenv
import discord
from discord.ext import commands

load_dotenv()
BOTKEY = os.environ.get("BOT_KEY")
openai.organization = "org-1448AVUWN87lsQLHBpotEVQD"
openai.api_key = os.environ.get("OPENAI_API_KEY")

intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)
model_engine = "gpt-3.5-turbo"


@bot.event
async def on_ready():
    print("Bot command ready")


@bot.event
async def on_message(ctx: discord.Message):
    if ctx.author != bot.user:
        content = ctx.content
        channel = bot.get_channel(1029289071840874497)
        message = [
            {
                "role": "system",
                "content": "Tu es un modérateur dans un chat de discussion, quand tu recois un message, indique par un boolean c'est a dire uniquement True si la phrase est insultante et doit être modérée, False sinon.",
            },
            {"role": "user", "content": content},
        ]
        response = openai.ChatCompletion.create(model=model_engine, messages=message)

        if "True" in response["choices"][0].message.content:
            await ctx.delete()
            await channel.send(f"`Un message a été modéré par {bot.user.name}`")


bot.run(BOTKEY)
