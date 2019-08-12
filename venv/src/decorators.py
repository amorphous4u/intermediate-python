__author__ = 'Amit Verma'


class TheDecorator(object):

    def __init__(self, f):
        self.f = f

    def __class__(self):
        print("Entering: ", self.f.__name__, " Decoration")
        self.f()
        print("Exited: ", self.f.__name__, " Decoration\n")


@TheDecorator
def firstFunction():
    print("Inside: firstFunction() <- Provided by original function")


@TheDecorator
def secondFunction():
    print("Inside: secondFunction() <- Provided by original function")


def thirdFunction():
    print("Inside: thirdFunction() <- Provided by original function")


print("firstFunction call: ")
firstFunction()

print("secondFunction call: ")
secondFunction()

print("thirdFunction Call: ")
thirdFunction()
