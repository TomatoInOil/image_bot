import logging
import os
from pathlib import Path

from dotenv import load_dotenv
from telegram.ext import (
    ApplicationBuilder,
    CallbackQueryHandler,
    CommandHandler,
    ConversationHandler,
    MessageHandler,
    filters,
)

from bot.callback_funcs import (
    WAITING_FOR_PHOTO,
    handle_photo,
    send_received_photos,
    send_submit_button,
)

_BASE_DIR = Path(__file__).parent

load_dotenv(dotenv_path=_BASE_DIR.parent / ".env")

_BOT_TOKEN = os.getenv("BOT_TOKEN")

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logging.getLogger("httpx").setLevel("WARNING")

photo_handler = ConversationHandler(
    entry_points=[CommandHandler("photo", send_submit_button)],
    states={
        WAITING_FOR_PHOTO: [
            MessageHandler(filters=filters.PHOTO, callback=handle_photo),
            CallbackQueryHandler(
                pattern=r"^save_photos", callback=send_received_photos
            ),
        ]
    },
    fallbacks=[],
)


def main():
    application = ApplicationBuilder().token(_BOT_TOKEN).build()
    application.add_handler(photo_handler)
    application.run_polling()


if __name__ == "__main__":
    main()
