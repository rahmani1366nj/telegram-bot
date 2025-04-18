from telegram.ext import Updater, CommandHandler

# 👇 توکن رباتت رو همینجا بذار
TELEGRAM_TOKEN = '7053077694:AAGopO5vn3_yjfTuyHz7DkFpC6sd_GhfJ8M'

# ساختن آبجکت updater و dispatcher
updater = Updater(token=TELEGRAM_TOKEN, use_context=True)
dispatcher = updater.dispatcher

# دستور /start
def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="سلام! ربات شما با موفقیت راه‌اندازی شد 🚀")

# اضافه کردن هندلر برای دستور start
start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

# اجرای ربات
updater.start_polling()
updater.idle()
