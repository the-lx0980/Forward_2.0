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
    SESSION = "BQAO68s2Ny4y6_5NpGP3ZVWcYICpufNpc9nf0AAdZTaITWiDO6wk4Xb2alAeV-EBwNS9f9TRUeYr5N8X2OcYJ0tWB2RBQhP4d6sI9z-cJqBVOIvCBvjteHMI1NDV_cckVsHI2Mwo0hMPqXFnzseNFDIPHjduRSb2yQl6Zxw1O7TRJTHEwHcRoiP3zAMRXp7XfK52islUXfWXL0Ie2cgYEm7t1dPkUWHiDBNf5eStLWIQEPQwVB0WicttyLZQTgEidzlIQpsrsI3dQ-Xa0Hshyqch49JEi-F3zyqEyaioj6d0hLNxCTbw1AvSlyMl01QgXOADFx06CjfcamKWC612Aq7aAAAAAW8HBfYA"
    TO_CHANNEL = -1001559863637
    BOT_USERNAME= "RentroxAutoCloneBot"


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
