# Define absolute error calculation
def abserror(old, new): 
  return abs((new - old) / new) * 100

# Define the function
def equ(x):
  # return x**3 - 0.165*(x**2) + 3.993*(10**-4)
  # another function for checking
  return -1+5.5*x-4*x**2+0.5*x**3
  
# Derivation of equation
def dequ(x):
  # return 3*(x**2) - 2*0.165*x
  return 5.5 - 8*x + 1.5*x**2 
  
# Define the False Position method
def newton_raphson(a, e):
  it = 1
  prevV = 0.0
  print('--------------------------------------------')
  print('-----------Newton Raphson Method-------------')
  print('---------------------------------------------')
  
  flag = True 
  while flag: 
    if(dequ(a) == 0):
      print('Impossible guess! Can\'t divide by zero. Try with different guess')
      return
    
    c = a - (equ(a) / dequ(a))
    err = abserror(prevV, c)
    print('It-%d, xi = %0.6f and xi+1 = %0.6f and Error = %0.6f' % (it, a, c, err))
    
    a = c
      
    it+=1
    prevV = c
    
    if(err < e):
      flag = False
      print('\n\n The approx. Root is: %0.6f' % c)
  
# Taking inputs
try:
  a = float(input('First guess: '))
  e = float(input('Tolerable error(in percent): '))
  
except ValueError:
  print('Please enter only valid number and Try again')
  
else: 
    newton_raphson(a, e)