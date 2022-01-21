import loggerconfig
import logging
logger = logging.getLogger(__name__)

import telebot 
from telebot.types import InputMediaPhoto
from config import IMAGE_UPLOAD_FOLDER

class myTeleBot(telebot.TeleBot):
    def sendPhoto(self, chat_id: int, photo, caption=None):
        out_photo = photo.telegram_id if photo.telegram_id else open(IMAGE_UPLOAD_FOLDER + f'/{photo.filename}', 'rb')        
        sent_data = self.send_photo(chat_id, out_photo, caption=caption)        
        if not photo.telegram_id:
            photo.telegram_id = sent_data.photo[0].file_id
            photo.commit()
        
    def sendMediaGroup(self, chat_id: int, photos, caption=None):
        out_photos = []
        for p in photos[:10]:
            _file = p.telegram_id if p.telegram_id else open(IMAGE_UPLOAD_FOLDER + f'/{p.filename}', 'rb')            
            out_photos.append(InputMediaPhoto(_file))
        out_photos[-1].caption = caption
        sent_data = self.send_media_group(chat_id, out_photos)
        logger.info(f'photos {sent_data[0]} was sent')
        for i in range(len(photos[:10])):
            if not photos[i].telegram_id:
                # logger.info(f'file_id = {sent_data[i].photo[0].file_id}')
                photos[i].telegram_id = sent_data[i].photo[0].file_id