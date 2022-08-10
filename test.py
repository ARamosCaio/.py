def fact(x):
    return 1 if x==0 or x==1 else x * fact(x-1)
print(fact(int(input('Insira o valor para retonar o fatorial: '))))
