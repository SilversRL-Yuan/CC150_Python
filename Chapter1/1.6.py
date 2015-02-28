#1.6 N*N matrix rotate by 90 degrees
#Not in place
def rotate_90degree(matrix1):
	N = len(matrix1)
	newmax = [[0 for j in range(0,N)] for i in range(0,N)]
	for i in range(0,N):
		for j in range(0,N):
			newmax[j][N-i-1] = matrix1[i][j]
	return newmax
l = [[1,2,3],
[4,5,6],
[7,8,9]]
print(rotate_90degree(l))

#In place
def newrotate_90(matrix1):
	matrix1 = matrix1[::-1]
	N = len(matrix1)
	for i in range(0,N):
		for j in range(i,N):
			matrix1[i][j],matrix1[j][i] = matrix1[j][i], matrix1[i][j]
	return matrix1
print(newrotate_90(l))
