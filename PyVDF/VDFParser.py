#####################################
# VDFWriter.py                      #
# Author: noriah            #
#                                   #
# For Reading VDF Files             #
#   (Valve Data Format)             #
#                                   #
# Copyright (c) 2013 noriah #
#####################################


import re
from collections import OrderedDict

class VDFParser:
	def __init__(self, filename):
		
		self.data = OrderedDict()
		
		try:
			with open(filename) as filec:
				fdata = filec.read()
				filec.close()
				self.error = False
		except IOError as e:
			print("Could not open '" + filename + "' for reading.")
			print("This is Okay if we are making a new file (say, with VDFWriter).")
			self.error = True
			return

		self.fdata = list(re.sub('!//.*!', '', fdata))
		self.fdata.append(None)
		self.__parse__()

	def __parse__(self):

		if self.error:
			return None

		data = OrderedDict() 
		array = wrap(data)
		key = ''
		string = ''
		path = ''
		grabKey = True
		quoted = False
		reading = False
		lastchar = ''
		lastlastchar = ''
		curchar = ''
		whitespace = ("\t", " ", "\n", "\r")
		quote = "\""
		escape = "\\"
		openbrace = "{"
		closebrace = "}"

		def formatPath(string, splitter):
			string = string.split(splitter)
			for i, s in enumerate(string):
				if re.search("\.", s) != None:
					string[i] = "[" + s + "]"
			return ".".join(string)

		def update():
			if grabKey:
				#key, string, grabKey
				return [string, '', False]
			else:
				if array().has_key(key):
					try:
						raise VDFParserError(5)
					except VDFParserError, e:
						print("[" + e + "]Key Already Exists: " + formatPath(path + "+" + key, "+"))
				array()[key] = string
				return ['', '', True]

		def newLevel():
			if grabKey:
				try:
					raise VDFParserError(2)
				except VDFParserError, e:
					print("[" + e + "]Something went wrong near here: " + formatPath(path, "+"))

			if array().has_key(key):
				try:
					raise VDFParserError(5)
				except VDFParserError, e:
					print("[" + e + "]Key Already Exists: " + formatPath(path + "+" + key, "+"))
			array()[key] = OrderedDict()
			a = wrap(array()[key])
			p = path
			if p == '':
				p += key
			else:
				p += '+' + key

			return [a, '', p, True]

		def oldLevel():
			if not grabKey:
				try:
					raise VDFParserError(2)
				except VDFParserError, e:
					print("[" + e + "]Something went wrong near here: " + formatPath(path, "+"))
			a = wrap(data)
			full_path = path.split('+')
			new_path = ''
			if full_path:
				for x in full_path[:-1]:
					if new_path == '':
						new_path += x
					else:
						new_path += '+' + x
					a = wrap(a()[x])

			return [a, new_path, True]
		
		
		for curchar in self.fdata:
			if not reading and curchar in whitespace:
				continue
			
			if curchar is None:
				if reading:
					if not quoted:
						if not (lastchar == quote and lastlastchar != escape):
							if string:
								if grabKey:
									try:
										raise VDFParserError(4)
									except VDFParserError, e:
										print("Invalid Data at End of File: " + string)
								else:
									update()
				else:
					if key != '':
						try:
							raise VDFParserError(4)
						except VDFParserError, e:
							print("Invalid Data at End of File: " + key)
				break

			if curchar == quote and lastchar != escape:
				if reading:
					reading = False
					quoted = False
					key, string, grabKey = update()
				else:
					reading = True
					quoted = True

			elif curchar in whitespace:
				if reading:
					if not quoted:
						reading = False
						key, string, grabKey = update()
					else:
						string += curchar
			
			elif curchar == openbrace:
				if reading:
					if not quoted:
						reading = False
						key, string, grabKey = update()
						array, key, path, grabKey = newLevel()
					else:
						string += curchar
				else:
					array, key, path, grabKey = newLevel()
					

			elif curchar == closebrace:
				if reading:
					if not quoted:
						reading = False
						key, string, grabKey = update()
						array, path, grabKey = oldLevel()
					else:
						string += curchar
				else:
					array, path, grabKey = oldLevel()
			else:
				string += curchar
				reading = True
			
			lastlastchar = lastchar
			lastchar = curchar
		self.data = data
	
	def setFile(self, filename):
		self.__init__(filename)

	def getData(self):
		return self.data

	def find(self, path):
		if not isinstance(path, str):
			raise TypeError("Type of param 'path' not 'string'")
		path = re.sub('\[', '"', re.sub('\]', '"', re.sub('.\[', '"', re.sub('\].', '"', path)))).split('"')
		q = 0
		p = list()
		for x in path:
			q += 1
			if q % 2 != 0:
				p += x.split(".")
			else:
				p.append(x)
		array = self.data
		for c in p:
			if array.has_key(c):
				array = array[c]
			else:
				return ''
		return array

	def findMany(self, paths):
		if not isinstance(paths, list):
			raise TypeError("Type of param 'paths' not type 'list'")
		return [self.find(p) for p in paths]


class VDFParserError(Exception):
	def __init__(self, value):
		self.value = value
	def __str__(self):
		return repr(self.value)

def wrap(obj):
	def __w__():
		return obj
	return __w__
