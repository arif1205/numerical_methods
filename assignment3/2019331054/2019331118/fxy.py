import numexpr as ne
import numpy as np
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from sympy.parsing.sympy_parser import standard_transformations,implicit_multiplication_application




def solveEQ(arr):
    a = Symbol('a')
    b = Symbol('b')
    c = Symbol('c')
    d = Symbol('d')
    if len(arr) == 2:
        res = solve(arr, a, b)
    elif len(arr) == 3:
        res = solve(arr, a, b, c)
    elif len(arr) == 4:
        res = solve(arr, a, b, c, d)
    # print(res)

    return res



    

def ddx_f(y, txt):

    user_str = txt
    my_symbols = {'x': Symbol('x', real=True)}
    my_func = parse_expr(user_str, my_symbols)

    hlw = diff(my_func, my_symbols['x'])

    hlw = str(hlw)
    print(hlw)

    return f(y, hlw)



def format_function(given_function):
    # expr = parse_expr(txt)
    transformations = (standard_transformations + (implicit_multiplication_application,))
    expr = parse_expr(given_function, transformations=transformations)
    return expr
def f(a, b, s):
    s = format_function(s)
    s = str(s)
    my_symbols = {'x': Symbol(str(a)), 'y': Symbol(str(b))}
    my_func = parse_expr(s, my_symbols)

    my_func = sympify(str(my_func), evaluate=True)
    res = N(my_func)

    return res
   

# print(f(0,0,input()))
