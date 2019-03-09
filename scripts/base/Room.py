# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Room(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		DEBUG_MSG("Room:base:__init__")
		self.createCellEntityInNewSpace(None)
		KBEngine.globalData["Room"] = self
		self.avatars = []

	def enterRoom(self, avatarBaseCall):
		DEBUG_MSG("Room:enterRoom")
		avatarBaseCall.createCell(self.cell)
		self.avatars.append(avatarBaseCall)
		DEBUG_MSG("self.avatars=" + str(self.avatars))

	def sendChat(self, chatContent):
		DEBUG_MSG("Room:sendChat chatContent=" + str(chatContent))
		for avatar in self.avatars:
			avatar.recieveChat(chatContent)
