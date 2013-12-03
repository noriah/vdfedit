#####################################
# VDFWriter.py                      #
# Author: noriah            #
#                                   #
# For Writing VDF Files             #
#   (Valve Data Format)             #
#                                   #
# Copyright (c) 2013 noriah #
#####################################

import re
from collections import OrderedDict

class VDFWriter:
	def __init__(self, filename, data = None):
		self.file = filename
		if data is None:
			self.data = OrderedDict()
		else:
			self.data = data
		self.olddata = self.data

	def setFile(self, filename):
		self.file = filename

	def setData(self, data):
		self.data = data
		self.olddata = data

	def getData(self):
		return self.data

	def edit(self, path):
		if not isinstance(path, str):
			raise TypeError("Type of param 'path' not type 'string'")
		array = self.data
		if not isinstance(array, OrderedDict):
			array = OrderedDict()
		path = path.split("=", 1)
		value = path[1]
		path = path[0]
		path = re.sub('\[', '', re.sub('\]', '', re.sub('.\[', '"', re.sub('\].', '"', path)))).split('"')
		q = 0
		p = list()
		for x in path:
			q += 1
			if q % 2 != 0:
				p += x.split(".")
			else:
				p.append(x)
		a = wrap(array)
		for c in p[:-1]:
			if not a().has_key(c):
				a()[c] = ""
			if not isinstance(a()[c], OrderedDict):
				a()[c] = OrderedDict()
			a = wrap(a()[c])
		if value == ";;DELETE;;":
			a().pop(p[-1], None)
		else:
			a()[p[-1]] = value
		self.data = array

	def editMany(self, paths):
		if not isinstance(paths, list):
			raise TypeError("Type of param 'paths' not type 'list'")
		[self.edit(p) for p in paths]

	def formatData(self, data = None):
		data = self.data if data is None else data
		def loop(array, tab=''):
			string = ''
			for k, v in array.iteritems():
				string += tab + '"' + k + '"'
				if isinstance(v, OrderedDict):
					string += '\n' + tab + '{\n'
					string += loop(v, tab + '\t')
					string += tab + '}\n'
				else:
					string += '\t\t"' + v + '"\n'
			return string
		return loop(self.data)

	def write(self):
		array = self.data
		if not isinstance(array, OrderedDict):
			if isinstance(array, list):
				try:
					raise VDFWriterError(3)
				except VDFWriterError, e:
					print("Cannot write out List Data: " + str(array))
			else:
				try:
					raise VDFWriterError(2)
				except VDFWriterError, e:
					print("Data to write is not a Dictionary: " + stry(array))


		try:
			filec = open(self.file, 'w')
		except IOError as e:
			print("Could not open '" + self.file + "' for writing.")
			print(e)
		data = self.formatData()
		filec.write(data)
		filec.close()
		self.olddata = self.data

	def undo(self):
		self.data = self.olddata


class VDFWriterError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)



def wrap(obj):
	def __w__():
		return obj
	return __w__
