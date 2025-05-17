from telegram import Update, MenuButtonWebApp, WebAppInfo
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Ваш токен
TOKEN = "8152835147:AAGadk_G-pk-UaPLwE0zgKlAi2nifmwd7BQ"
# URL вашего mini-app
WEB_APP_URL = "https://mipt.online/masters/data_science?utm_source=tgapp"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # 1) Установить кнопку рядом с полем ввода
    await context.bot.set_chat_menu_button(
        chat_id=update.effective_chat.id,
        menu_button=MenuButtonWebApp(
            text="Открыть приложение",
            web_app=WebAppInfo(url=WEB_APP_URL)
        )
    )
    # 2) Отправить пользователю инструкцию
    await update.message.reply_text(
        "Привет! Это приложение онлайн-магистратуры «Науки о данных»."
    )

if __name__ == "__main__":
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Поехали!")
    app.run_polling()