def media_lista():
    lista_resposta = []
    nome = input('Insira seu nome? ')
    idade = int(input('Insira sua idade: '))
    quant_notas = int(input('Quantas notas vc possui? '))
    notas = []
    for i in range(quant_notas + 1):
        if i < quant_notas:
            i = float(input('Insira sua nota'))
            notas.append(i)
            i += 1
        
        media = sum(notas) / quant_notas
        verify = media > 5
        lista_resposta = [nome, idade, notas, media, verify]
    return lista_resposta
        
    
media_lista()