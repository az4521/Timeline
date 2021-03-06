from Timeline.Server.Constants import TIMELINE_LOGGER, PACKET_TYPE, PACKET_DELIMITER, LOGIN_SERVER, WORLD_SERVER, LOGIN_SERVER_ALLOWED
from Timeline.Utils.Events import PacketEventHandler

from twisted.internet import threads
from twisted.internet.defer import Deferred

from collections import deque
import logging

@PacketEventHandler.XTPacketRule('s', 'i#ai', WORLD_SERVER)
def AddItemRule(data):
	param = data[2]

	item = param[0]

	return [[int(item)], {}]

@PacketEventHandler.XTPacketRule('s', 'i#qpp', WORLD_SERVER)
def GetPinsRule(data):
	return [[int(data[2][0])], {}]

@PacketEventHandler.XTPacketRule('s', 'i#qpa', WORLD_SERVER)
def GetAwardsRule(data):
	return [[int(data[2][0])], {}]