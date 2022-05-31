def questao_teste_mesa(n1,n2):
    while n1 != n2:
        if (n1 < n2):
            n2 = n2-n1
        else:
            n1 = n1-n2
    return n1

print(questao_teste_mesa(40,5))