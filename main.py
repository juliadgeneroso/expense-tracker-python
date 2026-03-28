gastos = [ ]

while True:
  print("\n--- Controle de Gastos ---")
  print("1. Adicionar gasto")
  print("2. Ver gastos")
  print("3. Ver total geral")
  print("4. Ver total por categoria")
  print("5. Rmover gasto")
  print("6. Sair")

opcao = input("Escolha uma opção: ")

if opcao == "1":
  nome = input("Nome do gasto: ")
  valor = float(input("Valor: "))
  categoria = input("Categoria (comida, transporte, etc): ")

  gastos.append({
   "nome": nome,
   "valor": valor,
   "categoria": categoria
})

  print("Gasto adicionado!")

elif opcao == "2":
  if not gastos:
    print("Nenhum gasto encontrado.")
  else:
    for i, gasto in enumerate(gastos, 1):
      print(f"{i}. {gasto['nome']} - R$ {gasto['valor']} ({gasto['categoria']}")

elif opcao == "3":
  total = sum(gasto["valor"] for gasto in gastos)
  print(f"Total geral: R$ {total}")

elif opcao == "4":
  categorias = {}

  for gasto in gastos:
    cat = gasto["categoria"]
    categorias[cat] = categorias.get(cat, 0) + gasto["valor"]

  print("\n--- Total por categoria ---")
  for cat, total in categorias.items():
    print(f"{cat}: R$ {total}")

elif opcao == "5":
  if not gastos:
    print(Nenhum gasto para remover.")
  else:
    for i, gasto in enumerate(gastos, 1):
      print(f"{i}. {gasto['nome']} - R$ {gasto['valor']}")

    num = int(input("Número do gasto para remover: "))

    if 0 < num <= len(gastos):
      gastos.pop(num - 1)
      print("Gasto removido!")
    else:
      print("Número inválido.")

elif opcao == "6":
  print("Saindo...")
  break

else:
  print("Opção inválida")

