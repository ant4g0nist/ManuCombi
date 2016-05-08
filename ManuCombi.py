#!/usr/bin/env python

# /*
#  * ----------------------------------------------------------------------------
#  * "THE BEER-WARE LICENSE" (Revision 42):
#  * <ichaithu@gmail.com> wrote this file.  As long as you retain this notice you
#  * can do whatever you want with this stuff. If we meet some day, and you think
#  * this stuff is worth it, you can buy me a beer in return.   @ant4g0nist
#  * ----------------------------------------------------------------------------
#  */

###############
### ManuCombi
### - @ant4g0nist
###############

__author__  = 'ant4g0nist'
__version__ = 'ichi'

import os
import time
import random
import commands
import itertools as ite
from copy import deepcopy

class ManuCombi:
	def __init__(self, target_fname, round_=None):
		self.target_fname = target_fname
		self.raw_bytes = self._read_file_as_rawBytes()
		self.length = len(self.raw_bytes)
		self.total = list(xrange(self.length)) # this'll be used to calculate combinations of positions
		self.count = 4
		if round_:
			self.round = round_
		else:
			self.round=1
		self._round() #calculate first round of combinations

	def _read_file_as_rawBytes(self):
		"""
		Reads file as byte array
		"""

		f=open(self.target_fname,'r').read()
		return bytearray(f)

	def _round(self):
		"""
		Calculates r(round) length subsequences of elements from the input iterable.
		"""
		print '[+]\tGoing through round '+str(self.round)
		self.combinations = ite.combinations(self.total,r=self.round)


	def _next(self):
		"""return next combination"""
		combi = self.combinations.next()
		return combi

	def _permute(self):
		"""
			permutes
		"""
		bytes = self._fuzz_file_bytes()
		return str(bytes)

	def _fuzz_file_bytes(self):

		if self.count==4:
			try:
				self.fuzz_byte = self._next()
			except Exception as e:
				self.round+=1
				self._round()
				self.fuzz_byte = self._next()

			self.count=0
		
		cou=0
		while  cou<len(self.fuzz_byte):
			for i in xrange(3):
				self.count = i
				val = self.fuzz_byte[cou]
				
				if self.count==0:
					self.new_file = self._fuzz_with_max_value(val)
					self.count+=1

				elif self.count==1:
					self.new_file = self._fuzz_with_min_value(val)
					self.count+=1

				elif self.count==2:
					self.new_file = self._fuzz_with_random_value(val)
					self.count=0
			cou+=1
			self.count==4
		return self.new_file

	def _fuzz_with_max_value(self,val):
		self.new_file = deepcopy(self.raw_bytes)
		var=ord('ff'.decode('hex'))
		self.new_file[val]=var

		return self.new_file

	def _fuzz_with_min_value(self,val):
		self.new_file = deepcopy(self.raw_bytes)
		var=ord('00'.decode('hex'))
		self.new_file[val]=var

		return self.new_file

	def _fuzz_with_random_value(self,val):
		self.new_file = deepcopy(self.raw_bytes)
		rbyte = random.randrange(256)
		self.new_file[val]=rbyte

		return self.new_file
