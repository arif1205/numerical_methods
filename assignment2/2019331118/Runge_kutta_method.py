import math

#define func 
def f(x, y):
  return -2.2067*10**(-12)*(y**4-81*10**8)

#define error 
def err(trueValue, currentValue):
  if(trueValue):
    trueErr = abs(trueValue - currentValue)
    trueErrP = trueErr/trueValue*100
    print('Absolute True Error: %0.06f' % trueErr)
    print('Absolute True Error in percent %0.06f' % trueErrP)

#define huens method 
def heuns_method(x0, y0, h, xf, truevalue, it):
  print('\n-----------Heuns Method-----------')
  it = int(it)
  
  prevX = x0
  prevY = y0
  for i in range(it):
    k1 = f(prevX, prevY)
    k2 = f(prevX+h, prevY+k1*h)
    y = prevY + 0.5*(k1+k2)*h 
    prevX += h
    prevY = y
  
  print('The solution is: %0.06f' % prevY) 
  err(truevalue, prevY)
 
  
#define midpoint method 
def midpoint_method(x0, y0, h, xf, truevalue, it):
  print('\n-----------Midpoint Method-----------')
  it = int(it)
  
  prevX = x0
  prevY = y0
  for i in range(it):
    k1 = f(prevX, prevY)
    k2 = f(prevX+(h/2), prevY+(k1*h/2))
    y = prevY + k2*h 
    prevX += h
    prevY = y
  
  print('The solution is: %0.06f' % prevY) 
  err(truevalue, prevY)
  
#define ralston method 
def ralston_method(x0, y0, h, xf, truevalue, it):
  print('\n-----------Midpoint Method-----------')
  it = int(it)
  
  prevX = x0
  prevY = y0
  for i in range(it):
    k1 = f(prevX, prevY)
    k2 = f(prevX+(3*h/4), prevY+(3*k1*h/4))
    y = prevY + (k1/3 + 2*k2/3)*h 
    prevX += h
    prevY = y
  
  print('The solution is: %0.06f' % prevY) 
  err(truevalue, prevY)

#define runge kutta method 
def runge_kutta_method(x0, y0, h, xf, truevalue):
  print('----------------------------------------')
  print('-----------Runge Kutta Method-----------')
  print('----------------------------------------')
  
  it = (xf - x0)/h
  while(it != math.floor(it)):
    print('Please Enter different step size.')
    try:
      h = int(input('New Step size: '))
      it = (xf - x0)/h
    except ValueError:
      print('Something went wrong!! Please enter a value')
      continue
  
  heuns_method(x0, y0, h, xf, truevalue, it)
  midpoint_method(x0, y0, h, xf, truevalue, it)
  ralston_method(x0, y0, h, xf, truevalue, it)


try: 
  x0 = float(input('Enter the first value of x, x0: '))
  y0 = float(input('Enter the first value of y, y0: '))
  xf = float(input('Enter the final value of x, xf: '))
  h = int(input('Enter the step size: '))
  
except ValueError:
  print('Please enter a number next time.')
  
except: 
  print('Something went wrong!')

else: 
  try:
    truevalue = float(input('Enter true value to judge the result if you know: '))
  except:
    truevalue = 0
  runge_kutta_method(x0, y0, h, xf, truevalue)