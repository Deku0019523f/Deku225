from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
import os
from products import repondre_produit  # fichier séparé

TOKEN = os.getenv("BOT_TOKEN")  # Ton token est à mettre dans Railway (en variable d’environnement)
ADMIN_CONTACT = "@Deku225"

keyboard = [
    ["1️⃣ Acheter un VPS", "2️⃣ Acheter un SCRIPT"],
    ["3️⃣ Compte AfricaSurf", "4️⃣ Compte Crunchyroll"],
    ["5️⃣ Compte Netflix", "6️⃣ Abonnement Télégram"],
    ["7️⃣ Fichier VPN Free", "8️⃣ Revendeur AfricaSurf"],
]
reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

def start(update: Update, context: CallbackContext):
    user = update.effective_user
    name = user.first_name or user.username or "utilisateur"
    msg = f"👋 Bonjour *{name}* !\nBienvenue sur le bot vendeur.\n\nBesoin d'aide ? Contacte l'admin ici : {ADMIN_CONTACT}"
    update.message.reply_text(msg, reply_markup=reply_markup, parse_mode="Markdown")

def handle_message(update: Update, context: CallbackContext):
    repondre_produit(update, context)

updater = Updater(TOKEN)
dp = updater.dispatcher

dp.add_handler(CommandHandler("start", start))
dp.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

updater.start_polling()
updater.idle()
