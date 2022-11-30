
def betaArr(x, y):
    # x = list(map(int, input().split()))
    # y = list(map(int, input().split()))

    avg_y = sum(y)/len(y)
    avg_x = sum(x)/len(x)

    down = 0

    for X in x:
        down += (X-avg_x)**2

    up = 0
    for i in range(len(x)):
        up += (x[i]-avg_x)*(y[i]-avg_y)

    beta1 = up/down

    beta2 = avg_y - beta1 * avg_x

    return [beta1, beta2]
# import numpy as np
# import matplotlib.pyplot as plt
# x = np.array(range(-100,100))
# y = x * beta1 + beta2
# c = ''
# if beta2 > 0:
#     c = '+'+str(beta2)
# elif beta2 == 0:
#     c = ''
# else:
#     c = str(beta2)
# plt.plot(x,y,label=('y='+str(beta1)+'x'+c))
# plt.xlabel('X')
# plt.ylabel('Y')
# plt.legend()
# plt.show()


