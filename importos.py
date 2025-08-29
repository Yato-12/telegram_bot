from keep_alive import keep_alive
keep_alive()

import os
import json
import random
from dotenv import load_dotenv   # <--- para cargar el .env
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, CallbackQueryHandler

# === Cargar variables del archivo .env ===
load_dotenv()
TOKEN = os.getenv("TELEGRAM_TOKEN")   # ahora se toma desde .env

# === Diccionario de categorías base ===
categories = {
    "Saludos": [...],
    "Viajes": [...],
    "Restaurante": [...],
    "Compras": [...],
    "Emergencia": [...],
    "Conversación": [...]
}

# === Nombre del archivo JSON ===
JSON_FILE = "frases_aleman.json"

# === Crear JSON si no existe ===
if not os.path.exists(JSON_FILE):
    phrases = []
    for _ in range(500):
        cat = random.choice(list(categories.keys()))
        base = random.choice(categories[cat])

        if "?" in base:
            variation = base.replace("?", " bitte?")
        elif base.endswith("!"):
            variation = base.replace("!", "!!")
        else:
            variation = base  # aquí se respeta la frase original

        entry = {"categoria": cat, "frase": variation}
        phrases.append(entry)

    with open(JSON_FILE, "w", encoding="utf-8") as f:
        json.dump(phrases, f, ensure_ascii=False, indent=2)

    print("Se generó frases_aleman.json automáticamente")
else:
    print("Se encontró frases_aleman.json")

# === Cargar frases ===
with open(JSON_FILE, "r", encoding="utf-8") as f:
    phrases = json.load(f)


# === /start ===
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(cat, callback_data=cat)] for cat in categories.keys()
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "Hallo! Soy tu bot de frases en alemán.\n\n"
        "➡ Usa /frase para obtener una frase aleatoria.\n"
        "➡ O elige una categoría:",
        reply_markup=reply_markup
    )


# === /frase (aleatoria global) ===
async def frase(update: Update, context: ContextTypes.DEFAULT_TYPE):
    entry = random.choice(phrases)
    await update.message.reply_text(f"[{entry['categoria']}] {entry['frase']}")


# === Handler de botones (categorías) ===
async def categoria_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    categoria = query.data
    frases_filtradas = [f for f in phrases if f["categoria"] == categoria]

    if frases_filtradas:
        entry = random.choice(frases_filtradas)
        await query.edit_message_text(f"[{categoria}] {entry['frase']}")
    else:
        await query.edit_message_text(f"No hay frases en la categoría {categoria}.")


# === Main ===
def main():
    if not TOKEN:
        raise ValueError("❌ No se encontró TELEGRAM_TOKEN en el archivo .env")
    
    app = Application.builder().token(TOKEN).build()

    # Handlers
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("frase", frase))
    app.add_handler(CallbackQueryHandler(categoria_handler))  # botones

    print("Bot corriendo...")
    app.run_polling()


if __name__ == "__main__":
    main()
