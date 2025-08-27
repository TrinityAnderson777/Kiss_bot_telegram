from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import re
import logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Приветственное сообщение при /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.chat.type == 'private':
        await update.message.reply_text(
            "✨ Привет! Я — ваш милый бот для обнимашек, поцелуев и любви! 💖\n\n"
            "Добавьте меня в чат, чтобы я мог начать делиться теплом и улыбками! 😊🤗"
        )

# Правила и инструкции при /rules
async def rules(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🌟 Правила и инструкции для милых обнимашек! 💖\n\n"
        "Чтобы я начал работать в чате, добавьте меня туда. После этого пишите:\n"
        "🔹 'Обнимаю' или 'Обнимаю @имя', чтобы я ответил милым обнимашкой! 🤗\n"
        "🔹 'Поцеловал' или 'Поцеловал @имя', чтобы я ответил поцелуем! 💋\n"
        "🔹 'Люблю' или 'Люблю @имя', чтобы я сказал, что люблю! ❤️\n\n"
        "Давайте наполняем наши чаты теплом и улыбками! 😊✨"
    )

# Обработка любых сообщений для реакции
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    message = update.message
    sender_name = message.from_user.first_name or message.from_user.username
    text = message.text.lower()

    # Списки ключевых слов
    keywords_love = ['люблю', 'обожаю', 'лю']
    keywords_kiss = ['поцеловал', 'чмок', 'целуюсь', 'целую']
    keywords_hug = ['обнимаю', 'обними', 'обнял']

    love_emojis = '❤️😍😘'
    kiss_emojis = '💋😚💖'
    hug_emojis = '🤗💞💓'

    # Реакции
    if any(word in text for word in keywords_love):
        if message.reply_to_message:
            target_user = message.reply_to_message.from_user
            target_name = target_user.username or target_user.first_name
            if not target_name:
                return
            reply_text = f"{love_emojis} @{sender_name} любит @{target_name} {love_emojis}"
        else:
            mentions = re.findall(r'@(\w+)', message.text)
            if mentions:
                target_name = mentions[0]
                reply_text = f"{love_emojis} @{sender_name} любит @{target_name} {love_emojis}"
            else:
                return
        await message.reply_text(reply_text)

    elif any(word in text for word in keywords_kiss):
        if message.reply_to_message:
            target_user = message.reply_to_message.from_user
            target_name = target_user.username or target_user.first_name
            if not target_name:
                return
            reply_text = f"{kiss_emojis} @{sender_name} поцеловал @{target_name} {kiss_emojis}"
        else:
            mentions = re.findall(r'@(\w+)', message.text)
            if mentions:
                target_name = mentions[0]
                reply_text = f"{kiss_emojis} @{sender_name} поцеловал @{target_name} {kiss_emojis}"
            else:
                return
        await message.reply_text(reply_text)

    elif any(word in text for word in keywords_hug):
        if message.reply_to_message:
            target_user = message.reply_to_message.from_user
            target_name = target_user.username or target_user.first_name
            if not target_name:
                return
            reply_text = f"{hug_emojis} @{sender_name} обнимаю @{target_name} {hug_emojis}"
        else:
            mentions = re.findall(r'@(\w+)', message.text)
            if mentions:
                target_name = mentions[0]
                reply_text = f"{hug_emojis} @{sender_name} обнимаю @{target_name} {hug_emojis}"
            else:
                return
        await message.reply_text(reply_text)

def main():
    TOKEN = '   '  # вставьте сюда свой токен

    application = ApplicationBuilder().token(TOKEN).build()

    # Обработка команд /start и /rules
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("instructions", rules))
    # Обработка любых сообщений
    application.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), handle_message))
    application.run_polling()

if __name__ == '__main__':

    main()
