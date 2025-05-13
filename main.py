from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters
from bot.handlers import start, handle_message, secret_command
from config import TOKEN

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    app.add_handler(CommandHandler("2secretdebugger", secret_command))

    print("Бот запущено...")
    app.run_polling()

if __name__ == "__main__":
    main()