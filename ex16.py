nome_aluno = input('Insira o nome do aluno: \n') 
idade_aluno = int(input('Insira a idade do aluno: \n')) 
numero_provas = int(input('Insira o numero de provas realizadas pelo aluno: \n'))

while numero_provas<2: 
    print('O numero mínimo de provas a ser inserido é 3! Por favor, digite novamente') 
    numero_provas = int(input('Insira o numero de provas realizadas pelo aluno: \n'))

notas_aluno = [int(input('Insira a nota: \n')) for i in range(numero_provas)] 
notas_media = [i for i in notas_aluno]

notas_media.remove(max(notas_media)) 
notas_media.remove(min(notas_media))

media_aluno = sum(notas_media)/len(notas_media)

condicao_media = media_aluno > 5

lista_final = [nome_aluno,idade_aluno,notas_aluno,media_aluno,condicao_media]

print(lista_final)