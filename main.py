from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application,
    CommandHandler,
    CallbackQueryHandler,
    MessageHandler,
    filters,
    ContextTypes
)

# Your bot token (will be revoked later)
BOT_TOKEN = "7927507913:AAHRmjqDOLs8VL22JIkwXNLKn-z3K3KpXls"
# REPLACE THESE WITH YOUR ACTUAL USERNAMES
CHANNEL_USERNAME = "YOUR_CHANNEL_USERNAME"  # Without '@'
GROUP_USERNAME = "YOUR_GROUP_USERNAME"
TWITTER_USERNAME = "YOUR_TWITTER_USERNAME"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("Join Channel", url=f"https://t.me/{CHANNEL_USERNAME}")],
        [InlineKeyboardButton("Join Group", url=f"https://t.me/{GROUP_USERNAME}")],
        [InlineKeyboardButton("Follow Twitter", url=f"https://twitter.com/{TWITTER_USERNAME}")],
        [InlineKeyboardButton("I've Joined ✅", callback_data="joined")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "🎉 Welcome to Airdrop Bot! 🎉\n\n"
        "To qualify:\n"
        "1. Join our channel\n"
        "2. Join our group\n"
        "3. Follow our Twitter\n"
        "4. Submit your Solana wallet\n\n"
        "Click below to join then press 'I've Joined'",
        reply_markup=reply_markup
    )

async def handle_join(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text("👍 Great! Now send your Solana wallet address:")

async def handle_wallet(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # No actual verification needed as per requirements
    await update.message.reply_text(
        "🎉 Congratulations! 🎉\n\n"
        "You've successfully joined our airdrop!\n"
        "No further verification needed for this test."
    )

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_join, pattern="^joined$"))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_wallet))
    
    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
