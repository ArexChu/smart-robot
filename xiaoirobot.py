# -*- coding: utf-8 -*-

import sys, os
import xiaoi.ibotcloud
import json

try:
	with open('xiaoirobot.json') as f: 
		data = json.loads(f.read())
		test_key = data["key"]
		test_sec = data["sec"]

except:
	test_key = '' # if key is '', get_response will return None
	test_sec = ''

signature_ask = xiaoi.ibotcloud.IBotSignature(app_key=test_key,
                                              app_sec=test_sec,
                                              uri="/ask.do",
                                              http_method="POST")

signature_reg = xiaoi.ibotcloud.IBotSignature(app_key=test_key,
                                              app_sec=test_sec,
                                              uri="/recog.do",
                                              http_method="POST")

signature_tts = xiaoi.ibotcloud.IBotSignature(app_key=test_key,
                                              app_sec=test_sec,
                                              uri="/synth.do",
                                              http_method="POST")

params_tts = xiaoi.ibotcloud.TTSParams(url="http://vcloud.xiaoi.com/synth.do")
params_reg = xiaoi.ibotcloud.RegParams(url="http://vcloud.xiaoi.com/recog.do")
params_ask = xiaoi.ibotcloud.AskParams(platform="custom",
                                       user_id="abc",
                                       url="http://nlp.xiaoi.com/ask.do",
                                       response_format="xml")

ask_session = xiaoi.ibotcloud.AskSession(signature_ask, params_ask)
reg_session = xiaoi.ibotcloud.RegSession(signature_reg, params_reg)
tts_session = xiaoi.ibotcloud.TTSSession(signature_tts, params_tts)

# demo how to get answer
def get_response(msg):
	try:
		#msg = '你好'
		ret_ask = ask_session.get_answer(msg)
		r = ret_ask.http_body
		return r
	except:
		return

if __name__ == '__main__':
	try:
		ipt = raw_input
		ipt = lambda: raw_input('>')
	except:
		ipt = lambda: input('>')
	while True:
		a = ipt()
		print(get_response(a))
