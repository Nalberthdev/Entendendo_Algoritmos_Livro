def pesquisa_binaria(lista, item):
    baixo = 0
    alto = len(lista) - 1
     
    while baixo <= alto:
        meio = (baixo + alto) // 2  # Corrigido para divisão inteira
        chute = lista[meio]
        if chute == item:
            return meio
        if chute > item:
            alto = meio - 1
        else:
            baixo = meio + 1
    return None

minha_lista = [1, 3, 5, 7, 9]

print(pesquisa_binaria(minha_lista, 3))  # Saída esperada: 1
print(pesquisa_binaria(minha_lista, -1))  # Saída esperada: None
