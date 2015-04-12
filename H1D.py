class H1D(object):

    DATA = 0 # data index
    NOE  = 1 # number of events index
    VAR  = 2 # bin variance index

    # constructor
    def __init__(self, n, lo, hi):
        """
        Initialize histogram event storage
        """

        self._n  = n
        self._lo = lo
        self._hi = hi

        self._integral   = 0.0
        self._variance   = 0.0
        self._nof_events = 0

        # Bin is defined to be a tuple of (float, int, float)
        self._underflow = (0.0, 0, 0.0)
        self._overflow  = (0.0, 0, 0.0)

        self._data     = [ (0.0, 0, 0.0) for k in range(self._n)]

    # base functionality - filling
    def fill(self, x, weight = 1.0):
        """
        Fill bin given event position and weight
        """

        self._nof_events += 1
        self._integral   += weight
        self._variance   += weight*weight

        idx = self.find_bin(x)

        if (idx < 0):
#            print(x,weight)
            t = (self._underflow[H1D.DATA] + weight, self._underflow[H1D.NOE] + 1, self._underflow[H1D.VAR] + weight*weight)
            self._underflow = t
            return

        if (idx >= self._n):
#            print(x,weight)
            t = (self._overflow[H1D.DATA] + weight, self._overflow[H1D.NOE] + 1, self._overflow[H1D.VAR] + weight*weight)
            self._overflow = t
            return

        t = (self._data[idx][H1D.DATA] + weight, self._data[idx][H1D.NOE] + 1, self._data[idx][H1D.VAR] + weight*weight)
        self._data[idx] = t
        return

    # indexer defined
    def __getitem__(self, idx):
        if (idx < 0):
            return self._underflow

        if (idx >= self._n):
            return self._overflow

        return self._data[idx]

    # observers
    def size(self):
        return self._n

    def lo(self):
        return self._lo

    def hi(self):
        return self._hi

    def integral(self):
        return self._integral

    def variance(self):
        return self._variance

    def nof_events(self):
        return self._nof_events

    def underflow(self):
        return self._underflow

    def overflow(self):
        return self._overflow

    def data(self):
        return self._data
