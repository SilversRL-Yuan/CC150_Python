#1.7 Write an algorithm such that if an element in an M*N matrix is 0, its entire row and column are set to 0.
def setzero(matrix):
	#row,column
	row = [False for i in range(len(matrix))]
	column = [False for j in range(len(matrix[0]))]
	#find 0 positions
	for i in range(0,len(matrix)):
		for j in range(0,len(matrix[0])):
			if matrix[i][j] == 0:
				row[i] = True
				column[j] = True
	#set row and column 0
	for i in range(0,len(matrix)):
		for j in range(0,len(matrix[0])):
			if row[i] == True or column[j] == True:
				matrix[i][j] = 0
	return matrix
l = [[1,2,3],
[4,5,6],
[7,8,9]]
print(setzero(l))
