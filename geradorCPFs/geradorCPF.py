import sys


def firstDigit(seed):
    ''' The returned quotient is the first CPF digit.'''
    position = 10
    tmp = 0
    for i in seed:
        tmp = tmp + (position * int(i))
        position = position - 1

    digit = int(tmp / 11)
    remainder = tmp % 11

#    print(digit, remainder)

    if remainder < 2:
        return(0)
    else:
        return(11 - remainder)



def secondDigit(seed, firstDigit):
    ''' Returns the CPF second digit.'''
    position = 11
    tmp = 0
    seed = str(seed) + str(firstDigit)

    for i in seed:
        tmp = tmp + (position * int(i))
        position = position - 1

    digit = int(tmp / 11)
    remainder = tmp % 11

    if remainder < 2:
        return(0)
    else:
        return(11 - remainder)



def main():
    finput = sys.argv[1]
    foutput = sys.argv[2]

    #### Generate data:
    fin = open(finput) 
    fout = open(foutput, 'a')
    for i in fin.readlines(): 
        seed = i.replace('\n','')
        tmp1 = firstDigit(seed.rstrip())
        tmp2 = secondDigit(seed.rstrip(), tmp1)
       
        cpf = str(seed) + str(tmp1) + str(tmp2) + '\n'
        fout.write(cpf) 
        
    fin.close()
    fout.close()


    return(0)

if __name__=='__main__':
    main()
