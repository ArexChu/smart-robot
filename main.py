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

myUserName = "Arex"
friends = "@"
chatrooms = "@@"

@itchat.msg_register('Text')
def text_reply(msg):
	global flag
	if msg['FromUserName'] == arex:
		global flag_group
		if 'help' in msg['Text'].lower():
			return '\
input set friend or chatroom to choose a object\n\
input enable friend or chatroom to open the robot\n\
input disable friend or chatroom to close the robot\n\
input arex to visit my blog'
		if 'set' in msg['Text'].lower(): 
			if 'friend' in msg['Text'].lower(): 
				global friends
				textUserName = msg['Text']
				otherUserName = textUserName.split(" ")[2]
				friends = itchat.search_friends(name=otherUserName)[0]["UserName"]
				#print friends
			if 'chatroom' in msg['Text'].lower(): 
				global chatrooms
				contentUserName = msg['Text']
				groupUserName = contentUserName.split(" ")[2]
				chatrooms = itchat.search_chatrooms(name=groupUserName)[0]["UserName"]
				#print chatrooms
			#reply = get_response(msg['Text'])
			#print reply
			return 'object enabled'
		if 'enable' in msg['Text'].lower(): 
			if 'friend' in msg['Text'].lower(): 
				flag = 1
				return 'robot enabled'
			if 'chatroom' in msg['Text'].lower(): 
				flag_group = 1
				return 'robot enabled'
		if 'disable' in msg['Text'].lower(): 
			if 'friend' in msg['Text'].lower(): 
				flag = 0
				return 'robot disabled'
			if 'chatroom' in msg['Text'].lower(): 
				flag_group = 0
				return 'robot disabled'
	if msg['FromUserName'] == friends:
		if 'help' in msg['Text'].lower():
			return '\
回复 enable 开启arex机器人\n\
回复 disable 关闭arex机器人\n\
回复 arex 浏览我的博客'
		if 'enable' in msg['Text'].lower(): 
			flag = 1
			return 'robot enabled'
		if 'disable' in msg['Text'].lower(): 
			flag = 0
			return 'robot disabled'
		if 'arex' in msg['Text'].lower(): 
			return 'http://arexchu.github.io'
		#elif 'picture' in msg['Text'].lower():
		#	itchat.send('@img@Himalayas.jpg', msg['FromUserName']) # there should be a picture
		if flag:
			print '%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName']
			reply = get_response(msg['Text'])
			#reply = prefix + reply
			print reply
			return reply

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
	if msg['FromUserName'] == chatrooms: 
		if msg['isAt']:
			global flag_group
			if 'help' in msg['Text'].lower():
				return '\
回复 enable 同时@我 开启arex机器人\n\
回复 disable 同时@我 关闭arex机器人\n\
回复 arex 同时@我浏览我的博客'
			if 'enable' in msg['Text'].lower(): 
				flag_group = 1
				return 'robot enabled'
			if 'disable' in msg['Text'].lower(): 
				flag_group = 0
				return 'robot disabled'
			if 'arex' in msg['Text'].lower(): 
				return 'http://arexchu.github.io'
		if flag_group:
			print '%s: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName']
			reply = get_response(msg['Content'])
			print reply
			return reply

itchat.auto_login(True)
itchat.get_friends(update=True)
arex = itchat.search_friends(name=myUserName)[0]["UserName"]
#print arex
itchat.run()
