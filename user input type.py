#to find out the data type of user input data
st = input()
try:
    type(int(st))==int
    print('This input is of type Integer.')
except ValueError:
    try:
        type(float(st))==float
        print('This input is of type Float.')
    except ValueError:
        type(st)==str
        print('This input is of type string.')
