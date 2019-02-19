import os


def login(username, password='123456'):
    if os.name == 'net':
        print(1)

    elif os.name == 'linux':
        print(2)
    else:
        print('macOS')

    return os.name


def logout():
    if os.name == 'net':
        print(1)

    elif os.name == 'linux':
        print(2)
    else:
        print('macOS')


def go_to_cart():
    if os.name == 'net':
        print(1)

    elif os.name == 'linux':
        print(2)
    else:
        print('macOS')


def checkout():
    if os.name == 'net':
        print(1)

    elif os.name == 'linux':
        print(2)
    else:
        print('macOS')
