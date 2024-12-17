from pyrogram import Client
from info import *
from aiohttp import web
from route import web_server

class Bot(Client):

    def __init__(self):
        super().__init__(
            name="tgbot",
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=200,
            plugins={"root": "plugins"},
            sleep_threshold=10,
        )

    async def start(self):
        await super().start()
        me = await self.get_me()
        self.id = me.id
        self.name = me.first_name
        self.mention = me.mention
        self.username = me.username
        self.force_channel = FORCE_SUB if FORCE_SUB else None  
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()      
        print(f'{me.first_name} is Started...🍃')

    async def stop(self, *args):
        await super().stop()      
        print("Bot restarting.....")
        
                           
  
app = Bot()
app.run()


        










