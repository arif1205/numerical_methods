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

  
def euler_method(x0, y0, h, xf, truevalue):
  print('----------------------------------------')
  print('--------------Euler Method--------------')
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
  
  it = int(it)
  
  prevX = x0
  prevY = y0
  for i in range(it):
    y = prevY + f(prevX, prevY)*h 
    prevX += h
    prevY = y
    # print(f(prevX, prevY))
  
  print('The solution is: %0.06f' % prevY) 
  err(truevalue, prevY)

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
  euler_method(x0, y0, h, xf, truevalue)