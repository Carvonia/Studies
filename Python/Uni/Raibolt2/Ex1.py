#Por: Matheus Cunha Nogueira
#Matrícula: 06006159

#Exercício1
def MatrizIdentidade(n):
    Matriz1 = []
    for i in range(n):
        Linha = []
        for j in range(n):
            Linha.append(1 if i == j else 0)
        Matriz1.append(Linha)
    return Matriz1
Ordem = 5
MatrizIdentidadeOrder = MatrizIdentidade(Ordem)
for Linha in MatrizIdentidadeOrder:
    print(Linha)
