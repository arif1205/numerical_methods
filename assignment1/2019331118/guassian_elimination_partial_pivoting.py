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

## exchange row func 
def exchange_row(r1, r2): 
  temp = [0 for i in range(n+1)]
  
  #copy all the element of row a to temp.
  # We can't copy like temp = a[r1], as array is reference type
  for i in range(n+1):
    temp[i] = a[r1][i]
    a[r1][i] = a[r2][i]
    
  for i in range(n+1):
     a[r2][i] = temp[i]
     


## Upper Traingular Matrix
for i in range(n):
  # check the partial pivoting 
  index = i 
  for p in range(i+1, n):
    if(a[index][i] < a[p][i]): 
      index = p 
  
  if(index != i): 
    exchange_row(i, index)
  
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