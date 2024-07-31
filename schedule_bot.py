# telegram token for schedule_bot
from typing import Final
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

TELEGRAM_TOKEN: Final = "7041545993:AAES0PnrOvkiQKVRD_09qH88dLBRsJ4rJQM"
BOT_USERNAME: Final = "@RecallAllBot"


# Command Handlers
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Привет! Тут ты можешь настроить напоминалку')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('Чтобы настроить напоминалку, напиши дату и время')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text('This is the custom command')

# Message Handler for User Responses
async def handle_response_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text.lower()
    response = await handle_response(user_message)
    await update.message.reply_text(response)

# Responses
async def handle_response(text: str) -> str:
    if 'четверг' in text:
        return 'На какое время поставить напоминалку?'
    if '21:00' in text:
        return 'Сообщение придёт в 21:00 в четверг'
    return 'i dont understand'

async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f'Update {update} caused error {context.error}')

if __name__ == "__main__":
    print('starting bot...')
    app = Application.builder().token(TELEGRAM_TOKEN).build()

    # Commands
    app.add_handler(CommandHandler('start', start_command))
    app.add_handler(CommandHandler('help', help_command))
    app.add_handler(CommandHandler('custom', custom_command))

    # Message handler
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_response_message))

    # Errors
    app.add_error_handler(error)

    # Polls the bot
    print('polling...')
    app.run_polling(poll_interval=3)