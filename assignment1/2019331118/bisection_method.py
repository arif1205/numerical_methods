# Define absolute error calculation
def abserror(old, new): 
  return abs((new - old) / new) * 100

# Define the function
def equ(x):
  return x**3 - 0.165*(x**2) + 3.993*(10**-4)
  # another function for checking
  # return -12 - 21*x + 18*x**2 - 2.75*x**3

# Define the bisection method
def bisection_method(a, b, e):
  it = 1
  prevV = 0.0
  print('----------------------------------------')
  print('-----------Bisection Method-------------')
  print('----------------------------------------')
  
  flag = True 
  while flag: 
    c = (a+b) / 2
    err = abserror(prevV, c)
    print('It-%d, x1 = %0.6f and x2 = %0.6f and xm = %0.6f and err = %0.6f' % (it, a, b, c, err))
    
    if(equ(a)*equ(c) < 0):
      b = c
    elif(equ(c) == 0):
      print('Root is : %0.6f' % (c))
      return
    else: 
      a = c
      
    it+=1
    prevV = c
    
    if(err < e):
      flag = False
      print('\n\n The approx. Root is: %0.6f' % c)
      
  
# Taking inputs
try:
  a = float(input('First guess: '))
  b = float(input('second guess: '))
  e = float(input('Tolerable error(in percent): '))
  
except ValueError:
  print('Please enter only valid number and Try again')
  
else: 
  # check if the root is between the guess
  if(equ(a)*equ(b) > 0.0):
    print('The root doesn\'t lie between your guesses.')
    print('Try Again with different guess values.')
    
  elif(equ(a)*equ(b) == 0.0): 
    print('Root: ', a) if equ(a) == 0 else print('Root: ', b)
  else: 
    bisection_method(a, b, e)