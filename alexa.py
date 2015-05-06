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
    def __init__(self, reply):
        self.reply = reply
