import logging
from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6232632255:AAHDfChw69jKwJO0aUFOQ-sY9mlJ-yYU8Js'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.reply('Я нахожусь в разработке.\nЭто приветственное сообщение.')

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
