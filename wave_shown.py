import matplotlib.pyplot as plt
import numpy as np

def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

def Sin(x):
    return np.sin(x)

def sinElement(idx, total, x):
    n_fac = factorial(total)
    nMk = factorial(total - idx)
    nPk = factorial(total + idx)
    return (n_fac * n_fac) / (nMk * nPk) * (Sin(idx * x) / idx)

def asymSin(x):
    ammount_of_asymmetry = 5
    result = sinElement(1, ammount_of_asymmetry, x)
    for i in range(2, ammount_of_asymmetry):
        result += sinElement(i, ammount_of_asymmetry, x)
    return result*1.1

def ramp(x):
    alpha = 20 / 100
    result = []
    for i in x:
        if i < 2*alpha*np.pi or (i > 2*np.pi and i < (2*np.pi+2*alpha*np.pi)):
            result.append(1)
        else:
            if i > 2*alpha*np.pi and i < 2*np.pi:
                result.append((-i / np.pi + 1 + alpha) / (1 - alpha))
            else:
                i -= 2*np.pi
                result.append((-i / np.pi + 1 + alpha) / (1 - alpha))
    return result

def step(x):
    alpha = 20 / 100
    result = []
    for i in x:
        if i < 2*alpha*np.pi or (i > 2*np.pi and i < (2*np.pi+2*alpha*np.pi)):
            result.append(1)
        else:
            result.append(0)
    return result

def twoStep(x):
    alpha = 20 / 100
    beta = 25 / 100
    beta_amp = 0.12
    result = []
    for i in x:
        if i < 2*alpha*np.pi or (i > 2*np.pi and i < (2*np.pi+2*alpha*np.pi)):
            result.append(1)
        elif i < 2*(alpha+beta)*np.pi or (i > 2*np.pi and i < (2*np.pi+2*(alpha+beta)*np.pi)):
            result.append(beta_amp)
        else:
            result.append(0)
    return result

def threeToOne(x):
    result = []
    for i in range(len(x)):
        if i < 3/4 * len(x):
            result.append(abs(Sin(x[i])))
        else:
            result.append(Sin(x[i]))
    return result

def revAsymSin(x):
    ammount_of_asymmetry = 5
    result = sinElement(1, ammount_of_asymmetry, x)
    for i in range(2, ammount_of_asymmetry):
        result += sinElement(i, ammount_of_asymmetry, x)
    return -result*1.1

def revRamp(x):
    alpha = 20 / 100
    result = []
    for i in x:
        if i < 2*alpha*np.pi or (i > 2*np.pi and i < (2*np.pi+2*alpha*np.pi)):
            result.append(-1)
        else:
            if i > 2*alpha*np.pi and i < 2*np.pi:
                result.append(-(-i / np.pi + 1 + alpha) / (1 - alpha))
            else:
                i -= 2*np.pi
                result.append(-(-i / np.pi + 1 + alpha) / (1 - alpha))
    return result

def revStep(x):
    alpha = 20 / 100
    result = []
    for i in x:
        if i < 2*alpha*np.pi or (i > 2*np.pi and i < (2*np.pi+2*alpha*np.pi)):
            result.append(-1)
        else:
            result.append(0)
    return result

def revTwoStep(x):
    alpha = 20 / 100
    beta = 25 / 100
    beta_amp = 0.12
    result = []
    for i in x:
        if i < 2*alpha*np.pi or (i > 2*np.pi and i < (2*np.pi+2*alpha*np.pi)):
            result.append(-1)
        elif i < 2*(alpha+beta)*np.pi or (i > 2*np.pi and i < (2*np.pi+2*(alpha+beta)*np.pi)):
            result.append(-beta_amp)
        else:
            result.append(0)
    return result

def revThreeToOne(x):
    result = []
    for i in range(len(x)):
        if i < 3/4 * len(x):
            result.append(-abs(Sin(x[i])))
        else:
            result.append(-Sin(x[i]))
    return result

def main():
    x = np.arange(0,4*np.pi,0.1)
    a = Sin(x)

    b = asymSin(x)
    c = ramp(x)
    d = step(x)
    e = twoStep(x)
    f = threeToOne(x)

    m = revAsymSin(x)
    n = revRamp(x)
    o = revStep(x)
    p = revTwoStep(x)
    q = revThreeToOne(x)

    # plt.plot(x,a, x,b, x,m)
    # plt.plot(x,a, x,c, x,n)
    # plt.plot(x,a, x,d, x,o)
    # plt.plot(x,a, x,e, x,p)
    plt.plot(x,f, x,q)
    plt.xlabel('Time')
    plt.ylabel('Displacement')
    plt.ylim(ymin=-2, ymax=2)
    # plt.legend(['sin wave', 'asymmetric sin (+)', 'asymmetric sin ( - )'])
    # plt.legend(['sin wave', 'ramp down (+)', 'ramp down ( - )'])
    # plt.legend(['sin wave', 'asymmetric square (+)', 'asymmetric square ( - )'])
    # plt.legend(['sin wave', '2-step square (+)', '2-step square ( - )'])
    plt.legend(['3-1 sin (+)', '3-1 sin ( - )'])
    plt.show()

if __name__ == '__main__':
    main()
