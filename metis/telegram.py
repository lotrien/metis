import telegram


class Telegram:

    def __init__(self, token, recipient_id):
        self._recipient_id = recipient_id
        self._bot = telegram.Bot(token)

    def send_message(self, msg):
        self._bot.send_message(chat_id=self._recipient_id, text=msg)

    def send_doc(self, path):
        with open(path, 'rb') as doc:
            self._bot.send_document(chat_id=self._recipient_id, document=doc)
