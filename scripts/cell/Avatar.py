# -*- coding: utf-8 -*-
import KBEngine
from KBEDebug import *

class Avatar(KBEngine.Entity):
	def __init__(self):
		KBEngine.Entity.__init__(self)
		DEBUG_MSG("Avatar:cell:__init__")

	def onGetWitness(self):
		DEBUG_MSG("Avatar:onGetWitness")
		self.addProximity(1, 0, 0)

	def onEnterTrap(self, entityEntering, range_xz, range_y, controllerID, userarg):
		DEBUG_MSG("%s::onEnterTrap: %i entityEntering=(%s)%i, range_xz=%s, range_y=%s, controllerID=%i, userarg=%i" % \
						(self.className, self.id, entityEntering.className, entityEntering.id, \
						range_xz, range_y, controllerID, userarg))
		if entityEntering.className == "Food":
			entityEntering.destroy()
			if self.moveSpeed > 0.2:
				self.moveSpeed = self.moveSpeed - 0.1

	def onLeaveTrap(self, entityLeaving, range_xz, range_y, controllerID, userarg):
		pass
