# Input 
n = int(input('Enter no of unknowns: '))

# Enter the argumented matrix
a = [[0 for i in range(n+1)] for j in range(n)]
print('Enter the argumented matrix: ')

for i in range(n): 
  for j in range(n+1):
    a[i][j] = float(input('Enter a[%d][%d] element: ' % (i, j)))
    
    
# print(a)

### Implementation

## Upper Traingular Matrix
for i in range(n):
  if(a[i][i] == 0): 
    print('Divide by zero problem! Terminating the program.')
    exit 
  
  # for the rows after i, find the needed ratio for each row after i
  for j in range(i+1, n):
    ratio = a[j][i] / a[i][i]
    
    # for the perticular row after i, change every element(col) to make below a[i][i] element 0
    for k in range (n+1):
      a[j][k] -= ratio*(a[i][k])
      

## Back substitution 
res = [0 for i in range(n)] ## Make a array to store result

## last result 
res[n-1] = a[n-1][n] / a[n-1][n-1]

## others value, iterate from the last
for i in range(n-2, -1, -1):
  # find the constant value
  res[i] = a[i][n]
  
  # substract all the founded value like: 
  # 3*x1 - 2*x2 + 3*x3 = 3
  # 3*x1 = 3(const) + 2*x2(founded) - 3*x3(founded) 
  for j in range(i+1, n):
    res[i] -= a[i][j]*res[j]
    
  # x1 = (3(const) + 2*x2(founded) - 3*x3(founded)) / 3
  res[i] /= a[i][i]
  
  
# solution
print('\nSolution is: ')
for i in range(n):
    print('X%d = %0.6f\n' %(i,res[i]))