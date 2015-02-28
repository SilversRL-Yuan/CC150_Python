#1.3 Write a method to tell if two strings are permutation or not
str1 = 'abcdefghijklmnopqrstuvwxyz'
str2 = 'qiwjdoaisndano'
def ispermutation(str1,str2):
	if len(str1) == len(str2):
		list1 = [i for i in str1]
		list2 = [i for i in str2]
		list1.sort()
		list2.sort()
		return ''.join(list1) == ''.join(list2)
	else:
		return False
print(ispermutation('abcd','cda'))
