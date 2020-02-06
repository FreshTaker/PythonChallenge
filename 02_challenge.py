# Problem 2: Decode
rawString = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

print(ord('a'))
print(ord('z'))

print(chr(ord('z')+4))

def moveForwardTwo(letter):
	if letter == 'y':
		return 'a'
	elif letter == 'z':
		return 'b'
	elif letter == '.':
		return letter
	elif letter == "'":
		return letter
	elif letter == '(':
		return letter
	elif letter == ')':
		return letter
	elif letter == ' ':
		return letter
	else:
		result = chr(ord(letter)+2)
		return result

newString = ""

for i in rawString:
	print(i)
	print(moveForwardTwo(i))
	newString = newString + moveForwardTwo(i)

print(newString)

# Answer:
# i hope you didnt translate it by hand. thats what computers are for. 
# doing it in by hand is inefficient and that's why this text is so long. 
# using string.maketrans() is recommended. now apply on the url.

## The better way to do it is by using str.maketrans(intab, outtab)
URL = 'map'

rawData = "abcdefghijklmnopqrstuvwxyz"
outData = "cdefghijklmnopqrstuvwxyzab"

transtab = URL.maketrans(rawData,outData)

print(URL.translate(transtab))


#ocr
