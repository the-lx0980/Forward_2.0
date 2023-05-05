import os
import logging
class Config:
    
    API_ID = 16448144
    API_HASH = "1073665850700150caf0e0cbb68216a2"
    BOT_TOKEN = "6042686351:AAF9vyXdL2BRIkWu8dFRkLva1GvW0KjrOtY"
    BOT_SESSION = "Rentrox_Forward_BOT"
    OWNER_ID = "5163706369"
    DATABASE_URI = "mongodb+srv://Boyuserrentrox:mg1BbXIGzcqXXTJG@cluster0.l1xnuaj.mongodb.net/?retryWrites=true&w=majority"
    DATABASE_NAME = "Cluster0"
    COLLECTION_NAME = 'Rentrox_Forward_data'
    SESSION = "BQCZx6_wR5qum-ro7v7Bu2DfcOsWT08O5mgknvGZ0jk3103xExKcxMFO11eB-KZ6zTjFv1NPCF3YLXL1zP9ZbY1uJ47cgxfasdVNuJpk0074lQUowF4eETicNrjg8yc_csCBshlFidYnffQX49wVc74x2VAX3P7UjKg2bxjSQ9MXrlc2R0Rzo_XPcUwsg3vf9iANbxTalIiW_mgiPJClx4A-ojBxLgHj7NsnkRQyg-Nk3J7LsjWKx4Le1g6wGYwyEpkJ7zbB0cTwQAkg_PzedHDDmqzqEvSJPU39bNBZiDY42M3M1VJCEoNBMbRe06QOa7hBf1x7SUeHWcT8ME8cWSgUAAAAAW8HBfYA"
    TO_CHANNEL = -1001559863637
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
