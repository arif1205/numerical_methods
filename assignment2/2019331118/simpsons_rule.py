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

#define simpsons rule fun
def simpsons_rule(lm, um, n, truevalue):
  h = (um - lm) / 2 
  #Two segment 
  res = (h/3)*(f(lm) + f(um) + 4*f((lm+um)/2))
  print('\n---------Two Segment------------')
  print('Distance Covered: %0.06f\n' % res)
  err(truevalue, res)
  
  #multi segment
  print('\n---------Multi Segment------------')
  h = (um - lm) / n
  middleSum = 0
  for i in range(n-1):
    if((i+1) % 2 == 0):
      middleSum += 2*f(lm+(i+1)*h)
    else:
      middleSum += 4*f(lm+(i+1)*h)
  
  mres = (h/3)*(f(lm) + middleSum + f(um))
  print('Distance Covered: %0.06f\n' % mres)
  err(truevalue, mres)
  

try:
  lower_limit = float(input('Enter the lower limit: '))
  upper_limit = float(input('Enter the upper limit: '))
  n = int(input('Enter step size for multi segment (only even number): '))
  if(n%2==1):
    raise Exception('Sorry! Please enter only even number of step size.')
  
except ValueError:
  print('Enter numerical value.')
  
except Exception as e:
  print(e)
  
else:
  try:
    truevalue = float(input('Enter true value to judge the result if you know: '))
  except:
    truevalue = 0
    
  simpsons_rule(lower_limit, upper_limit, n, truevalue) 