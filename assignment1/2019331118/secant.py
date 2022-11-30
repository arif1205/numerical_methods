# Define absolute error calculation
def abserror(old, new): 
  return abs((new - old) / new) * 100

# Define the function
def equ(x):
  # return x**3 - 0.165*(x**2) + 3.993*(10**-4)
  # another function for checking
  return -12 - 21*x + 18*x**2 - 2.4*x**3
  
# Define the False Position method
def secant(a, b, e):
  it = 1
  prevV = 0.0
  print('--------------------------------------------')
  print('-----------Secant Method-------------')
  print('---------------------------------------------')
  
  flag = True 
  while flag: 
    if(equ(a) == equ(b)):
      print('Impossible guess! Can\'t divide by zero. Try with different guess')
      return
    
    c = b - ((equ(b)*(b-a)) / (equ(b) - equ(a)))
    err = abserror(prevV, c)
    print('It-%d, x0 = %0.6f and x1 = %0.6f and xm = %0.6f and Error = %0.6f' % (it, a, b, c, err))
    
    a = b
    b = c
      
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
    secant(a, b, e)