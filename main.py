import os
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    ContextTypes,
    CommandHandler,
    MessageHandler,
    filters,
)

# گرفتن توکن از محیط
TOKEN = os.getenv("BOT_TOKEN")

# پاسخ به /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! ربات DateChat آماده است 😊")

# پاسخ پیش‌فرض به هر پیام متنی
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"پیامتو گرفتم: {user_message}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()

    # هندلرها
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # اجرای ربات
    print("ربات در حال اجراست...")
    app.run_polling()
