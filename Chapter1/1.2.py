#1.2 Write code to reverse a C-Style String. 
#(C-String means that “abcd” is represented as five characters, including the null character.)
str1 = 'abcde '
#print(str1[::-1])
def reversestr(strings):
	lists = [i for i in strings]
	for i in range(len(lists)//2):
		lists[i],lists[-i-1] = lists[-i-1],lists[i]
	return ''.join(lists)
print(reversestr(str1))
