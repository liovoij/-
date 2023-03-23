# coding:utf-8
import requests
import json
import pprint
import time
from tools.parse_confile import ParseConfile


class new_request(object):
    def __init__(self):
        self.cf = ParseConfile()
        self.protocal = self.cf.get_account('new_demo', 'protocal')
        self.host = self.cf.get_account('new_demo', 'host')
        self.requestPath = self.cf.get_account('new_demo', 'requestpath')
        self.url = self.protocal + self.host + self.requestPath

    def response_get(self, corpus):
        response = requests.request('get', url=self.url + corpus)
        # time.sleep(0.1)
        responseText = response.text
        return responseText

    def response_handle(self, reponseText):
        response_data = json.loads(reponseText)
        result_data = response_data['data']
        if not result_data:
            return "[]"
        else:
            return result_data[0]['intent_path']

    def get_child_intent(self, reponseText):
        response_data = json.loads(reponseText)
        result_data = response_data['data']
        if result_data == []:
            return "[]"
        elif (result_data != []) & (result_data[0]['child_intent'] == []):
            return "[]"
        else:
            return result_data[0]['child_intent'][0]['intent_path']

    def get_children_intent(self, reponseText):
        response_data = json.loads(reponseText)
        result_data = response_data['data']
        if result_data == []:
            return "[]"
        elif (result_data != []) & (result_data[0]['child_intent'] == []):
            return "[]"
        else:
            return result_data[0]['child_intent'][0]['intent_path']


if __name__ == '__main__':
    # r = NewDemoRequest()
    # print(r.doGet("出差"))
    data = json.loads(new_request().response_get("请假"))
    pprint.pprint(data)
