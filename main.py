from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# 替换为你的机器人token
TOKEN = "7971409482:AAFrMTCMeNMfmGcxdeJVpzKgL9JG2tgLX1M"
BOT_USERNAME = "@DvboxBot"

async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("你好！我是一个回声机器人，发送任何消息我都会回传给你。")

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("只需发送任何消息，我会将它回传给你！")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    await update.message.reply_text(f"你说了: {user_message}")

def main():
    print("启动机器人...")
    app = Application.builder().token(TOKEN).build()

    # 命令处理器
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))

    # 消息处理器
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    # 错误处理
    # app.add_error_handler(error)

    # 轮询
    print("轮询中...")
    app.run_polling(poll_interval=3)

if __name__ == "__main__":
    main()