test = 1


#def f1():
#    print(test)
#    test = 7
#    print(test)


#f1()


def f2():
    test = 2
    print(test)

    if 'test' not in globals():
        raise Exception
    if 'test' not in locals():
        raise Exception


f2()


def func():
    var = 1

    #def f3():
    #    par = 2
    #    if 'var' not in locals():
    #        raise Exception
    #    print('var' in locals())

    #f3()

    def f4():
        par = 3
        print(var)
        if 'var' not in locals():
            raise Exception

    f4()

    #def f5():
    #    var = 4
    #    par = 4
    #    print(var)
    #    if 'var' not in globals():
    #        raise Exception

    #f5()


func()
