#coding=utf8
import itchat
#from tuling import get_response
from xiaoirobot import get_response

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
input disable friend or chatroom to close the robot\n\
input arex to visit my blog')
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
			#reply = get_response(msg['Text'])
			#print(reply)
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
	if msg['FromUserName'] == friends:
		if 'help' in msg['Text'].lower():
			return u'\
回复 enable 开启arex机器人\n\
回复 disable 关闭arex机器人\n\
回复 arex 浏览我的博客'
		if 'enable' in msg['Text'].lower(): 
			flag = 1
			return 'robot is enabled'
		if 'disable' in msg['Text'].lower(): 
			flag = 0
			return 'robot is disabled'
		if 'arex' in msg['Text'].lower(): 
			return 'http://arexchu.github.io'
		#elif 'picture' in msg['Text'].lower():
		#	itchat.send('@img@Himalayas.jpg', msg['FromUserName']) # there should be a picture
		if flag:
			print u'%s: %s' % (msg['Type'], msg['Text']), msg['FromUserName']
			reply = get_response(msg['Text'].encode("utf-8"))
			#reply = prefix + reply
			print(reply)
			return (reply.decode("utf-8"))

@itchat.msg_register('Text', isGroupChat = True)
def group_reply(msg):
	if msg['FromUserName'] == chatrooms: 
		if msg['isAt']:
			global flag_group
			if 'help' in msg['Text'].lower():
				return u'\
回复 enable 同时@我 开启arex机器人\n\
回复 disable 同时@我 关闭arex机器人\n\
回复 arex 同时@我浏览我的博客'
			if 'enable' in msg['Text'].lower(): 
				flag_group = 1
				return 'robot is enabled'
			if 'disable' in msg['Text'].lower(): 
				flag_group = 0
				return 'robot is disabled'
			if 'arex' in msg['Text'].lower(): 
				return 'http://arexchu.github.io'
		if flag_group:
			print u'%s: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName']
			reply = get_response(msg['Content'].encode("utf-8"))
			print(reply)
			return (reply.decode("utf-8"))

itchat.auto_login(True)
mySelf = itchat.get_friends()[0]["UserName"]
#print(mySelf)
itchat.get_friends(update=True)
myFriends = itchat.search_friends(name=myUserName)[0]["UserName"]
#print(myFriends)
itchat.run()
