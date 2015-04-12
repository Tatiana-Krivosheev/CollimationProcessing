from H1D import H1D

class H1Du(H1D):
    """
    Uniform step histogram
    """

    # constructor
    def __init__(self, n, lo, hi):
        super(H1Du, self).__init__(n, lo, hi)

        self._step = (self._hi - self._lo) / float(self._n)

    # find bin, defined in derived class
    def find_bin(self, x):
        """
        Given event position X, find bin index
        """

        if (x < self._lo):
            return -1

        if (x > self._hi):
            return self._n;

        return int( (x-self._lo)/self._step )

    # observers
    def step(self):
        """
        Returns step size
        """
        return self._step

if __name__ == "__main__":
    import random

    random.seed(11)

    g = H1Du(10, 0.1, 0.9)
    h = H1Du(10, 0.1, 0.9)

    for i in range(0,1000000):
        x = random.random()

        g.fill(x)
        h.fill(x, 2.0)

    # printing g
    norm = g.integral()
    size = g.size()

    under = g.underflow()
    print(under[0]/norm, under[1])
    for k in range(0, size):
        bin = g[k]
        print(bin[0]/norm, bin[1])
    over = g.overflow()
    print(over[0]/norm, over[1])
    print( "----------------------------" )

    # printing h
    norm = h.integral()
    size = h.size()

    under = h.underflow()
    print(under[0]/norm, under[1])
    for k in range(0, size):
        bin = h[k]
        print(bin[0]/norm, bin[1])
    over = h.overflow()
    print(over[0]/norm, over[1])
