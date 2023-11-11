from aiogram import Bot, Dispatcher,executor,types
from aiogram.types.web_app_info import WebAppInfo


bot = Bot('6930965554:AAFxd4TyhextP5rXy2_A_aQk59Nwl1Eawhc')
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start (message: types.Message):
    markup = types.ReplyKeyboardMarkup()
    markup.add(types.KeyboardButton('Открыть веб стрницу',web_app=WebAppInfo(url='https://qna.habr.com/q/1304534')))
    await message.answer('Привет мой друг', reply_markup=markup)


executor.start_polling(dp)