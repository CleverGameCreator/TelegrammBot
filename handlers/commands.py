from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandStart


router = Router()



# Функция /start при нажатии пишет текст
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Привет, чел!   нажми /help')

# Функция /help при нажатии пишет текст
@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer('Я готов помогать! (Но это не точно)')


@router.message(Command('about'))
async def cmd_about(message: Message):
    await message.answer('Я бот который был  создан человеком нефором он любит жесткие  тусы и веселье :)')


'''
# Если ввести слово Привет то бот пишет Привет!
@router.message(F.photo)
async def cmd_hello(message: Message):
    pphoto = message.photo
    text = "Какое красивое фото!"
    await message.answer_photo(pphoto[0].file_id, text)


@router.message()
async def handle_messages(message: Message):
    if message.text:
        await message.answer("Это текстовое сообщение!")
    elif message.photo:
        await message.answer("Спасибо за фото!")
    elif message.video:
        await message.answer("Спасибо за видео!")
    elif message.document:
        await message.answer("Спасибо за документ!")
    elif message.audio:  # Исправлено sessage -> message
        await message.answer("Спасибо за аудио!")
    elif message.voice:
        await message.answer("Спасибо за голосовое сообщение!")
    elif message.location:  # Исправлено ellf -> elif
        await message.answer(f"Вы отправили местоположение: {message.location.latitude}, {message.location.longitude}")
    elif message.contact:
        # Исправлены опечатки и синтаксис
        await message.answer(f"Контакт: {message.contact.first_name} ({message.contact.phone_number})")
    else:
        await message.answer("Получено сообщение неизвестного типа")

# Если ввести слово Привет то бот пишет Привет!
@router.message(F.text == "Привет")
async def cmd_hello(message: Message):
    await message.reply(f'Привет!')

# Если ввести слово Привет то бот пишет Привет (имя)!
@router.message(F.text == "Привет")
async def cmd_hello(message: Message):
    name = message.from_user.first_name
    await message.answer(f'Привет {name}!')

# Если ввести любое слово то бот выдаст это же слово
@router.message(F.text)
async def cmd_hello(message: Message):
    text = message.text
    await message.answer((f'Вы написали: {text}'))
'''