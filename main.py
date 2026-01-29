from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, ContextTypes, ChatMemberHandler, CommandHandler

WELCOME_TEXT = "Привет, {name}! 👋\nДобро пожаловать в наш чат 💬\nНажми кнопку ниже, чтобы получить приветственное сообщение в личку!"

PRIVATE_TEXT = "Привет, {name}! 🌟\nРады видеть тебя в нашем сообществе!\nЕсли будут вопросы — пиши сюда 💌"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    name = update.effective_user.first_name
    await update.message.reply_text(PRIVATE_TEXT.format(name=name))

async def welcome(update: Update, context: ContextTypes.DEFAULT_TYPE):
    result = update.chat_member
    if result.new_chat_member.status == "member":
        user = result.new_chat_member.user
        name = user.first_name

        button = InlineKeyboardMarkup([
            [InlineKeyboardButton("Получить приветствие 💌", url=f"https://t.me/{context.bot.username}?start=welcome")]
        ])

        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=WELCOME_TEXT.format(name=name),
            reply_markup=button
        )

app = ApplicationBuilder().build()
app.add_handler(CommandHandler("start", start))
app.add_handler(ChatMemberHandler(welcome, ChatMemberHandler.CHAT_MEMBER))
app.run_polling()
