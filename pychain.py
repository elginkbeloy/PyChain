from hashlib import sha256

class Block():
	'''
	Block: A basic blockchain block.
		*id (int) representing block number, indexing at zero.
		*ledger (dict/JSON) representing the info the block stores (transactions here).
		*prev_hash (str) the SHA256 hash of the last block in the chain.
		*current_difficulty (int) x-number of zeros that must start the block hash.
		*hash (hex str) the current block's SHA256 hash (of all block attributes).

	This blockchain uses SHA256 hash and a POW variant.
	Similar to bitcoin, it stores transactions in it's ledger.
	'''

	def __init__(id, ledger, prev_hash, current_difficulty, nonce=0):
		self.id = id
		self.ledger = ledger
		self.prev_hash = prev_hash
		self.nonce = nonce
		self.hash = self.get_block_hash(current_difficulty)

	# Get a block SHA256 hash based on all block attributes that starts
	# with current_difficulty(int) number of zeros.
	def get_block_hash(difficulty):
		# Increment nonce while sha256 hash does not start with
		# difficulty(int) number of zeros.
		while not self.get_hash().startswith('0' * current_difficulty)
			self.nonce += 1

			# Get SHA256 hash based on all block attributes.
			block_str = str(self.id + json.dumps(self.ledger) + self.prev_hash + self.nonce)
			hash_hex_str = sha256(block_str.encode('utf-8')).hexdigest()

		hash_hex_str




blocks = []
