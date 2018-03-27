import logging
from io import BytesIO
from pathlib import Path

import requests
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

from .config import TOKEN


def post(contents):
    headers = {'Content-Type': 'application/octet-stream'}
    resp = requests.post('https://paste.rs/', data=contents, headers=headers)
    return resp.text.strip()


def handle_file(bot, update):
    document = update.message.document

    if document.mime_type.split('/')[0] != 'text':
        return

    file_contents = BytesIO()
    document.get_file().download(out=file_contents)

    extension = Path(document.file_name).suffix

    link = post(file_contents.getvalue())
    update.message.reply_text(f'{link}{extension}')


def handle_start(bot, update):
    update.message.reply_text("Ciao! Send me text a file and I'll upload it"
                              "to paste.rs and give you the link.\n"
                              "You can also add me to groups ;)")


def handle_error(bot, update, error):
    update.message.reply_text(error)


def main():
    logging.basicConfig()

    updater = Updater(TOKEN)

    start_handler = CommandHandler('start', handle_start)
    updater.dispatcher.add_handler(start_handler)

    file_handler = MessageHandler(Filters.document, handle_file)
    updater.dispatcher.add_handler(file_handler)

    updater.dispatcher.add_error_handler(handle_error)

    updater.start_polling()


if __name__ == '__main__':
    main()
