from H1D import H1D

class H1Dn(H1D):
    """
    Nonuniform step histogram
    """

    # constructor
    def __init__(self, x):
        self._x = sorted(x)

        n  = len(self._x) - 1 # one less bin for a give boundaries
        lo = self._x[0]
        hi = self._x[-1]

        super(H1Dn, self).__init__(n, lo, hi)

    # base functionality - filling
    def find_bin(self, x):
        """
        Given event position X, find bin index
        """

        if (x < self._lo):
            return -1

        if (x > self._hi):
            return self._n;

        lo = 0
        hi = len(self._x) - 1

        while lo < hi:
            mid = (lo + hi)//2
            val = self._x[mid]
            if val > x:
                hi = mid
            else:
                lo = mid

            if (hi - lo) == 1:
                return lo

    # observers
    def x(self):
        """
        Returns sorted bins boundaries
        """
        return self._x

if __name__ == "__main__":
    import random

    g = H1Dn([0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95])
    h = H1Dn([0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 0.95])

    random.seed(11)

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
