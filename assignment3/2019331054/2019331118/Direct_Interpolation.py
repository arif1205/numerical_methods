from threading import Thread

import fxy as fg
import sys
take = input

show = sys.stdout.write
txt = ''

def f(x, y):
    global function
    return fg.f(x, y, function)
def showFunctions(inp, l, X):
    global txt
    
    p = 0
    arr = list()
    for line in range(l):

        x = inp[line][1]
        y = inp[line][2]
        
        eq = ''
        
        for i in range(l):
            if x**i == 0:
                continue
            if i != 0:
                eq += ' + '
            if x**i != 1:
                eq += str(x**i)+'*'
                # show(str(x**i))
            eq += chr(ord('a')+i)
        txt += eq + ' = '+ str(y)+'\n'
        eq += ' - '+str(y)

        arr.append(eq)

    resd = fg.solveEQ(arr)
    txt += str(resd)+'\n'
    y = 0
    xx = 1
    for x in resd:
        y += resd[x]*xx
        xx *= X
    txt += 'f('+str(X)+') = '+str(y)+'\n'

    txt+= '\n'
    return y

def linear(inp, X):
    return showFunctions(inp, 2, X)

def Quadratic(inp, X):
    return showFunctions(inp, 3, X)

def Cubic(inp, X):
    return showFunctions(inp, 4, X)

def work(inp, chk):

    d = dict()
    # inp = list()
    # for _ in range(int(input())):
    #     x, y = map(float, input().split())
    #     inp.append([0, x, y])
    #     d[x] = y
    chk = float(chk)
    for i in range(len(inp)):
        inp[i][0] = abs(inp[i][1] - chk)
    inp.sort()

    global txt


    txt+='Linear Direct Interpolation: \n'
    res1 = linear(inp, chk)
    txt+='Quadratic Direct Interpolation: \n'
    res2 = Quadratic(inp, chk)
    txt+='Cubic Direct Interpolation: \n'
    res3 = Cubic(inp, chk)
    # print(txt)

    txt += 'Linear:\t\t'+ str(res1)+ ',\t error = ...\n'

    txt += 'Quadratic:\t\t' + str(res2)+ ',\t error = '+ str(abs(100*(res2-res1)/res2))+'%\n'
    txt += 'Cubic:\t\t' + str(res3) + ',\t error =' + str(abs(100*(res3-res2)/res3)) +'%\n'

    import print_text_gui as ptg
    ptg.showStr('Direct_Interpolation',txt)
# work([[0,10,34],[0,43,423],[0,423,34],[0,42,342],[0,23,432]], 16)

def run(mat, xx):
    Thread(target=work, args=(mat, xx)).start()