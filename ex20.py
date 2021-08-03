import random

def create_deck(): 
    naipe = ['Copas','Espadas','Ouro','Paus'] 
    numero = ['Ás','2','3','4','5','6','7','8','9','10','Dama','Valete','Rei'] 
    deck = {} 
    for i in numero: 
        for j in naipe: 
            carta = i+'-'+j 
            if carta[:2] == 'Ás': 
                deck[carta] = 1 
            elif carta[0:2] == '10': 
                deck[carta] = 10

            else:
                try:
                    valor_carta = int(carta[0])
                    deck[carta] = valor_carta
                except:
                    deck[carta] = 10

    return deck

def random_card(deck): 
    selection = random.choice(list(deck.keys())) 
    value = deck[selection] 
    del deck[selection] 
    return value

def jogada(player,dic,deck): 
    while dic[player]['ativo'] == True: 
        print('Você possui {} pontos!'.format(dic[player]['pontos'])) 
        resposta = int(input('{},Deseja continuar jogando?(1 - Sim | 0 - Não) \n'.format(player))) 
        if resposta == 0: 
            dic[player]['ativo'] = False 
        else: 
            valor_jogada = random_card(deck) 
            pontos_jogada = dic[player]['pontos'] 
            pontos_jogada+=valor_jogada 
            dic[player]['pontos'] = pontos_jogada 
            if dic[player]['pontos'] > 21: 
                print('Você passou de 21 pontos, infelizmente está eliminado da rodada!') 
                dic[player]['ativo'] = False

def main(): 
    num_jogadores = int(input('Insira o numero de jogadores: \n')) 
    dic_jogo = {} 
    deck = create_deck() 
    lista_players = [] 
    lista_pontos = []
    
    for i in range(num_jogadores):
        nome_jogador = input('Insira o nome do jogador {}: \n'.format(i+1))
        dic_jogo[nome_jogador] = {'pontos':0,'ativo':True}

    for i in dic_jogo.keys():
        jogada(i,dic_jogo,deck)

    for i in dic_jogo.keys():
         if dic_jogo[i]['pontos'] <=21:
                lista_players.append(i)
                lista_pontos.append(dic_jogo[i]['pontos'])
    maximo_pontos = max(lista_pontos)

    indices = [index for index, elemento in enumerate(lista_pontos) if elemento == maximo_pontos]
    vencedores = [lista_players[i] for i in indices]

    return print('Os vencedores são: {}'.format(vencedores))

main()