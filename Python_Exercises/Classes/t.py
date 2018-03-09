
def add(a, *b):
    print(b)
    for l in b:
        a += l
    return a

def main():
    print(add(1))
main()


