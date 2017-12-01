#http://www.practicepython.org/exercise/2014/04/30/13-fibonacci.html


def fibo(num):
    """Returns the fibonacci sequence in the range of the num"""

    fibo1 = 0
    fibo2 = 1
    fibonacci = []
    for i in xrange(num+1):
        fibo2 = fibo2 + fibo1
        fibo1 = fibo2 - fibo1
        fibonacci.append(fibo2)
    return fibonacci

num = int(raw_input("What large do you want your fibonacci sequence: "))
print fibo(num)