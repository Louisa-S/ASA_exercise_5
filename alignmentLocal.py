import sys

# Define single-letter acid code
acidcode = ["A", "R", "N", "D", "C", "Q", "E", "G", "H", "I", "L", "K", "M", "F", "P", "S", "T", "W", "Y", "V", "B", "Z", "X"]
# Define indel cost
indelcost = -10

# Core algorithm running a O(n^2), dynamic programming approach to find all alignments
def  local_al(T, s, t, matrix):
	
	# Define n x m
	m = len(s)
	n = len(t)

	maxi = (0,0,0) #pos i, pos j, score
	
	# create  empty  matrix
	T.append([(0, "l")] * (m+1))

	for i in range(1, n+1):
		T.append([(None, None)] * (m+1)) # add  empty  row i
		T[i][0] = (0, "u") # init 0th  column  of row i

		for j in range(1, m+1):
			
			# fill in next cell of matrix
			sco = score(t[i-1], s[j-1], matrix)
			maximum = max(0, T[i-1][j-1][0] + sco, T[i-1][j][0] + indelcost, T[i][j-1][0] +indelcost)
			ind = [0, T[i-1][j-1][0] + sco, T[i-1][j][0] +indelcost, T[i][j-1][0] +indelcost].index(maximum)
			T[i][j] = (maximum, getdirection(ind))
			
			# found another maximum? save it
			if T[i][j][0] > maxi[2]:
				maxi = (i, j, T[i][j][0])
				
	return maxi

# Read score from BLOSUM matrix by character index.
def score(c1, c2, matrix):
	return int(matrix[getindex(c1)][getindex(c2)])

# Map positions to directions in the n x m matrix
def getdirection(pos):
	if pos == 1:
		return "d"
	elif pos == 2:
		return "u"
	elif pos == 3:
		return "l"
	else: return "undef"
	
# Reads in the scoring matrix	
def readmatrix(f):
	matrix = []
	
	for line in f:
		
		if line[0] == "#" or line[0] == ' ':
			continue
		
		if line == "\n":
			break
		
		line = line.replace("  ", " ")	
		line = line[:-1].split(" ")
		matrix.append(line[1:])
		
	return matrix
			
# Returns the index of a single-letter aminoacid code in the score matrix
def getindex(c):
	return acidcode.index(c)
	
# Extracts the final alignment for the best score and returns both aligned strings T1 and T2
def getstring(T, s, t, maxi):
	i = maxi[0]
	j = maxi[1]
	
	start = T[i][j]
	ress = ""
	rest = ""
	
	while(start[0] != 0):
		
		if start[1] == "d":
			i -= 1
			j -= 1
			ress += s[j]
			rest += t[i]
		elif start[1] == "u":
			i -= 1
			ress += "-"
			rest += t[i]
		else:
			j -= 1
			ress += s[j]
			rest += "-"
					
		start = T[i][j]
		
		 
	return ress[::-1], rest[::-1]

	
#####
# MAIN:
# ARGUMENTS:
# 1. String of Text T1
# 2. String of Text T2
# 3. Path to BLOSUM matrix. e.g. ~/Documents/BLOSUM.txt
#
# Program description:
# - OPEN SCORE MATRIX AND RUN LOCAL ALIGNMENT
# - GET ALIGNED STRINGS AND BEST SCORE AND PRINT IT
#####
with open(str(sys.argv[3])) as f:
	matrix = readmatrix(f)

T = []	
s = sys.argv[1]
t = sys.argv[2]
maxi = local_al(T,s , t, matrix)
print maxi [2]

strings = getstring(T,s, t ,maxi)
print strings[0]
print strings[1]
