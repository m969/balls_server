# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *
import GameUtils

class Room(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		DEBUG_MSG("Room:cell:__init__")
		for i in range(20):
			pos = GameUtils.randomPosition3D()
			KBEngine.createEntity("Food", self.spaceID, pos, (0.0,0.0,0.0), {})
			DEBUG_MSG("food pos=" + str(pos))
