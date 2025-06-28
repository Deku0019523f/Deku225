from telegram import Update, InputMediaPhoto
from telegram.ext import CallbackContext

IMG = {
    "1": "https://raw.githubusercontent.com/Deku0019523f/Deku225/main/images/1.png",
    "2": "https://raw.githubusercontent.com/Deku0019523f/Deku225/main/images/2.png",
    "3": "https://raw.githubusercontent.com/Deku0019523f/Deku225/main/images/3.png",
    "4": "https://raw.githubusercontent.com/Deku0019523f/Deku225/main/images/4.png",
    "5": "https://raw.githubusercontent.com/Deku0019523f/Deku225/main/images/5.png",
    "6": "https://raw.githubusercontent.com/Deku0019523f/Deku225/main/images/6.png",
    "7": "https://raw.githubusercontent.com/Deku0019523f/Deku225/main/images/7.png",
    "8": "https://raw.githubusercontent.com/Deku0019523f/Deku225/main/images/8.png",
}

ADMIN = "@Deku225"

def repondre_produit(update: Update, context: CallbackContext):
    msg = update.message.text
    contenu = {
        "1️⃣ Acheter un VPS": {
            "img": IMG["1"],
            "txt": "🖥️ *VPS à petit prix :*\n- 1Gb RAM : 1500F\n- 4Gb RAM : 4000F\n- 8Gb RAM : 5500F\n\nCommande rapide : " + ADMIN
        },
        "2️⃣ Acheter un SCRIPT": {
            "img": IMG["2"],
            "txt": "📜 *Scripts VPN :*\n- SlowDNS : 4500F\n- UDP Tunnel : 3000F\n\nContacte l’admin pour les détails : " + ADMIN
        },
        "3️⃣ Compte AfricaSurf": {
            "img": IMG["3"],
            "txt": "🌍 *AfricaSurf Premium*\n- 1 mois : 2000F\n- 3 mois : 5000F\n\nCompatible Moov/MTN/Airtel. Achat via " + ADMIN
        },
        "4️⃣ Compte Crunchyroll": {
            "img": IMG["4"],
            "txt": "🎥 *Crunchyroll Premium*\n- 1 mois : 1500F\n\nLivraison rapide après achat.\nContact : " + ADMIN
        },
        "5️⃣ Compte Netflix": {
            "img": IMG["5"],
            "txt": "🎬 *Netflix Profil Premium*\n- 1 mois : 2400F\n\nDispo en stock limité. Contact : " + ADMIN
        },
        "6️⃣ Abonnement Télégram": {
            "img": IMG["6"],
            "txt": "📢 *Telegram Premium*\n- 1 mois : 3500F\n- 3 mois : 10000F\n- 1 an : 23500F\n\nCommande : " + ADMIN
        },
        "7️⃣ Fichier VPN Free": {
            "img": IMG["7"],
            "txt": "🔓 *Fichiers VPN Free (France)*\nTélécharge ici : [Lien Google Drive](https://drive.google.com/drive/folders/1g-KHwmcIsMDZD2NNkpW7nfEtQHesmYDu)\nBesoin d’aide ? " + ADMIN
        },
        "8️⃣ Revendeur AfricaSurf": {
            "img": IMG["8"],
            "txt": "💼 *Revendeur officiel AfricaSurf*\n- Prix : 2000F\n- Accès revendeur + support\n\nPlus d'infos ? Contacte : " + ADMIN
        }
    }

    produit = contenu.get(msg)
    if produit:
        update.message.reply_photo(
            photo=produit["img"],
            caption=produit["txt"],
            parse_mode="Markdown",
        )
    else:
        update.message.reply_text("❓ Choix inconnu. Tape /start pour voir le menu.")
