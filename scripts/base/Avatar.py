# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Avatar(KBEngine.Proxy):
	def __init__(self):
		KBEngine.Proxy.__init__(self)
		DEBUG_MSG("Avatar:base:__init__")

	def onClientEnabled(self):
		DEBUG_MSG("Avatar:onClientEnabled")
		KBEngine.globalData["Room"].enterRoom(self)

	def createCell(self, roomCellCall):
		DEBUG_MSG("Avatar:createCell")
		self.createCellEntity(roomCellCall)

	def sendChat(self, chatContent):
		DEBUG_MSG("Avatar:sendChat chatContent" + str(chatContent))
		KBEngine.globalData["Room"].sendChat(chatContent)

	def recieveChat(self, chatContent):
		DEBUG_MSG("Avatar:recieveChat")
		self.client.recieveChat(chatContent)
