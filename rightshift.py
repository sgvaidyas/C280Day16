def rightShiftList(l, ix=-1):
    if ix != len(l) * -1:
        l[ix-1], l[ix] = l[ix], l[ix-1]
        return rightShiftList(l, ix-1)
    return l

def perfectNumber(self,number,i):
    global sum
    if i <= number // 2:
        if number % i == 0:
            print(i)
            sum += i
        i += 1
        self.perfectNumber(number, i)
    return sum

def primeNumber(self,n, i=2):
        if n == 1:
            return "Neither prime nor not composite"
        elif i == n // 2:
            return "It's prime"
        elif n % i == 0:
            return "It's not prime"
        return self.primeNumber(n, i + 1)

l = [11,22,33,44]
rightShiftList(l)
"""
ix=-1
-len(l)= -4  T  l[-2],l[-1] = l[-1],l[-2]
l = [11,22,44,33]
   ix=-2
   -len(l)= -4 T l[-3][-2] = l[-2][-3]
    l = [11,44,22,33]   
    ix=-3 != -4 T l[-4][-3] = l[-3][-4]
         l = [44,11,22,33]   
    -4 !=-4 F => l

"""
