import os
import openai
from dotenv import load_dotenv
from src.app.core.promps.promps import ROLE_PROMPT
from src.app.core.twitch.avertissements import Compteur
from twitchio import Message
from twitchio.ext import commands
import json

from src.app.core.utils.format_response import formatResponse

load_dotenv()
TWITCH_TOKEN = os.environ.get("TWITCH_TOKEN")

bot_name = "ModeratorBot"  # Remplacez par le nom d'utilisateur de votre bot
oauth_token = TWITCH_TOKEN  # Remplacez par votre jeton OAuth
channel_name = "latavernedesvieux"
model_engine = "gpt-3.5-turbo"
openai.organization = "org-1448AVUWN87lsQLHBpotEVQD"
openai.api_key = os.environ.get("OPENAI_API_KEY")


class TwitchBot(commands.Bot):
    def __init__(self, compteur: Compteur):
        self.compteur = compteur
        super().__init__(
            token=oauth_token,
            prefix="!",
            initial_channels=[channel_name],
        )

    async def event_ready(self):
        print(f"{bot_name} is connected and ready to receive messages!")

    async def event_message(self, message: Message):
        if not message.echo:
            prompt = [ROLE_PROMPT, {"role": "user", "content": message.content}]

            response = openai.ChatCompletion.create(model=model_engine, messages=prompt)

            chaptGptResponse: str = response["choices"][0].message.content

            json_string = formatResponse(chaptGptResponse)

            isParsed = False
            try:
                parsed_message = json.loads(json_string)
                isParsed = True
            except:
                pass

            if isParsed and parsed_message.get("rep"):
                self.compteur.add(message.author.name)
                await message.channel.send(
                    f'[AVERTISSEMENT n°{self.compteur.avertissementList[message.author.name]} pour {message.author.mention}] : {parsed_message.get("motif")}'
                )
            else:
                print(f"non modéré, réponse du bot {chaptGptResponse}")


if __name__ == "__main__":
    bot = TwitchBot(Compteur())
    bot.run()
