import sys

def  local_al(s, t, maxdist, matrix):
	
	m = len(s)
	n = len(t)

	maxi = (0,0,0) #pos i, pos j, score
	
	T = []   # create  empty  matrix
	
	
	T.append([0] * (m+1))

	for i in range(1, n+1):
		T.append([None] * (m+1)) # add  empty  row i
		T[i][0] = 0 # init 0th  column  of row i
		

		for j in range(1, m+1):
			T[i][j] = max(0, T[i-1][j-1] + score(t[i-1], s[j-1], matrix), T[i-1][j] -10, T[i][j-1] -10)
			if T[i][j] > maxi[2]:
				maxi = (i, j, T[i][j])
		print T
	
	
	return maxi


def score(c1, c2, matrix):
	return int(matrix[getindex(c1)][getindex(c2)])
	
	
	
	
def readmatrix(f):
	matrix = []
	
	next(f)
	next(f)
	next(f)
	next(f)
	next(f)
	next(f)
	next(f)
	for line in f:
		
		
		if line == "\n":
			break
		
		line = line.replace("  ", " ")	
		line = line[:-1].split(" ")
		matrix.append(line[1:])
		
	return matrix
			
			
	
def getindex(c):
	l = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V", "B", "Z", "X"] 
	return l.index(c)
	
	
	
#main
with open(str(sys.argv[3])) as f:
	matrix = readmatrix(f)
	
print local_al(sys.argv[1], sys.argv[2], 1000, matrix)
