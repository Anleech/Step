def f(a, x=5, *args, **kwargs):
    print(a)
    print(x)
    print(args)
    print(kwargs)


f(1, 2, 3, 4, b='test', c='hi')
