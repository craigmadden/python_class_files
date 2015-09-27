def calc_functing(a,b):
    '''
    :param a:
    :param b:
    :return:
    '''
    if a > 10:
        return a - b
    else:
        return a + b

def main():
    mylist = []
    for i in range(5,20,3):
        for j in range(1,4):
            z = calc_functing(i,j)
            # ToDo: add more error checking here
            mylist.append(z)
            print z

main()
