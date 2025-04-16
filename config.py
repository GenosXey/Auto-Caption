# (c) @RknDeveloperr
# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr

import re, os, time
id_pattern = re.compile(r'^.\d+$') 

class Rkn_Bots(object):
    
    # Rkn client config  ( required.. 😥)
    API_ID = os.environ.get("API_ID", "24817837")
    API_HASH = os.environ.get("API_HASH", "acd9f0cc6beb08ce59383cf250052686")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "7598768754:AAFjjQR0rs8uyF81zXKYnCEPq62blYUyW-s")

    # start_pic
    RKN_PIC = os.environ.get("RKN_PIC", "https://telegra.ph/file/21a8e96b45cd6ac4d3da6.jpg")

    # wes response configuration
    BOT_UPTIME = time.time()
    PORT = int(os.environ.get("PORT", "8080"))

    # force subs channel ( required.. 😥)
    FORCE_SUB = os.environ.get("FORCE_SUB", "BotZFlix") 
    
    # database config ( required.. 😥)
    DB_NAME = os.environ.get("DB_NAME", "Aniflix")     
    DB_URL = os.environ.get("DB_URL", "mongodb+srv://Aniflix:Lipun123@aniflix.q2wina5.mongodb.net/?retryWrites=true&w=majority&appName=Aniflix")

    # default caption 
    DEF_CAP = os.environ.get("DEF_CAP", "<b>Chaîne Telegram: @KGCAnime</b>",
    )

    # sticker Id
    STICKER_ID = os.environ.get("STICKER_ID", "CAACAgIAAxkBAAIIXGf_-25yBWQGpebD_kiDCJqlNzPFAAJcAQACPQ3oBAABMsv78bItBB4E")

    # admin id  ( required.. 😥)
    ADMIN = [int(admin) if id_pattern.search(admin) else admin for admin in os.environ.get('ADMIN', '7428552084').split()]
    

# Rkn Developer 
# Don't Remove Credit 😔
# Telegram Channel @RknDeveloper & @Rkn_Botz
# Developer @RknDeveloperr
