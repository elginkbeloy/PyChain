# PyChain

PyChain is a basic blockchain implementation done solely in Python. 

*Note: PyChain should not be used for any real-world applications, and is created only for demonstration of concepts. 

## Usage

Create a new PyChain blockchain.

```python
# Standard imports
from hashlib import sha256

# PyChain local imports
from block import Block
from chain import Chain

# Info for the first block in the chain.
GENESIS_PREV_HASH = sha256('Example text for first hash.'.encode('utf-8')).hexdigest()
GENESIS_TX = {'to': 'NoName', 'from': '0000', 'amount': 1000000}
GENESIS_DIFFICULTY = 8

# Create a genesis block to start your chain.
GENESIS_BLOCK = Block(0, GENESIS_TX, GENESIS_PREV_HASH, GENESIS_DIFFICULTY)

# Mine the GENESIS_BLOCK hash.
GENESIS_BLOCK.mine_valid_block_hash()

# Take a look at your first block.
print(GENESIS_BLOCK)

# Create a PyChain blockchain to store your created block.
pychain_chain = Chain(GENESIS_BLOCK, GENESIS_DIFFICULTY)

# Take a look at that too.
print(pychain_chain)


```

## Contributing
There are a lot of TODOs here. Pull requests are welcome, and I will love you for it! ;)

## Coming Soon / TODOs
1) Structure and class for ledger.
2) Methods for creating new blocks within Chain class.
3) Method for validation of chain.
4) Method for validation of ledger.
5) PK Crypto for TX validation. +User creation, etc.
6) Interaction between peers.

