#coding=utf8
import itchat
#from tuling import get_response
from xiaoirobot import get_response
import sys  

reload(sys)  
sys.setdefaultencoding('utf8')

flag = 0
flag_group = 0

#prefix = "[自动回复]"

textUserName = "Arex"
groupUserName = "阿瑞斯"

@itchat.msg_register('Text')
def text_reply(msg):
	global flag
	if 'help' in msg['Text'].lower():
		return '\
回复 open 开启机器人\n\
回复 close 关闭机器人\n\
回复 arex 浏览我的博客'
	elif 'open' in msg['Text'].lower(): 
		flag = 1
		return '机器人已开启'
	elif 'close' in msg['Text'].lower(): 
		flag = 0
		return '机器人已关闭'
	elif 'arex' in msg['Text'].lower(): 
		return 'http://arexchu.github.io'
	#elif 'picture' in msg['Text'].lower():
	#	itchat.send('@img@Himalayas.jpg', msg['FromUserName']) # there should be a picture
	elif flag:
		print '%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName']
		if msg['FromUserName'] == friends:
			reply = get_response(msg['Text'])
			print reply
		else:
			reply = get_response(msg['Text'])
			#reply = prefix + reply
			print reply
			return reply
	else:
		return

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
	global flag_group
	if msg['FromUserName'] == chatrooms: 
		if msg['isAt']:
			return '\
回复 open 开启机器人\n\
回复 close 关闭机器人\n\
回复 arex 浏览我的博客'
		elif 'open' in msg['Text'].lower(): 
			flag_group = 1
			return '机器人已开启'
		elif 'close' in msg['Text'].lower(): 
			flag_group = 0
			return '机器人已关闭'
		elif 'arex' in msg['Text'].lower(): 
			return 'http://arexchu.github.io'
		elif flag_group:
			print '%s: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName']
			reply = get_response(msg['Content'])
			print reply
			return reply
		else:
			return

itchat.auto_login(True)
#itchat.get_friends(update=True)
friends = itchat.search_friends(name=textUserName)[0]["UserName"]
#print friends
chatrooms = itchat.search_chatrooms(name=groupUserName)[0]["UserName"]
#print chatrooms
itchat.run()
