#coding=utf8
import itchat
from tuling import get_response

flag = 0
flag_group = 0

#prefix = "[自动回复]"

myUserName = "Arex"
friends = "@"
chatrooms = "@@"

@itchat.msg_register('Text')
def text_reply(msg):
	global flag
	if msg['FromUserName'] == mySelf:
		global flag_group
		if 'help' in msg['Text'].lower():
			print('\
input set friend or chatroom to choose a object\n\
input enable friend or chatroom to open the robot\n\
input disable friend or chatroom to close the robot')
			return '\
input set friend or chatroom to choose a object\n\
input enable friend or chatroom to open the robot\n\
input disable friend or chatroom to close the robot'
		if 'set' in msg['Text'].lower(): 
			if 'friend' in msg['Text'].lower(): 
				global friends
				textUserName = msg['Text']
				otherUserName = textUserName.split(" ")[2]
				itchat.get_chatrooms(update=True)
				friends = itchat.search_friends(name=otherUserName)[0]["UserName"]
				print("%s is seted" % otherUserName)
				return (otherUserName + "is seted") 
			if 'chatroom' in msg['Text'].lower(): 
				global chatrooms
				contentUserName = msg['Text']
				groupUserName = contentUserName.split(" ")[2]
				itchat.get_chatrooms(update=True)
				chatrooms = itchat.search_chatrooms(name=groupUserName)[0]["UserName"]
				print(chatrooms)
				print("%s is seted" % groupUserName)
				return (groupUserName + "is seted") 
		if 'enable' in msg['Text'].lower(): 
			if 'friend' in msg['Text'].lower(): 
				flag = 1
				print('robot is enabled')
				return 'robot is enabled'
			if 'chatroom' in msg['Text'].lower(): 
				flag_group = 1
				print('robot is enabled')
				return 'robot is enabled'
		if 'disable' in msg['Text'].lower(): 
			if 'friend' in msg['Text'].lower(): 
				flag = 0
				print('robot is disabled')
				return 'robot is disabled'
			if 'chatroom' in msg['Text'].lower(): 
				flag_group = 0
				print('robot is disabled')
				return 'robot is disabled'
		else:
			return get_response(msg['Text'])
	if msg['FromUserName'] == friends:
		if 'help' in msg['Text'].lower():
			return u'\
回复 enable 开启arex机器人\n\
回复 disable 关闭arex机器人'
		if 'enable' in msg['Text'].lower(): 
			flag = 1
			return 'robot is enabled'
		if 'disable' in msg['Text'].lower(): 
			flag = 0
			return 'robot is disabled'
		if flag:
			#print u'%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName']
			reply = get_response(msg['Text'])
			#reply = prefix + reply
			#print(reply)
			return (reply)

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
	if msg['FromUserName'] == chatrooms: 
		if msg['isAt']:
			global flag_group
			if 'help' in msg['Text'].lower():
				return u'\
回复 enable 同时@我 开启arex机器人\n\
回复 disable 同时@我 关闭arex机器人'
			if 'enable' in msg['Text'].lower(): 
				flag_group = 1
				return 'robot is enabled'
			if 'disable' in msg['Text'].lower(): 
				flag_group = 0
				return 'robot is disabled'
		if flag_group:
			#print u'%s: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName']
			reply = get_response(msg['Content'])
			#print(reply)
			return (reply)

itchat.auto_login(True)
mySelf = itchat.get_friends()[0]["UserName"]
itchat.run()
