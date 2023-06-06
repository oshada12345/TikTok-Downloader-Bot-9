from aiogram.filters import BaseFilter
from aiogram.types import Message



class UrlFilter(BaseFilter):
    """Url Filter."""
    async def __call__(self, message: Message) -> bool:
        if message.text.startswith("https://www.tiktok.com/") \
        or message.text.startswith("https://vt.tiktok.com/"):
            return True
        
        await message.reply_sticker('CAACAgUAAxkBAAED9kRiDq_GkOHuRHPeVv4IRhsvy4NtbwACqQQAAncUyFftN80YUiyXnyME')

        return False
        
