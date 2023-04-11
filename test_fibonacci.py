import unittest
from fibonacci import Fibonacci


class TestFibonacci(unittest.TestCase):

    def testFibonacci_I(self):
        fibo = Fibonacci()
        result = fibo.fibonacci(1)
        self.assertEqual(result, 1)

    def testFibonacci_II(self):
        fibo = Fibonacci()
        result = fibo.fibonacci(2)
        self.assertEqual(result, 1)

    def testFibonacci_III(self):
        fibo = Fibonacci()
        result = fibo.fibonacci(3)
        self.assertEqual(result, 2)
    
    def testFibonacci_IV(self):
        fibo = Fibonacci()
        result = fibo.fibonacci(4)
        self.assertEqual(result, 3)

    def testFibonacci_V(self):
            fibo = Fibonacci()
            result = fibo.fibonacci(5)
            self.assertEqual(result, 5)

    def testFibonacci_VI(self):
        fibo = Fibonacci()
        result = fibo.fibonacci(6)
        self.assertEqual(result, 8)

    def testFibonacci_VII(self):
        fibo = Fibonacci()
        result = fibo.fibonacci(7)
        self.assertEqual(result, 13)

    def testFibonacci_VIII(self):
        fibo = Fibonacci()
        result = fibo.fibonacci(8)
        self.assertEqual(result, 21)

    def testFibonacci_IX(self):
        fibo = Fibonacci()
        result = fibo.fibonacci(9)
        self.assertEqual(result, 34)

    def testFibonacci_X(self):
        fibo = Fibonacci()
        result = fibo.fibonacci(10)
        self.assertEqual(result, 55)








if __name__ == '__main__':
    unittest.main()









