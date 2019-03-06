# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Room(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		DEBUG_MSG("Room:base:__init__")
		self.createCellEntityInNewSpace(None)
		KBEngine.globalData["Room"] = self

	def enterRoom(self, avatarBaseCall):
		DEBUG_MSG("Room:enterRoom")
		avatarBaseCall.createCell(self.cell)
