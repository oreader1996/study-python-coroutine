import sys

if __name__ == "__main__":
    l = [i for i in range(100000)]
    # print(type(l))

    gen = (i for i in range(100000))
    # print(type(gen))

    print(sys.getsizeof(1))
    print(sys.getsizeof(10))
    print(sys.getsizeof("hello"))
    print(sys.getsizeof(l))
    print(sys.getsizeof(gen))
