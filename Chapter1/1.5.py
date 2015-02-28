#1.5 Implement a method to perform basic string compression using the counts of repeated characters.
str1 = 'aabcccccaaa'# output 'a2b1c5a3'
def stringcompressed(strings):
	newstr = ''
	count = 1
	last = strings[0]
	for i in strings[1:]:
		if i == last:
			count += 1
		else:
			newstr = newstr + last + str(count)
			last = i
			count = 1
	newstr = newstr + last + str(count)
	if len(strings) > len(newstr):
		return newstr
	else:
		return strings
print(stringcompressed('abcdefg'))
