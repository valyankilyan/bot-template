from bot import bot
import answers
from loggerconfig import getLogger
logger = getLogger(__name__)
logger.info("Starting bot ")

@bot.message_handler(commands=['start'])
def send_welcome(message):
    logger.info(f'{message.from_user.username} sent {message.text}')
    bot.send_message(message.chat.id, answers.start)


@bot.message_handler(commands=['help'])
def send_help(message):
    logger.info(f'{message.from_user.username} sent {message.text}')
    bot.send_message(message.chat.id, answers._help)


@bot.message_handler(func=lambda m: True)
def error(message):
    logger.info(f'{message.from_user.username} sent {message.text}')
    bot.reply_to(message, answers.error)    
