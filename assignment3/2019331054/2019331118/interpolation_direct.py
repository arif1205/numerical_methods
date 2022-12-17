## Direct

# linear, quadric, cubic
# no of unknowns 
n = int(input('No of unknowns: '))

# n = 2

argarr = [[0 for i in range(n+1)] for j in range(n)]
# argarr = [[1, 10, 100, 227.04],[1, 15, 225, 362.78], [1,20,400,517.35]]
# argarr = [[1, 15, 362.78], [1, 20, 517.35]]

for i in range(n):
  print('Enter unkowns for equation%d: ' % (i+1))
  d = float(input('x value for equation%d: ' % (i+1)))
  for j in range(n):
    argarr[i][j] = (d**j)
  
  y = float(input('Y value for equation%d: ' % (i+1)))
  argarr[i][n] = y

#upper traingular 
for i in range(n):
  if(argarr[i][i] == 0): 
    print('Divide by zero problem! Terminating the program.')
    exit 
  
  # for the rows after i, find the needed ratio for each row after i
  for j in range(i+1, n):
    ratio = argarr[j][i] / argarr[i][i]
    
    # for the perticular row after i, change every element(col) to make below a[i][i] element 0
    for k in range (n+1):
      argarr[j][k] -= ratio*(argarr[i][k])


#back substitution
res = [0 for i in range(n)]

res[n-1] = argarr[n-1][n] / argarr[n-1][n-1]

for i in range(n-2, -1, -1):
  res[i] = argarr[i][n]
  
  for j in range(i+1, n):
    res[i] -= argarr[i][j]*res[j]
  
  res[i] /= argarr[i][i]
  


x = float(input('Enter the value: '))
sum = 0
for i in range(n):
  sum += res[i]*(x**i)
  
  
print("Ans", sum)