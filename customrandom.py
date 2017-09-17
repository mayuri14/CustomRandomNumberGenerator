import math, time

class MyRNG:

    def __init__(self, low = 0, high = 0):
    #     The constructor initializes data members "m_min" and "m_max"
        if(low < 2):
            low = 2
        if(high < 2):
            high = 9223372036854775807
        self.m_min = low
        self.m_max = high
        self.m_seed = time.time()

    def Seed(self, seed):
    #  Seed the generator with 'seed'
        self.m_seed = seed

    def Next(self):
    #     Return the next random number"
        a = self.m_min
        m = self.m_max
        q = math.trunc(m / a)
        
        r = m % a
        
        hi = self.m_seed / q
        lo = self.m_seed % q
        x = (a * lo) - (r * hi)
        
        if(x < a):
           x += a
        
        self.m_seed = x
        self.m_seed %= m
        
        # ensure that the random number is not less
        # than the minimum number within the user specified range
        if(self.m_seed < a):
            self.m_seed += a

        return int(self.m_seed)

def test():
    min_count=0
    max_count=0
    mylist=[]
    random = MyRNG(1, 10)
    for x in range(100):
        num=random.Next()
        if(num<5 and min_count<27):
            min_count+=1
            mylist.append(num)
        else:
            max_count+=1
            mylist.append(num)
    print(len(mylist),min_count,max_count)
    print(mylist)


if __name__ == '__main__':
    test()


