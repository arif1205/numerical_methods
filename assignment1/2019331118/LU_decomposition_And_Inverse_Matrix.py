# Input 
n = int(input('Order of matrix: '))

# Enter the matrix
a = [[0 for i in range(n)] for j in range(n)]
print('Enter the matrix: ')

for i in range(n): 
  for j in range(n):
    a[i][j] = float(input('Enter a[%d][%d] element: ' % (i, j)))


## print matrix 
def print_matrix(mat):
  for i in range(n):
    for j in range(n):
      print('%0.3f' % mat[i][j], end = '\t')
    print('\n')

## LU Decomposition matrix
def lu_decomposition(n, l, u): 
  # copy the  a to u
  for r in range(n):
    for c in range(n):
      u[r][c] = a[r][c]
  
  
  for i in range(n):
    if(u[i][i] == 0): 
      print('Divide by zero problem! Terminating the program.')
      exit 
    
    for r in range(n): 
      if(i == r):
        l[r][r] = 1
      elif(r>i):
        l[r][i] = u[r][i] / u[i][i]
      else: 
        l[r][i] = 0
    
    # for the rows after i, find the needed ratio for each row after i
    for j in range(i+1, n):
      ratio = u[j][i] / u[i][i]
      
      # for the perticular row after i, change every element(col) to make below a[i][i] element 0
      for k in range (n):
        u[j][k] -= ratio*(u[i][k])
  
  # print matrix
  print('Lower Traingular matrix')
  print_matrix(l)
  print('Upper Traingular matrix')
  print_matrix(u)
  
  
#Inverse matrix with LU
def inverse_matrix(n, l, u):
  # Inverse matrix B
  b = [[0 for i in range(n)] for j in range(n)]
  
  ## need n steps for n columns
  for col in range(n):
    c = [0 for i in range(n)]
    c[col] = 1
    ## find z
    z = [0 for i in range(n)]
    z[0] = c[0]
    
    for i in range(1, n):
      # find the constant value
      z[i] = c[i]
      
      # substract all the founded value like: 
      # 3*x1 - 2*x2 + 3*x3 = 3
      # 3*x1 = 3(const) + 2*x2(founded) - 3*x3(founded) 
      for j in range(i):
        z[i] -= l[i][j]*z[j]
        
      # x1 = (3(const) + 2*x2(founded) - 3*x3(founded)) / 3
      z[i] /= l[i][i]
    
    ## find the column of inverse matrix
    column = [0 for i in range(n)] ## Make a array to store result

    ## last result 
    column[n-1] = z[n-1] / u[n-1][n-1]

    ## others value, iterate from the last
    for i in range(n-2, -1, -1):
      # find the constant value
      column[i] = z[i]
      
      # substract all the founded value like: 
      # 3*x1 - 2*x2 + 3*x3 = 3
      # 3*x1 = 3(const) + 2*x2(founded) - 3*x3(founded) 
      for j in range(i+1, n):
        column[i] -= u[i][j]*column[j]
        
      # x1 = (3(const) + 2*x2(founded) - 3*x3(founded)) / 3
      column[i] /= u[i][i]
      
    for i in range(n):
      b[i][col] = column[i]
      
  print("Inverted matrix: ")
  print_matrix(b)
  
  
  
## take container for l and u
l = [[0 for i in range(n)] for j in range(n)]
u = [[0 for i in range(n)] for j in range(n)]

lu_decomposition(n, l, u)
inverse_matrix(n, l, u)