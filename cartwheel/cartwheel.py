from os import system, name
from time import sleep

print(__name__)


# define our clear function to clear screen in windows and linux
def clear():
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


# The walking man matrix will stay here
M1 = [['9', '9', 'o', '9', '9', '9'],
      ['9', '/', '|', "\\", '9', '9'],
      ['9', '/', '9', "\\", '9', '9']]

M2 = [["\\", '9', 'o', '9', '/', '9'],
      ['9', '9', '9', '|', '9', '9'],
      ['9', '9', '/', '9', "\\", '9']]

M3 = [['9', '9', '9', '_', '9', 'o', '9', '9', '9'],
      ['9', '9', '9', '9', '9', '/', "\\", '9', '9'],
      ['9', '9', '9', '9', '|', '9', "\\", '9', '9']]

M4 = [['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9'],
      ['9', '9', '9', '9', '9', '9', '9', '_', '_', '_', "\\", 'o'],
      ['9', '9', '9', '9', '9', '9', '/', ')', '9', '9', '|', '9']]

M5 = [['9', '9', '9', '9', '9', '9', '9', '9', '9', '_', '_', '|', '9', '9', '9'],
      ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', "\\", 'o', '9'],
      ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '(', '9', "\\"]]

M6 = [['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', "\\", '9', '/', '9', '9', '9'],
      ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '|', '9', '9', '9'],
      ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '/', 'o', "\\", '9', '9']]

M7 = [['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '|', '_', '_', '9'],
      ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', 'o', '/', '9', '9', '9'],
      ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '/', '9', ')', '9', '9', '9']]

M8 = [
    ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9',
     '9'],
    ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', 'o', '/', '_', '_',
     '9'],
    ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '|', '9', '9', '(',
     "\\"]]

M9 = [
    ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', 'o',
     '9', '_', '9', '9'],
    ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9',
     '/', "\\", '9', '9'],
    ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9',
     '/', '9', '|', '9']]

M10 = [
    ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', "\\", '9',
     'o', '9', '/', '9'],
    ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9',
     '9', '|', '9', '9'],
    ['9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9', '9',
     '/', '9', "\\", '9']]

# Mapping the matrix with string variables
Relate = {'M1': M1, 'M2': M2, 'M3': M3, 'M4': M4, 'M5': M5, 'M6': M6, 'M7': M7, 'M8': M8, 'M9': M9, 'M10': M10}


# the code calls matrix to perform a cart wheel
def cartwheel():
    # back cartwheel
    for i in range(10, 1, -1):
        # print(Relate["M{}".format(i)])
        for item in Relate["M{}".format(i)]:
            for atom in item:
                if atom == '9':
                    print(" ", end='')
                else:
                    print(atom, end='')
            print("")
        sleep(0.2)
        clear()
    # front cartwheel
    for i in range(1, 11):
        # print(Relate["M{}".format(i)])
        for item in Relate["M{}".format(i)]:
            for atom in item:
                if atom == '9':
                    print(" ", end='')
                else:
                    print(atom, end='')
            print("")
        sleep(0.2)
        clear()

    # set the number of front and back cartwheels and do the cart wheel.


for _ in range(3):
    cartwheel()
