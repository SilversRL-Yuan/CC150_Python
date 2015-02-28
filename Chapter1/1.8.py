#1.8Assume you have a method isSubString which checks if one word is a substring of another.
#Given two strings, s1 and s2, write code to check if 
#s2 is a rotation of s1 using only one call to isSubString (i.e. "waterbottle" is a rotation of "erbottlewat")
s1 = 'waterbottle'
s2 = 'erbottlewat'
def isSubString(str,substr):
	if substr in str:
		return True
	return False
print(isSubString('abcdefghijkl','abcdefghijklm'))
def isRotation(str1,str2):
	if len(str1) != len(str2):
		return False
	newstr = str1 + str1
	return isSubString(newstr,str2)
print(isRotation('waterbottle','erbottlewat'))
