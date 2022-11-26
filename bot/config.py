import os

class Config:
    TELEGRAM_TOKEN=os.environ["TELEGRAM_TOKEN", "5919847405:AAEASoQD1KnDBuPGr60xa8GUhUWjAUlIAPk"]
    SUDOS=os.environ["SUDOS", "1964732367"]
    TELEGRAM_APP_HASH=os.environ["TELEGRAM_APP_HASH", "1c40c54693e2cdbe51f90a152ed1bd5f"]
    TELEGRAM_APP_ID=int(os.environ["TELEGRAM_APP_ID", "5994204"])
    
    if not TELEGRAM_TOKEN:
        raise ValueError("TELEGRAM BOT TOKEN not set")
    
    if not TELEGRAM_APP_HASH:
        raise ValueError("TELEGRAM_APP_HASH not set")

    if not TELEGRAM_APP_ID:
        raise ValueError("TELEGRAM_APP_ID not set")
