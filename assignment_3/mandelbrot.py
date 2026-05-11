import numpy as np

#define the function
def mandelbrot(c, max_iter=100):
    """
    Iterate z = z^2 + c for each point c in the complex plane.
    Returns an array of iteration counts at which each point diverged.
    Points that never diverge are given the value max_iter.
    """
    z = np.zeros_like(c)   #creates a grid of zeros having same shape of c
    diverge_iter = np.full(c.shape, max_iter) 
    # ^^ Creates a grid filled with max_iter (100) for every point. Points that diverge, their values are updated. 
    for i in range(max_iter):
        mask = np.abs(z)**2 <= 4 #True for points that are still bounded
        z[mask] = z[mask]**2 + c[mask] #Only update z for points that are still bounded. 
        
        #Find points that just diverged this iteration and haven't been recorded yet, then record which iteration they diverged at.
        diverged = (np.abs(z)**2 > 4) & (diverge_iter == max_iter)
        diverge_iter[diverged] = i
    return diverge_iter #Return the grid of iteration counts