# Standard imports
from hashlib import sha256

# PyChain local imports
from block import Block
from chain import Chain

# Create genesis block to start chain. Include first tx.
GENESIS_PREV_HASH = sha256('Long live PyChain!'.encode('utf-8')).hexdigest()
GENESIS_TX = {'to': 'elgin', 'from': '0000', 'amount': 100000}
GENESIS_DIFFICULTY = 3
GENESIS_BLOCK = Block(0, GENESIS_TX, GENESIS_PREV_HASH, GENESIS_DIFFICULTY)

# Mine GENESIS_BLOCK hash.
GENESIS_BLOCK.mine_valid_block_hash()
print(GENESIS_BLOCK)

pychain_chain = Chain(GENESIS_BLOCK, GENESIS_DIFFICULTY)
print(pychain_chain)
