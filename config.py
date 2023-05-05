import os
import logging
class Config:
    
    API_ID = 16448144
    API_HASH = "1073665850700150caf0e0cbb68216a2"
    BOT_TOKEN = "6042686351:AAE_USR81Wy0Km66NKKSCEjQiU50du2eebc"
    BOT_SESSION = "Rentrox_Forward_BOT"
    OWNER_ID = "5163706369"
    DATABASE_URI = "mongodb+srv://Boyuserrentrox:mg1BbXIGzcqXXTJG@cluster0.l1xnuaj.mongodb.net/?retryWrites=true&w=majority"
    DATABASE_NAME = "Cluster0"
    COLLECTION_NAME = 'Rentrox_Forward_data'
    SESSION = "BQCW-kwbJ3YL0jLCJ6_tXGJBzNAP29HgsM8GbxKrIjrbyZRW7NUMCWbz7iC3O_QvSgymzVRqAX1eV2rTC9j88F3gAQQDX_-OqUv3DCezLY-At55XvgFQBaaTJTM9sjT36Vp3ZaqNPWq0qXtH8x7NJKKRsV72j6Zh1oP9QWd4CsFLfeX3v3YKCN8IMX1-hAyEWYb0njLa9d4FEqlnoWA84HspXc26YtaeqpqyBgxrsOzzcOuwmrrYPo58IF0SNZhr8AzgFj6Q6bnzCbL0jeZUDTiNwKACc-ou5GIZtMeJKyw05wAym89wmtvruJpistLjSNUOvE1c7KGVPdC2glyDJN0YAAAAAW8HBfYA"
    

    TO_CHANNEL = -1001559863637
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
