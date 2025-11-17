import os
import re
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Get token from environment variable
BOT_TOKEN = os.environ.get(8427841207:AAFXUnoD41wcsYIYitQNqwrXw3msYryGSoE)

def validate_shibtc_address(address: str) -> bool:
    """Validate SHIBTC wallet address"""
    address = address.strip()
    
    if re.match(r'^0x[a-fA-F0-9]{40}$', address):  # Ethereum/BSC
        return True
    if re.match(r'^[13][a-km-zA-HJ-NP-Z1-9]{25,34}$', address):  # Bitcoin
        return True
    if re.match(r'^T[a-zA-Z0-9]{33}$', address):  # TRON
        return True
    
    return False

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🔐 SHIBTC Validator Bot - Send me a wallet address to validate!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.strip()
    
    if validate_shibtc_address(text):
        response = f"✅ Valid SHIBTC address!\n\n`{text}`"
    else:
        response = "❌ Invalid address format! Supported: Ethereum(0x...), Bitcoin(1...), TRON(T...)"
    
    await update.message.reply_text(response, parse_mode='Markdown')

def main():
    if not BOT_TOKEN:
        print("❌ Error: BOT_TOKEN not set!")
        return
    
    application = Application.builder().token(BOT_TOKEN).build()
    application.add_handler(CommandHandler("start", start_command))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    
    print("🤖 SHIBTC Bot is running...")
    application.run_polling()

if __name__ == "__main__":
    main()
