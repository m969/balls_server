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
