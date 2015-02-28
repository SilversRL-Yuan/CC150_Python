#1.4: Write a method to replace all spaces in a string with '%20'.
str1 = 'abdf iiqo ijoioi skl'
def replacespace(str1):
	n = 0
	for i in str1:
		if i == ' ':
			n += 1
	newlist = [i for i in range(0,len(str1)+2*n)]
	j = 0
	for i in range(0,len(str1)):
		if str1[i] != ' ':
			newlist[j] = str1[i]
			j = j + 1
		else:
			newlist[j] = '%'
			newlist[j+1] = '2'
			newlist[j+2] = '0'
			j = j + 3
	return ''.join(newlist)
print(replacespace('sauidhu ahsuidhasiu asuhdiuha nasjkn '))
