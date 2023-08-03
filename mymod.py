print(f'Hello from mymod!')

x = 100

y = [10, 20, 30]

d = {'a':100, 'b':200, 'c':300}   # I added this dict to mymod

def hello(name):
    return f'Hello, {name}, from mymod!'

print(f'Goodbye from mymod!')

if __name__ == '__main__':  # this is only true when the module is run as a program (i.e., not imported)
    print('Never see this when imported!')