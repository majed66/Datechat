import logging
import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
# فعال کردن لاگ‌ها برای دیباگ
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
# دستور شروع
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("سلام! من ربات DateChat هستم.")
if __name__ == '__main__':
    token = os.getenv("BOT_TOKEN")
    if not token:
        print("❌ توکن تعریف نشده. لطفاً BOT_TOKEN را به عنوان env variable تنظیم کنید.")
        exit(1)
 app = ApplicationBuilder().token(token).build()
  app.add_handler(CommandHandler("start", start))
 print("✅ ربات DateChat در حال اجراست...")
    app.run_polling()
