cpf = list(str((input("CPF:"))))
aux = list(reversed(range(2, 12)))
verify = 0
for x in range(1, len(aux)):
    verify += int(cpf[x-1]) * aux[x]
if verify*10%11 != int(cpf[9]):
    print("CPF invalido")
    exit()

verify = 0
for x in range(len(aux)):
    verify += int(cpf[x]) * aux[x]
if verify*10%11 != int(cpf[10]):
    print("CPF invalido")
    exit()
print("CPF Validado")