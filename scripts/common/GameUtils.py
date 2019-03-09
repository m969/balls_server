# -*- coding: utf-8 -*-

"""
"""
import Math
import math
import KBEngine
import random


def randomPosition3D():
	return Math.Vector3(random.randint(-20, 20) + random.random(), 0.0, random.randint(-20, 20) + random.random())
