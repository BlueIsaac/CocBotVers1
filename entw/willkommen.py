import discord
from discord.ext import commands
import json


# Laden der bereits begrüßten Benutzerdaten aus einer JSON-Datei (falls vorhanden)
def loadWelcomedUsers():
    try:
        with open("welcomed_users.json", "r") as file:
            welcomed_users = json.load(file)
            return welcomed_users
    except FileNotFoundError:
        welcomed_users = []
        return welcomed_users

# Funktion zum Speichern der begrüßten Benutzerdaten in die JSON-Datei
def save_welcomed_users(welcomed_users):
    with open("welcomed_users.json", "w") as file:
        json.dump(welcomed_users, file)
