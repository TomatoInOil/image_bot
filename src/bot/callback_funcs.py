import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto, Update
from telegram.ext import ContextTypes, ConversationHandler

from bot import api_service
from bot.logger import log_start_and_end

_LOGGER = logging.getLogger(__name__)
WAITING_FOR_PHOTO = 1


@log_start_and_end(logger=_LOGGER)
async def send_submit_button(
    update: Update, _context: ContextTypes.DEFAULT_TYPE
) -> int:
    await update.effective_chat.send_message(
        text="Отправь фотографии, а затем нажми на кнопку, чтобы их сохранить.",
        reply_markup=InlineKeyboardMarkup.from_button(
            InlineKeyboardButton(text="Сохранить", callback_data="save_photos")
        ),
    )
    return WAITING_FOR_PHOTO


@log_start_and_end(logger=_LOGGER)
async def handle_photo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    file_id = update.effective_message.photo[-1].file_id
    new_file = await context.bot.get_file(file_id)
    photo_bytearray = await new_file.download_as_bytearray()
    await api_service.save_photo(
        photo_bytearray=photo_bytearray, filename=new_file.file_path, file_id=file_id
    )
    received_photos = context.user_data.get("received_photos")
    if received_photos:
        received_photos.append(InputMediaPhoto(file_id))
    else:
        context.user_data["received_photos"] = [
            InputMediaPhoto(file_id, caption="Отличные фотографии!")
        ]
    return None


@log_start_and_end(logger=_LOGGER)
async def send_received_photos(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> int:
    await update.effective_message.edit_reply_markup()
    await update.effective_chat.send_media_group(
        media=context.user_data.get("received_photos")
    )
    context.user_data.clear()
    return ConversationHandler.END
