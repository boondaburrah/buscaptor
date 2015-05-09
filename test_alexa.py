__author__ = 'lukeberr'
from alexa import Intent
import nose


class test_alexa:

    sample_intent = dict()

    def setup(self):
        self.sample_intent['version'] = "1.0"
        self.sample_intent['session'] = dict()
        self.sample_intent['session']['new'] = True
        self.sample_intent['session']['sessionId'] = "amzn1.echo-api.session.abeee1a7-aee0-41e6-8192-e6faaed9f5ef"
        self.sample_intent['session']['user'] = dict()
        self.sample_intent['session']['user']['userId'] = "amzn1.account.AM3B227HF3FAM1B261HK7FFM3A2"
        self.sample_intent['request'] = dict()
        self.sample_intent['request']['type'] = "IntentRequest"
        self.sample_intent['request']['requestId'] = " amzn1.echo-api.request.6919844a-733e-4e89-893a-fdcb77e2ef0d"
        self.sample_intent['request']['intent'] = dict()
        self.sample_intent['request']['intent']['name'] = "GetBus"
        self.sample_intent['request']['intent']['slots'] = dict()
        self.sample_intent['request']['intent']['slots']['route'] = dict()
        self.sample_intent['request']['intent']['slots']['route']['name'] = "route"
        self.sample_intent['request']['intent']['slots']['route']['value'] = 66


    def teardown(self):
        pass

    def test_intent_detection(self):
        intent = Intent(self.sample_intent)
