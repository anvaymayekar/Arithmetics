class Arithmetics:
    def __init__(self, number):
        self.number = number   

    def isprime(self):
        for i in range(2, self.number):
            if self.number % i == 0:
                return False
                break
            else:
                return True

    def getprimenumbers(self):
        prime = [2, 3, 5]
        for i in range(2, self.number+1):   
            condition = i % 2 == 0 or i % 3 == 0 or i % 5 == 0 or i % 7 == 0 or i % 11 == 0
            if condition:
                continue
            else:
                prime.append(i) 
        return prime[:self.number:]

    def factorize(self):
        factors = []
        for i in range(1, self.number+1):
            if (self.number % i == 0):
                factors.append(i)
        return factors
    
    # with iteration
    def getfactorial(self):
        factor = 1
        for i in range(1, self.number):
            factor *= (i+1)     
        return factor  
    
    # with recursion
    @staticmethod
    def getfactorialrecursion(self, number):
        if number == 0:
            return 1
        return number * self.getfactorialrecursion(self, number=number-1)  
    
    @staticmethod  
    def lcm(num1, num2):
        i = max(num1, num2)
        while True:
            if(i % num1 == 0 and i % num2 == 0):
                return i
                break
            else:
                i+=1
    
    @staticmethod
    def hcf(num1, num2):
        maxNum = min(num1, num2)
        for i in range(maxNum, 1, -1):
            if (num1 % i== 0 and num2 % i == 0):
                return i
                break

    @staticmethod
    def getfibonacci(number):
        a, b = 0, 1
        array = [a, b]
    
        if number <= 0:
            raise ValueError("Fibonnacci numbers cannot be zero or negative")
    
        for i in range(2, number):
            c = a + b
            a, b = b, c 
            array.append(c)
            
        return array[:number:]

arithmeic = Arithmetics(6)
print(arithmeic.isprime()) # returns a boolean whether the given number is prime or not
print(arithmeic.getprimenumbers()) # generates a list of prime numbers from 1 to given number

print(arithmeic.factorize()) # generates a list of factors of the given number
print(arithmeic.getfactorial()) # computes the factorial of the given number through iteration
print(arithmeic.getfactorialrecursion(arithmeic, 5)) # computes the factorial of the given number through iteration

print(arithmeic.lcm(12, 19)) #calculates lcm of the given numbers
print(arithmeic.lcm(12, 19)) #calculates hcf of the given numbers

print(arithmeic.getfibonacci(11)) # generates a list of fiboncci series
        