import json

import discord
from discord.ext import commands
import logging
import textbot

# Definieren Sie die Intents, die Ihr Bot benötigt
intents = discord.Intents.all()
intents.typing = True
intents.presences = True
TOKEN = 'MTE0NDI5MTkwMzY4MTA4OTU3OA.Gyd5rI.zQXZ6eicMa3JQtDXrA1qKV1keB6ULmqPBhDmck'
# Initialisieren Sie den Bot mit den Intents
bot = commands.Bot(command_prefix='!', intents=intents)

# Konfigurieren Sie das Logging
logging.basicConfig(filename='bot_log.txt', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# Klasse zur Verwaltung der Willkommensnachrichten und der begrüßten Benutzer
class WelcomeManager:
    def __init__(self):
        self.welcomed_users = self.load_welcomed_users()

    def load_welcomed_users(self):
        try:
            with open("welcomed_users.json", "r") as file:
                data = json.load(file)
                if isinstance(data, list):
                    return data
                else:
                    return []  # Wenn die Datei leer oder ungültig ist, gebe eine leere Liste zurück
        except (FileNotFoundError, json.decoder.JSONDecodeError):
            return []  # Wenn die Datei nicht gefunden oder ungültig ist, gebe eine leere Liste zurück

    def save_welcomed_users(self):
        try:
            with open("welcomed_users.json", "w") as file:
                json.dump(self.welcomed_users, file)
        except Exception as e:
            print(f"Fehler beim Speichern der JSON-Datei: {str(e)}")

    def has_received_welcome_message(self, user_id):
        return user_id in self.welcomed_users

    def mark_as_welcomed(self, user_id):
        self.welcomed_users.append(user_id)
        self.save_welcomed_users()

    def to_dict(self):
        return {
            "welcomed_users": self.welcomed_users,
            # Weitere relevante Attribute hier hinzufügen
        }

    @classmethod
    def from_dict(cls, data):
        welcome_manager = cls()
        welcome_manager.welcomed_users = data["welcomed_users"]
        # Weitere relevante Attribute hier hinzufügen
        return welcome_manager

# Beispiel: Initialisieren des WelcomeManager
welcome_manager = WelcomeManager()

@bot.event
async def on_ready():
    print(f'Eingeloggt als {bot.user.name}')
    logging.info(f'Eingeloggt als {bot.user.name}')


@bot.event
async def on_message(message):
    # Bot-Nachrichten ignorieren, um eine Endlosschleife zu vermeiden
    if message.author == bot.user:
        return

    # Protokollieren Sie die Nachricht in der Log-Datei
    if isinstance(message.channel, discord.DMChannel):
        # Für private Nachrichten (DMs)
        logging.info(f'{message.author.name} ({message.author.id}) in einer privaten Nachricht - {message.content}')
    else:
        # Für Nachrichten in Server-Kanälen
        logging.info(f'{message.author.name} ({message.author.id}) in #{message.channel.name} - {message.content}')

    if isinstance(message.channel, discord.DMChannel) or isinstance(message.channel, discord.TextChannel):
        # Hier überprüfen wir, ob der Benutzer schon eine Willkommensnachricht erhalten hat
        if not welcome_manager.has_received_welcome_message(message.author.id):
            # Wenn der Benutzer noch keine Willkommensnachricht erhalten hat
            await message.channel.send(f'Willkommen, {message.author.mention}!')

            # Sende eine private Nachricht an den Benutzer
            await message.author.send(textbot.get_response("willkommen"))

            # Markiere den Benutzer als "Willkommensnachricht erhalten"
            welcome_manager.mark_as_welcomed(message.author.id)

    if isinstance(message.channel, discord.DMChannel):
        if message.content.startswith('!'):
            # Extrahieren Sie den Befehl aus der Nachricht
            command = message.content[1:].lower()

            if command == 'info':
                await message.channel.send(textbot.get_response(command))

            elif command == 'ping':
                await message.channel.send('Pong!')

            elif command == 'regeln':
                await message.channel.send(textbot.get_response(command))
            elif command == 'hilfe':
                await message.channel.send(textbot.get_response(command))
            else:
                await message.channel.send('Befehl nicht bekannt, probiere !hilfe für eine Liste der Befehle')

    # Liste der erlaubten Kanal-IDs, in denen der Bot antworten soll
    erlaubteKanaele = [1141843775187075195, 1141850337452494931, 1144530857860812830, 1144753372205953125, 1145763805184401540]
    # Überprüfen, ob die Nachricht aus einem erlaubten Kanal stammt
    if message.channel.id in erlaubteKanaele:
        if message.content.startswith('!'):
            # Extrahieren Sie den Befehl aus der Nachricht
            command = message.content[1:].lower()

            # Führen Sie Befehle basierend auf dem erhaltenen Befehl aus
            if command == 'hallo':
                await message.channel.send(f'Hallo, {message.author.mention}!')

            elif command == 'ping':
                await message.channel.send('Pong!')

            elif command == 'info':
                await message.channel.send(textbot.get_response(command))
            elif command == 'regeln':
                await message.channel.send(textbot.get_response(command))
            elif command == 'hilfe':
                await message.channel.send(textbot.get_response(command))
            else:
                await message.channel.send('Befehl nicht bekannt, probiere !hilfe für eine Liste der Befehle')


bot.run(TOKEN)
