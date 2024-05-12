def area():
    length, width = yield
    while True:
        length, width = yield length * width


if __name__ == "__main__":
    gen = area()
    next(gen)  # 启动生成器
    print(gen.send((3, 5)))
    print(gen.send((2, 4)))
    print(gen.send((4, 8)))

    for i in range(10):
        print(gen.send((i * 2, i * 3)))
