import numpy as np

def integ(xs,ys):
    Y = []
    X = []
    temp_y = 0.0
    temp_x = 0.0
    for i in range(len(xs)-1):
        temp_x = (xs[i+1]+xs[i])/2
        X.append(temp_x)

        temp_y += (xs[i+1]-xs[i])*(ys[i+1]+ys[i])/2
        Y.append(temp_y)
    return np.array(X),np.array(Y)

def diff(x,y):
    h = x[1]-x[0]
    y0 = (-3*y[0]+4*y[1]-y[2])/(2*h)
    y1 = (y[2:]-y[:-2])/(2*h)
    y2 = (y[-3]-4*y[-2]+3*y[-1])/(2*h)
    return np.concatenate(([y0],y1,[y2]))

def moving_average(a, n=3):
    ret = np.cumsum(a, dtype=float)
    ret[n:] = ret[n:] - ret[:-n]
    return ret[n - 1:] / n
