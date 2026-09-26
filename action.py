from pyrogram import Client, filters, enums
from pyrogram.errors import ContinuePropagation

# This function runs before all other plugins because of group=-1
@Client.on_message(filters.incoming & filters.private, group=-1)
async def typing_action_status(bot, message):
    try:
        # Triggers the "typing..." animation for the user
        await bot.send_chat_action(message.chat.id, enums.ChatAction.TYPING)
    except Exception as e:
        print(f"Chat Action Error: {e}")
        pass
    
    # Continues processing the message to your other 10 files
    raise ContinuePropagation
