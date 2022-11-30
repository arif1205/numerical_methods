# import eulers_method as eu
# import Runge_kutta_method as ru
import math

def err(trueValue, currentValue):
  if(trueValue):
    trueErr = abs(trueValue - currentValue)
    trueErrP = trueErr/trueValue*100
    return trueErrP

#define func 
def f(x, y):
  return -2.2067*10**(-12)*(y**4-81*10**8)

#define huens method 
def heuns_method(x0, y0, h, xf, truevalue, it):
  it = int(it)
  
  prevX = x0
  prevY = y0
  for i in range(it):
    k1 = f(prevX, prevY)
    k2 = f(prevX+h, prevY+k1*h)
    y = prevY + 0.5*(k1+k2)*h 
    prevX += h
    prevY = y
  
  return err(truevalue, prevY)
  
#define midpoint method 
def midpoint_method(x0, y0, h, xf, truevalue, it):
  it = int(it)
  
  prevX = x0
  prevY = y0
  for i in range(it):
    k1 = f(prevX, prevY)
    k2 = f(prevX+(h/2), prevY+(k1*h/2))
    y = prevY + k2*h 
    prevX += h
    prevY = y
  
  return err(truevalue, prevY)

#define ralston method 
def ralston_method(x0, y0, h, xf, truevalue, it):
  it = int(it)
  
  prevX = x0
  prevY = y0
  for i in range(it):
    k1 = f(prevX, prevY)
    k2 = f(prevX+(3*h/4), prevY+(3*k1*h/4))
    y = prevY + (k1/3 + 2*k2/3)*h 
    prevX += h
    prevY = y
  
  return err(truevalue, prevY)

#define runge kutta method 
def runge_kutta_method(x0, y0, h, xf, truevalue):
  it = int((xf - x0)/h)
  
  heunsError = heuns_method(x0, y0, h, xf, truevalue, it)
  midpointError = midpoint_method(x0, y0, h, xf, truevalue, it)
  ralstonError = ralston_method(x0, y0, h, xf, truevalue, it)
  
  return [heunsError, midpointError, ralstonError]

def euler_method(x0, y0, h, xf, truevalue):
  it = int((xf - x0)/h)
  
  prevX = x0
  prevY = y0
  for i in range(it):
    y = prevY + f(prevX, prevY)*h 
    prevX += h
    prevY = y
  
  errors = err(truevalue, prevY)
  return errors 

def compareODE(steps, truevalue):
    x0 = float(input('Enter the first value of x, x0: '))
    y0 = float(input('Enter the first value of y, y0: '))
    xf = float(input('Enter the final value of x, xf: '))
    
    print('------------------------------------------')
    print('-------------Error Comparison-------------')
    print('------------------------------------------')
    
    for i in steps:
      h = i
      eulerError = euler_method(x0, y0, h, xf, truevalue)
      rungeErrors = runge_kutta_method(x0, y0, h, xf, truevalue)
      heunsError = rungeErrors[0]
      midpointError = rungeErrors[1]
      ralstonError = rungeErrors[2]
      

      output = 'Step size: {} ---- Euler: {:0.06f} ---- Heuns: {:0.06f} ---- Midpoint: {:0.06f} ---- Ralston: {:0.06f} \n'
      print(output.format(i, eulerError, heunsError, midpointError, ralstonError))
  

try:
    truevalue = float(input('Enter true value to judge the result if you know: '))
    steps = []
    st = int(input('Enter step size (Enter -1 when need to stop):'))
    while(st > 0):
      steps.append(st)
      st = int(input('Enter step size (Enter -1 when need to stop):'))
    
except:
    print('Invalid value entered!')
    
else: 
  compareODE(steps, truevalue)