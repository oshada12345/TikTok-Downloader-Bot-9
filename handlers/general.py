
import os

from aiogram import Router
from aiogram.types import Message, FSInputFile
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext

from bot.ext import keyboards, GetUrl, TikTok
from bot.filters import UrlFilter, CancelFilter
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery




router = Router(name="General Handler")
#Button
START_BUTTONS=[
    [
        InlineKeyboardButton("Manuja", url="https://t.me/boolen3xd"),
        InlineKeyboardButton("Vimukthi", url="https://t.me/vimukthioshada"),
    ],
]




async def get_url(message: Message) -> None:
    await message.reply_sticker('CAACAgUAAxkBAAEB2OtkgFNpCSVb3ukEv8_J796JtCyn-gACNwUAAuBGiVTP-IZF8MfuMi8E')
    await message.answer(
        "🚀 DOᗯᑎᒪOᗩᗪIᑎG Video TO Sᕮᖇᐯᕮᖇ ....",
        reply_markup=InlineKeyboardMarkup(START_BUTTONS))
    
     

    try:
        tik_tok = TikTok(message.text)

        video = tik_tok.download_video(f"{message.from_user.username}.mp4")
        aiovideo = FSInputFile(video)

        await message.answer_video(video=aiovideo)
        os.remove(video) 
        
          # Get the video caption
        caption = tik_tok.get_video_caption("fk")

        await message.answer_video(video=aiovideo)
        os.remove(video)

    except Exception:
        await message.answer('\n\n [🏖 @boolen3xd] \n\n[🔥 @vimukthioshada] ')
      
    




