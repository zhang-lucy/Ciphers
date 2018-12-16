"""Ciphers based on Marvin Gardner's book Codes, Ciphers, and Secret Writing.
"""
import string
import random

class Cipher:
	def __init__(self,encoded="",decoded="",key=None,):
		self.encoded=encoded.upper()
		self.decoded=decoded.upper()
		self.key=key

	def tokenize(self,text):
		"""Given a string of text, returns a list of each word, spaces removed."""
		x=0
		ret=[]
		smol=""
		while x<len(text):
			if text[x]!=" ":
				smol=smol+text[x]
			else:
				if len(smol)>0:
					ret.append(smol)
				smol=""
			x+=1
		if len(smol)>0:
			ret.append(smol)
		return ret

	def flatten(self,text):
		ret=''
		for t in text:
			if t!=" ":
				ret=ret+t
		return ret

	def random_letters(self,n):
		"""Generates a string of n random letters"""
		ret=""
		for x in range(n):
			ret=ret+random.choice(string.ascii_uppercase)
		return ret

	def decode(self):
		return

# c=Cipher('','MEeT mE TONiGhT')
# print(c.flatten(c.decoded))
# print(c.random_letters(4))


class Railfence(Cipher):
	"""Uses 4-letter breaks"""
	def __init__(self,encoded="",decoded="",key=None,chunk_size=4):
		Cipher.__init__(self,encoded,decoded,key)
		self.chunk_size=chunk_size

	def encode(self):
		#add missing random letters for a multiple of 4
		extra=len(self.decoded)%self.chunk_size
		self.decoded=self.flatten(self.decoded+self.random_letters(extra))

		ret=""
		for x in range(0,len(self.decoded),2):
			ret=ret+self.decoded[x]
		for x in range(1,len(self.decoded),2):
			ret=ret+self.decoded[x]

		temp=""
		x=1
		for let in ret: #add spaces
			temp=temp+let
			if x==self.chunk_size:
				temp=temp+" "
				x=1
			else:
				x+=1

		self.encoded=temp
		return self.encoded

	def decode(self):
		self.encoded=self.flatten(self.encoded)
		ret=""
		for x in range(len(self.encoded)//2):
			ret=ret+self.encoded[x]+self.encoded[x+len(self.encoded)//2]
		self.decoded=ret
		return ret

r=Railfence('aalu hnhs edfy mnag igih aofz','')
# print(r.encode())
print(r.decode())



class RSA(Cipher):
	def __init__(self,encoded,decoded,key):
		pass