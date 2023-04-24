import json
import os
import openai
from dotenv import load_dotenv
import discord
from discord.ext import commands
from src.app.core.promps.promps import ROLE_PROMPT

from src.app.core.utils.format_response import formatResponse

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
async def on_message(discordMessage: discord.Message):
    if discordMessage.author != bot.user:
        content = discordMessage.content
        channel = bot.get_channel(732283082601791528)
        prompt = [
            ROLE_PROMPT,
            {"role": "user", "content": content},
        ]
        response = openai.ChatCompletion.create(
            model=model_engine,
            messages=prompt,
            temperature=0.3,
            max_tokens=256,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0,
        )

        chatgptContent = response["choices"][0].message.content

        json_string = formatResponse(chatgptContent)
        isParsed = False
        try:
            parsed_message = json.loads(json_string)
            isParsed = True
        except:
            pass

        if isParsed and parsed_message.get("rep"):
            await discordMessage.delete()
            await channel.send(
                f'```Un message a été modéré par {bot.user.name}\n\nContenu du message : {content}\n\nAuteur : {discordMessage.author.name}\n\nMotif : {parsed_message.get("motif")}```'
            )
            print(f"Modéré, par la réponse : {chatgptContent}")
        else:
            print(f"parsed = {isParsed}, Non modéré, reponse du bot : {chatgptContent}")


bot.run(BOTKEY)
