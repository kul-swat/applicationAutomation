import logging
logging.basicConfig(filename="log_test.log",level=logging.DEBUG,
                    format='%(asctime)s: %(levelname)s: %(message)s')

def add(a,b):
    return a + b 

def substract(a,b):
    return a - b

def multiplication(a,b):
    return a * b

def division(a, b):
    return a // b

a = 2
b = 3
checking_addition = add(a,b)
logging.debug("so addition result is " +  str(checking_addition))

checking_substraction = substract(a,b)
logging.debug("so substraction result is " + str(checking_substraction))

checking_multiplication = multiplication(a,b)
logging.debug("so multiplication result is " + str(checking_multiplication))

checking_division = division(a,b)
logging.debug("so division result is " + str(checking_division))