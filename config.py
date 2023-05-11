import os
import logging
class Config:
    
    API_ID = 16448144
    API_HASH = "1073665850700150caf0e0cbb68216a2"
    BOT_TOKEN = "6042686351:AAE_USR81Wy0Km66NKKSCEjQiU50du2eebc"
    BOT_SESSION = "Rentrox_Forward_BOT"
    OWNER_ID = "6157698550"
    DATABASE_URI = "mongodb+srv://Boyuserrentrox:mg1BbXIGzcqXXTJG@cluster0.l1xnuaj.mongodb.net/?retryWrites=true&w=majority"
    DATABASE_NAME = "Cluster0"
    COLLECTION_NAME = 'Rentrox_Forward_data'
    SESSION = os.environ.get("SESSION")
    TO_CHANNEL = -1001559863637
    BOT_USERNAME= "RentroxAutoCloneBot"


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
