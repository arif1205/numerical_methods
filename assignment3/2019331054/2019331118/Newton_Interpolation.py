from threading import Thread

import sys
take = input
# input = sys.stdin.readline
show = sys.stdout.write

txt = ''

def showFunctions(inp, l, X):
    global txt
    txt += 'v(t) = b0'
    tt = ''
    for i in range(l-1):
        tt += ' (t-t'+str(i)+')'
        txt += ' + b'+str(i+1)+tt
    txt += '\n'
    txt += 't = '+str(X)+'\n'


    lst = inp[:l]

    lst.sort(key = lambda x: x[1])
    b = list()


    for i in range(l):
        b.append(lst[i][2])
        txt += '(t'+str(i)+', v(t'+str(i)+')) = ('+str(lst[i][1])+', '+str(lst[i][2])+')\n'
    

    res = 0
    tt = 1

    for i in range(l):
        txt += 'b'+str(i)+' = '+str(b[0])+'\n'
        res += b[0]*tt
        for j in range(l-i-1):
            b[j] = (b[j+1]-b[j])/(lst[j+i+1][1]-lst[j][1])

        tt *= (X-lst[i][1])


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

    # print(inp)



    txt += 'Linear Newton\'s divided difference Interpolation: '
    res1 = linear(inp, chk)
    txt += 'Quadratic Newton\'s divided difference Interpolation: '
    res2 = Quadratic(inp, chk)
    txt += 'Cubic Newton\'s divided difference Interpolation: \n'
    res3 = Cubic(inp, chk)

    txt += 'Linear:\t\t'+ str(res1)+ ',\t error = ...\n'

    txt += 'Quadratic:\t\t' + str(res2)+ ',\t error = '+ str(abs(100*(res2-res1)/res2))+'%\n'
    txt += 'Cubic:\t\t' + str(res3) + ',\t error =' + str(abs(100*(res3-res2)/res3)) +'%\n'

    import print_text_gui as ptg
    ptg.showStr('Newton\'s divided difference Interpolation',txt)
# work([[0,10,34],[0,43,423],[0,423,34],[0,42,342],[0,23,432],[0,13,56]], 16)


def run(mat, xx):
    Thread(target=work, args=(mat, xx)).start()