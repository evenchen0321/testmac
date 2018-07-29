def f1(f):
    while f != '12345':
        if f == '1':
            print('1')
            break
        elif f == '2':
            print('2')
            f2(input('233:'))
            break
        else:
            print('3')


def f2(f21):
    while f21 != 'q':
        print('123')
        break


f1(input("123:"))