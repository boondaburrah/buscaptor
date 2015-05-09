__author__ = 'boondaburrah'


class Intent:
    def __init__(self, json_data):
        if json_data['request']['type'] == "IntentRequest" and json_data['version'] == "1.0":
            self.json_data = json_data
        else:
            raise RuntimeError("Data received wasn't an intent request.")

    def get_amazon_user(self):
        return self.json_data['session']['user']['userId']

    def get_type(self):
        return self.json_data['request']['intent']['name']


class Response:
    def __init__(self):
        self.close_session = True
        self.speech = dict()
        self.card = dict()

    def set_voice(self, text):
        self.speech['type'] = "PlainText"
        self.speech['text'] = text

    def set_card(self, title, subtitle, text):
        self.card['type'] = "Simple"
        self.card['title'] = title
        self.card['subtitle'] = subtitle
        self.card['content'] = text

    def set_close(self, yn):
        self.close_session = yn

