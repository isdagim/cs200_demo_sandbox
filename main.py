def foo(x, y):
    return (x*y) + 1


def bar(x, y):
    return (x*y) + 2


def baz(x, y):
    return x**y


def func1():
    lst = []
    print('Enter numbers one at a time. Enter 0 to stop.')
    inpNum = int(input('num:'))
    while inpNum != 0:
        lst.append(inpNum)
        inpNum = int(input('num:'))
    print('You added', len(lst), 'numbers.')
    return lst


def func2(data):
    print('Here is the data:')
    print(data)

    Selection = ''
    while True:
        Selection = input('Select an option. 1-sum  2-min  3-max  4-quit')
        menu(data, Selection)


def menu(data, Selection):
    if Selection == '1':
        print('The sum is', sum(data))
    elif Selection == '2':
        print('Not supported yet')
    elif Selection == '3':
        print('Not supported yet')
    elif Selection == '4':
        print('Goodbye')
        return


def main():
    print("Hello, World!")
    data = func1()
    func2(data)


if __name__ == "__main__":
    main()
