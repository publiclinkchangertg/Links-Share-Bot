import asyncio
from pyrogram import Client, filters, enums
from pyrogram.errors import ContinuePropagation

@Client.on_message(filters.incoming & filters.private, group=-1)
async def typing_action_status(bot, message):
    try:
        # एनीमेशन चालू करेगा
        await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
        
        # 1.5 सेकंड का ब्रेक लेगा ताकि यूज़र को एनीमेशन दिखे
        await asyncio.sleep(1.5) 
    except Exception as e:
        print(f"Chat Action Error: {e}")
        pass
    
    # काम खत्म होने के बाद मैसेज को तेरी बाकी फाइल्स के पास भेज देगा
    raise ContinuePropagation
