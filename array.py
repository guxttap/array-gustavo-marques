nomes = ["joao", "maria", "jose", "pedro", "ana"]

# Exibindo nomes pelos índices desejados
indices = [0, 2, 4]
for i in indices:
    print(nomes[i])

print("-" * 40)

# Verificando se "maria" está na lista (com capitalização na mensagem)
nome_procurado = "maria"
if nome_procurado in nomes:
    print(f"{nome_procurado.capitalize()} está na lista")
else:
    print(f"{nome_procurado.capitalize()} não está na lista")
