from threading import Thread

import sys
take = input
# input = sys.stdin.readline
show = sys.stdout.write

txt = ''

def showFunctions(inp, l, X):

    global txt
    
    p = 0
    arr = list()
    res = 0
    for line in range(l):

        x = inp[line][1]
        y = inp[line][2]
        

        txt += 't'+str(line)+' = '+str(x)+'\n'
        txt += 'v(t'+str(line)+') = '+str(y)+'\n'

        eq = ''

        L = 1
        for i in range(l):
            if i==line:
                continue
            xp = inp[i][1]
            L *= (X-xp)/(x-xp)
        
        txt += 'L(t'+str(line)+') = '+str(L)+'\n'
        txt += 'v(t'+str(line)+') * L(t'+str(line)+') = '+str(y*L)+'\n'
        res += y*L
        txt += '\n'


    txt += 'v('+str(X)+') = '+str(res)+'\n\n\n'
    

    return res

def linear(inp, X):
    return showFunctions(inp, 2, X)

def Quadratic(inp, X):
    return showFunctions(inp, 3, X)

def Cubic(inp, X):
    return showFunctions(inp, 4, X)
    

def work(inp, chk):
    global txt
    chk = float(chk)
    for i in range(len(inp)):
        inp[i][0] = abs(inp[i][1] - chk)
    inp.sort()


    txt += 'Linear Lagrangian Interpolation: \n'
    res1 = linear(inp, chk)
    txt += 'Quadratic Lagrangian Interpolation: \n'
    res2 = Quadratic(inp, chk)
    txt += 'Cubic Lagrangian Interpolation: \n'
    res3 = Cubic(inp, chk)

    txt += 'Linear:\t\t'+ str(res1)+ ',\t error = ...\n'

    txt += 'Quadratic:\t\t' + str(res2)+ ',\t error = '+ str(abs(100*(res2-res1)/res2))+'%\n'
    txt += 'Cubic:\t\t' + str(res3) + ',\t error =' + str(abs(100*(res3-res2)/res3)) +'%\n'

    import print_text_gui as ptg
    ptg.showStr('Lagrangian Interpolation',txt)
# work([[0,10,34],[0,43,423],[0,423,34],[0,42,342],[0,23,432]], 16)


def run(mat, xx):
    Thread(target=work, args=(mat, xx)).start()