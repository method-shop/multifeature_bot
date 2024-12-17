from pyrogram import Client, filters
from pyrogram.types import InputMediaPhoto
import json
import aiohttp

@Client.on_message(filters.command("image"))
async def image_search(client, message):
    try:
        text = message.text.split(None, 1)[1] 
    except IndexError:
        return await message.reply_text(
            "Provide me a query to search! like /image luffy"
        )  
    
    search_message = await message.reply_text("🔎 Searching for images...")
    
    async with aiohttp.ClientSession() as session:
        async with session.get(f"https://horridapi.onrender.com/image_search?query={text}") as resp:
            images = json.loads(await resp.text())  # Parse the response JSON into a list of image URLs

    media = []
    count = 0
    for img in images:
        if count == 7:
            break
       
        media.append(InputMediaPhoto(media=img))
        count += 1

    await search_message.edit_text(f"Found {count} images for your query!")
    await message.reply_media_group(media=media)    
    await search_message.delete()