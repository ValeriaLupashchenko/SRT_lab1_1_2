from random import randrange
from math import sin
import matplotlib.pyplot as plt
import matplotlib as mpl


class Signal:

    def __init__(self, n=12, W_max=900, N=256, manually=False, arr=[0,1]):
        if manually:
            self.random_signals = arr
        else:
            self.n = n
            self.W_max = W_max
            self.N = N
            # signal
            self.random_signals = self.create_process()
        self.manually=manually
        print("Process ...")


    def create_process(self):

        x = [0 for i in range(self.N)]
        for i in range(self.N):
            for j in range(self.n):
                A = randrange(0, 100)
                q = randrange(0, 100)
                SINUS = A * sin(((self.W_max/self.n) *( (j + 1) / self.n) )* i + q)
                x[i] += SINUS
        return x

    def get_signal(self):
        return [round(self.random_signals[i], 3) for i in range(len(self.random_signals))]

    def show(self, name="X(t)"):
        # graph
        if self.manually:
            x = [i * 3 for i in range(len(self.random_signals))]
        else:
            x = [i for i in range(len(self.random_signals))]
        plt.title('Signal')
        plt.xlabel('t')
        plt.ylabel(name)
        plt.plot(x, self.get_signal(), color='red',label='X(t)')
        plt.show()

    def get_math_och(self):

        Mx = sum(self.random_signals)/len(self.random_signals)
        return Mx

    def get_variation(self):

        Mx = self.get_math_och()
        Dx = sum([(self.random_signals[i] - Mx)**2 for i in range(len(self.random_signals))])/(len(self.random_signals)-1)
        return Dx


def Rxx(s1, Mx1, D1, s2, Mx2):
    N = int(signal_1.N/2)
    return [sum([(s1[j] - Mx1)*(s2[j+i] - Mx2) for j in range(N)])/((N-1)*D1) for i in range(N)]

def show(t, name="Rxx"):
    plt.title(name)
    plt.xlabel('N')
    plt.ylabel(name)
    plt.plot([i for i in range(int(signal_1.N/2))], t, color='red', label='X(t)')
    plt.show()

signal_1 = Signal()
signal_2 = Signal()

R_xx = Rxx(signal_1.get_signal(), signal_1.get_math_och(), signal_1.get_variation(), signal_1.get_signal(), signal_1.get_math_och())
R_xy = Rxx(signal_1.get_signal(), signal_1.get_math_och(), signal_1.get_variation(), signal_2.get_signal(), signal_2.get_math_och())
print("Rxx = {}".format(R_xx))
print("Rxy = {}".format(R_xy))

signal_1.show()
signal_2.show(name="Y(t)")

show(R_xx)
show(R_xy, name="Rxy")

