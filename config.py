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
    SESSION = "BQC-84ergJSnJgRTe5IEke1Jbtrau7e0nohG6JNZ7BEaNRLGMNlqZ_ZhTRT75EpeD1zvFP5_HqD-Re3-avmoycUGsmvWULcgq43jb07kDhtzNdOgCaSAS90TMjw3qPrxle9gHhpH8e-7p9ihnLLeKnM3J_3qZ0p8Td_dz_Hwmj4x9eEEkWATZuigD2E_oMZcbqHSRhDRWj5Z5FbwetD1T7ALIu9lbgMCgFjoEPUWJn59txuftitgPqSBERIMs8ZZCOHubNjt9KWvNjIWbKTs3gBdsZ_PNoUJ6YZflBaRex0zW5tMzU1uypzOmI5jkhrfIxFLYYLPjXeh18dRazicS6sDAAAAAW8HBfYA"
    TO_CHANNEL = -1001559863637
    BOT_USERNAME= os.environ.get("BOT_USERNAME", None)


def LOGGER(name: str) -> logging.Logger:
    return logging.getLogger(name)
