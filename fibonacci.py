
class Fibonacci:
    
    def fibonacci(self, numb):
        if numb <= 1:
            return numb
        return self.fibonacci(numb - 1) + self.fibonacci(numb - 2)