import numpy as np
import matplotlib.pyplot as plt

class sinWaveForm:
    def __init__(self, **kwargs) :
        self.end = kwargs.get('end', 1)
        self.sample = kwargs.get('sample', 0.01)
        self.amp = kwargs.get('amp', 1)
        self.freq = kwargs.get('freq', 1)
        self.start = kwargs.get('start', 0)
        self.base = kwargs.get('base', 0)

    def calcDomain(self) :
        return np.arange(0.0, self.end, self.sample)

    def calcSinValue(self, time) :
        return self.amp * np.sin(2*np.pi*self.freq*time + self.start) + self.base
    def plotWave(self) :
        time = self.calcDomain()
        result = self.calcSinValue(time)
    
        plt.plot(time, result)
        plt.grid(True)
        plt.xlabel('time')
        plt.ylabel('sin')
        plt.show()

if __name__ == "__main__" :
    test = sinWaveForm(amp = 2, end = 1)
    test.end1 = 2
    print(test.calcDomain())
    print(test.calcSinValue(test.calcDomain()))
    test.plotWave()
