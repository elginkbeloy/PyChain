# Library Imports
import ecdsa

# Standard imports
from hashlib import sha256
from time import time
from binascii import hexlify

class User():
	'''
	User: A user who can make transactions with other users and mine blocks.
		*username (str) a name associated with the address/public_key.
		*balance (int) the current balance of a user.
		*private_key (ecdsa SECP256k1 sk) the private key for signing transactions.
		*public_key (ecdsa SECP256k1 pk) the public key for verification of signing.
		Also used as an address.
	'''
	def __init__(self, username):
		self.username = username
		self.balance = 0
		self.private_key = ecdsa.SigningKey.generate(curve=ecdsa.SECP256k1)
		self.public_key = self.private_key.get_verifying_key()
		self.address = hexlify(self.public_key.to_string())
		# NOTE: One could also pay to a public_address hash P2KH, but why?
		#self.address = sha128(public_key.encode("utf-8")).hexdigest()

	def __str__(self):
		return """
Username: {0}
User Address: {1}
User Balance: {2}
		""".format(self.username, self.address, self.balance)

	def sign_str(self, str_to_sign):
		# SECP256k1 is the elliptic curve used in Bitcoin.
		signature = self.private_key.sign(str_to_sign)
		assert self.public_key.verify(signature, str_to_sign) # True

		return signature
