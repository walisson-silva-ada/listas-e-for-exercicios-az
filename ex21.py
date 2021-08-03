def coleta_informacao(): 
    nome = input('Insira o nome: \n') 
    cpf = input('Insira o CPF: \n') 
    email = input('Insira o Email: \n') 
    lista_informacao = [nome,cpf,email] 
    return lista_informacao

def cadastrar_cliente(lista_geral): 
    novo_cadastro = coleta_informacao() 
    lista_geral.append(novo_cadastro)

def verificar_cpf(lista_geral,cpf): 
    for i in lista_geral: 
        if i[1] == cpf: 
            return print(i)
        return print('Usuário não encontrado!')

def main(): 
    lista_geral = [] 
    resposta = 100
    while resposta !=0:
        resposta = int(input('Insira o que desejada: \n 0 - Sair \n 1 - Cadastrar novo usuário \n 2 - Procurar por CPF \n 3 - Mostrar todos os cadastros \n '))

        if resposta == 1:
            cadastrar_cliente(lista_geral)
        elif resposta == 2:
            cpf_busca = input('Insira o CPF que deseja ser buscado: \n')
            verificar_cpf(lista_geral,cpf_busca)
        elif resposta == 3:
            print(lista_geral)
            
main()