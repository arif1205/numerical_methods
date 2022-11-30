from math import log

#define fun
def f(x):
  return 2000*log(140000/(140000-2100*x)) - 9.8*x

#define error 
def err(trueValue, currentValue):
  if(trueValue):
    trueErr = abs(trueValue - currentValue)
    trueErrP = trueErr/trueValue*100
    print('Absolute True Error: %0.06f' % trueErr)
    print('Absolute True Error in percent %0.06f' % trueErrP)

#define trapizoidal rule fun
def trapizoidal_rule(lm, um, n, truevalue):
  #single segment 
  res = ((um - lm)*(f(lm)+f(um))/2)
  print('\n---------Single Segment------------')
  print('Distance Covered: %0.06f\n' % res)
  err(truevalue, res)
  
  #multi segment
  print('\n---------Multi Segment------------')
  middleSum = 0
  h = (um - lm) / n 
  for i in range(n-1):
    middleSum += 2*f(lm+(i+1)*h)
  
  mres = (h/2)*(f(lm) + middleSum + f(um))
  print('Distance Covered: %0.06f\n' % mres)
  err(truevalue, mres)
  

try:
  lower_limit = float(input('Enter the lower limit: '))
  upper_limit = float(input('Enter the upper limit: '))
  n = int(input('Enter step size for multi segment: '))
  
except ValueError:
  print('Enter numerical value.')
  
else:
  try:
    truevalue = float(input('Enter true value to judge the result if you know: '))
  except:
    truevalue = 0
    
  trapizoidal_rule(lower_limit, upper_limit, n, truevalue) 