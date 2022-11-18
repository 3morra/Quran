import asyncio, os

from pyrogram import Client, filters, enums

from pytgcalls import PyTgCalls 

from pytgcalls import idle

from pytgcalls import StreamType

from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped

from pytgcalls.types.input_stream.quality import HighQualityAudio,    HighQualityVideo,    LowQualityVideo,    MediumQualityVideo

from pytube import YouTube

import aiohttp

from Python_ARQ import ARQ

from pyrogram.types import Message

ARQ_API_KEY = "HMPXNS-BDPCCB-UJKRPU-OQADHG-ARQ"

aiohttpsession = aiohttp.ClientSession()

arq = ARQ("https://thearq.tech", ARQ_API_KEY, aiohttpsession)

API_ID = int(os.getenv("API_ID"))
CHAT_ID = int(os.getenv("CHAT_ID"))
API_HASH = os.getenv("API_HASH")
LINK = os.getenv("LINK")
SESSION = os.getenv("SESSION")

app = Client(

    "MyBot",

    api_id=API_ID,

    api_hash=API_HASH,
    
    session_string=SESSION

)

call_py = PyTgCalls(app)
    

@app.on_message(filters.command("play"))
async def play(client, message):
    await message.delete()
    if len(message.text.split()) < 2:
     return 
    try:
      yt = YouTube(message.text.split()[1])
    except:
      return await message.reply("رابط المقطع غير صحيح")
    await message.reply("Downloading ...")
    dl = yt.streams.get_audio_only().download(output_path='/cache')
    await call_py.join_group_call(                    chat_id,                    AudioPiped(                        dl,                    ),                    stream_type=StreamType().pulse_stream,                )
    await message.reply("Done")
    await app.read_chat_history(message.chat.id)



async def main():
    await app.start()
    print(" Deployed Successfully✅")
    await call_py.start()
    yt = YouTube(LINK)
    dl = yt.streams.get_audio_only().download(output_path='/cache')
    for a in range(1000000000000000):
       await call_py.join_group_call(CHAT_ID,AudioPiped(dl,),stream_type=StreamType().pulse_stream,)
       print("Done ✅")
       await asyncio.sleep(yt.length+5)
    await idle()
    await app.stop()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())
