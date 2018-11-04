# Standard imports
import json
from hashlib import sha256

class Chain():
	'''
	Chain: A (linked-list) blockchain.
		*blocks (array) an array of all past blocks.
		*difficulty (dict/JSON) representing the info the block stores (transactions here).
		*prev_hash (str) the SHA256 hash of the last block in the chain.
		*current_difficulty (int) x-number of zeros that must start the block hash.
		*hash (hex str) the current block's SHA256 hash (of all block attributes).

	This blockchain uses SHA256 hash and a POW variant.
	Similar to bitcoin, it stores transactions in it's ledger.
	'''

	def __init__(self, genesis_block, starting_difficulty, blocks=None):
		if blocks == None:
			self.blocks = [genesis_block]
		self.difficulty = starting_difficulty

	def __str__(self):
		return ("""
Current Difficulty: {0}
Blocks: {1}
		""").format(self.difficulty, [str(block) for block in self.blocks])
