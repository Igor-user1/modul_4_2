def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
    inner_function()
    return


print(test_function())
print(inner_function())
