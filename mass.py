'''from div import *'''
def root(func):
    def inner(a,b):
        if b==0:
            print(f'division not possible')
        return func(a,b)
    return inner
@root
def div(a,b):
    print (a/b)
div(1,0)