import pdb

def getHint(self, secret, guess):
	secret = str(1999)
	guess = str(8888)
	for i in len(guess):
        	#if i is None: continue
	if secret[i] == guess[i]:
		print ("a")
	else:
		print ("b")

