# Standard imports
import json
from hashlib import sha256
from time import time

class Block():
	'''
	Block: A basic blockchain block.
		*id (int) representing block number, indexing at zero.
		*ledger (dict/JSON) representing the info the block stores (transactions here).
		*prev_hash (str) the SHA256 hash of the last block in the chain.
		*time (UNIX Timestamp / str) unix timestamp from block creation date/time.
		*difficulty (int) x-number of zeros that must start the block hash.
		*hash (hex str) the current block's SHA256 hash (of all block attributes).

	This blockchain uses SHA256 hash and a POW variant.
	Similar to bitcoin, it stores transactions in its ledger.
	'''

	def __init__(self, id, ledger, prev_hash, time, difficulty, nonce=0):
		self.id = id
		self.ledger = ledger
		self.prev_hash = prev_hash
		self.time = time
		self.difficulty = difficulty
		self.nonce = nonce
		self.hash = None

	# A string representation of a block.
	def __str__(self):
		return ("""
ID: {0}
Ledger: {1}
Previous Hash: {2}
Creation Date: {3}
Difficulty: {4}
Nonce: {5}
Hash: {6}
			""").format(self.id, self.ledger, self.prev_hash, self.time,
			self.difficulty, self.nonce, self.hash)

	# Get a block SHA256 hash based on all hashable block attributes that starts
	# with current_difficulty(int) number of zeros.
	def mine_valid_block_hash(self):
		# SHA256 of all hashable block attributes.
		block_str = str(self.id) + json.dumps(self.ledger) + self.prev_hash + str(self.time)
		valid_hash = sha256((block_str + str(self.nonce)).encode('utf-8')).hexdigest()

		# Increment nonce while sha256 hash does not start with
		# difficulty(int) number of zeros.
		while not valid_hash.startswith('0' * self.difficulty):
			self.nonce += 1
			valid_hash = sha256((block_str + str(self.nonce)).encode('utf-8')).hexdigest()

		self.hash = valid_hash
