# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Food(KBEngine.Entity):
	def __init__(self):
		DEBUG_MSG("Food:__init__")
		KBEngine.Entity.__init__(self)
