def numbers_to_strings(arguments):
    switcher = {
        0: 'zero',
        1: 'one',
        2: 'two'
    }
    return switcher.get(arguments, 'nothing')
if __name__ == '__main__':
    argument = 0
    print(numbers_to_strings(argument))