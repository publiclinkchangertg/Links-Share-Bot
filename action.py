import asyncio
from pyrogram import Client, filters, enums
from pyrogram.errors import ContinuePropagation

@Client.on_message(filters.incoming & filters.private, group=-1)
async def typing_action_status(bot, message):
    try:
        # एनीमेशन चालू करेगा
        await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
        
        # बॉट को ज़बरदस्ती 2.5 सेकंड रोकेगा ताकि तुझे स्क्रीन पर "typing..." दिखे
        await asyncio.sleep(2.5) 
    except Exception:
        pass
    
    # इसके बाद मैसेज को तेरी बाकी 10 फाइल्स के पास भेज देगा
    raise ContinuePropagation
