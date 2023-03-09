import json
import random

from aiogram.dispatcher.filters import Text
from resourses import results_text
from bot.creating import dp
from aiogram import types
import asyncio


@dp.message_handler(commands=["start"])
async def cmd_strat(message: types.Message):
    print("here")
    keyboard = types.InlineKeyboardMarkup(row_width=1)
    buttons = [types.InlineKeyboardButton(text="ИГРАЮ",
                                          callback_data="game")
               ]
    keyboard.add(*buttons)
    text = "Привет, я предлагаю сыграть тебе в одну игру 🎁\n\n" \
           "Ты можешь выиграть одну из скидок «0.8%, 8%, 18%, 28%, 38% или 38.8%»\n\n" \
           "Жми кнопку «ИГРАЮ», чтобы получить индивидуальный промокод на скидку"
    photo = types.InputFile("./images/hello.png")
    await message.answer_photo(photo=photo, caption=text, reply_markup=keyboard)


@dp.callback_query_handler(Text("game"))
async def game(call: types.CallbackQuery):
    with open("already_played.json", "r") as f:
        already_played = json.load(f)
        print(already_played)
        # мой - 505330351
        if call.from_user.id in already_played and call.from_user.id not in [505330351, 193305875, 5299691720,
                                                                             141811292, 401860914, 803812742,
                                                                             1114482386, 547170709, 5081356958,
                                                                             5770496288, 435590215]:
            await call.message.answer("Извини, но только один промокод для одного человека!")
            return
        else:
            if call.from_user.id not in [505330351, 193305875, 5299691720, 141811292, 401860914, 803812742, 1114482386,
                                         547170709, 5081356958, 5770496288, 435590215]:
                already_played.append(call.from_user.id)
    with open("already_played.json", "w") as f:
        json.dump(already_played, f)
    randomint = random.choices([1, 2, 3, 4, 5, 6], weights=[0.01, 0.1, 0.22, 0.42, 0.22, 0.01], k=1)[0]
    if randomint == 1:
        video = types.InputFile("./videos/08.mp4")
        await call.message.answer_video(video=open("./videos/08.mp4", "rb"))
        image = types.InputFile("./images/sale_images/08.png")
        video_text = "0.8"
        text = results_text["0.8"]
    elif randomint == 2:
        video = types.InputFile("./videos/8.mp4")
        await call.message.answer_video(video=open("./videos/8.mp4", "rb"))
        image = types.InputFile("./images/sale_images/8.png")
        video_text = "8"
        text = results_text["8"]
    elif randomint == 3:
        video = types.InputFile("./videos/18.mp4")
        await call.message.answer_video(video=open("./videos/18.mp4", "rb"))
        image = types.InputFile("./images/sale_images/18.png")
        video_text = "18"
        text = results_text["18"]
    elif randomint == 4:
        video = types.InputFile("./videos/28.mp4")
        await call.message.answer_video(video=open("./videos/28.mp4", "rb"))
        video_text = "28"
        image = types.InputFile("./images/sale_images/28.png")
        text = results_text["28"]
    elif randomint == 5:
        video = types.InputFile("./videos/38.mp4")
        await call.message.answer_video(video=open("./videos/38.mp4", "rb"))
        image = types.InputFile("./images/sale_images/38.png")
        video_text = "38"
        text = results_text["38"]
    elif randomint == 6:
        video = types.InputFile("./videos/388.mp4")
        await call.message.answer_video(video=open("./videos/388.mp4", "rb"))
        video_text = "38.8"
        image = types.InputFile("./images/sale_images/388.png")
        text = results_text["38.8"]
    #await call.message.answer_document(open("./videos/388.mp4", "rb"))
    await aiogram.methods.send_video.SendVideo(call.from_user.id,open("./videos/388.mp4", "rb"))
    await asyncio.sleep(15)
    await call.message.answer_photo(photo=image, caption=text)

@dp.message_handler()
async def aaaa(message: types.Message):
    print(message)