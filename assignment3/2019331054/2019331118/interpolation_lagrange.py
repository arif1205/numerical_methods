import matplotlib.pyplot as plt
import pandas as pd
import numpy as np


def lagrange_method():  
  print("Performing linear interpolation using Lagrange method: ")
  print("Enter first point: ")
  x0 = float(input('x0 = '))
  y0 = float(input('y0 = '))

  print("Enter second point: ")
  x1 = float(input('x1 = '))
  y1 = float(input('y1 = '))

  print("Enter calculation point: ")
  x = float(input('x = '))
  
 

  y_linear = (((x-x1)*y0)/(x0-x1)) + (((x-x0)*y1)/(x1-x0))


  print("Performing quadratic interpolation: ")

  print("Enter first point: ")
 
  x0 = float(input('x0 = '))
  y0 = float(input('y0 = '))

  print("Enter second point: ")
  x1 = float(input('x1 = '))
  y1 = float(input('y1 = '))

  print("Enter third point: ")
  x2 = float(input('x2 = '))
  y2 = float(input('y2 = '))
  

  print("Enter calculation point: ")
  x = float(input('x = '))



  y_quadratic = ((x-x1)/(x0-x1))*((x-x2)/(x0-x2))*y0 + ((x-x0)/(x1-x0))*((x-x2)/(x1-x2))*y1 + ((x-x0)/(x2-x0))*((x-x1)/(x2-x1))*y2

  


  print("Performing cubic interpolation: ")
  print("Enter first point: ")
  x0 = float(input('x0 = '))
  y0 = float(input('y0 = '))

  print("Enter second point: ")
  x1 = float(input('x1 = '))
  y1 = float(input('y1 = '))

  print("Enter third point: ")
  x2 = float(input('x2 = '))
  y2 = float(input('y2 = '))

  print("Enter fourth point: ")
  x3 = float(input('x3 = '))
  y3 = float(input('y3 = '))
  

  print("Enter calculation point: ")
  x = float(input('x = '))



  y_cubic = ((x-x1)/(x0-x1))*((x-x2)/(x0-x2))*((x-x3)/(x0-x3))*y0 + ((x-x0)/(x1-x0))*((x-x2)/(x1-x2))*((x-x3)/(x1-x3))*y1 + ((x-x0)/(x2-x0))*((x-x1)/(x2-x1))*((x-x3)/(x2-x3))*y2 + ((x-x0)/(x3-x0))*((x-x1)/(x3-x1))*((x-x2)/(x3-x2))*y3

 
  print('Interpolated value at %0.4f is %0.4f for linear interpolation' %(x,y_linear))
  print('Interpolated value at %0.4f is %0.4f for quadratic interpolation' %(x,y_quadratic))
  print('Interpolated value at %0.4f is %0.4f for cubic interpolation' %(x,y_cubic))
  error_1 = (abs(y_quadratic-y_linear)/y_quadratic) * 100
  error_2 = (abs(y_cubic-y_quadratic)/y_cubic) * 100
  
 

  column_1 = pd.Series([int(1),y_linear,"---"],name='col_1')
  column_2 = pd.Series([int(2),y_quadratic,error_1],name='col_2')
  column_3 = pd.Series([int(3),y_cubic,error_2],name='col_3')

  table=pd.concat([column_1,column_2,column_3],axis=1)
  table = table.rename( columns = {"col_1": " ", "col_2": " ", "col_3": " "})
  table = table.rename(index={0: 'Order of polynomial', 1: 'Interpolated value', 2:'Absolute relative approximate error'})

  print(table)

 
  


lagrange_method()  







