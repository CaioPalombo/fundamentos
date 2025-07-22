def grupo1_gerador_caixas(local = "Aquario", quantidade = 5):
  i = 1  # Início do contador das caixas

  print(f"\n📍 Local de coleta: {local}")
  print(f"📦 Quantidade de caixas a serem recolhidas: {quantidade}\n")
  input("👉 Pressione Enter para iniciar a geração das caixas...\n")

  #para exemplificar a utilização do return
  lista_caixas_return = []

  # Estrutura while: repete enquanto i for menor ou igual à quantidade solicitada
  while i <= quantidade:
      # Código único da caixa no formato CX001, CX002, etc.
      codigo = f"CX{i:03d}"

      # Tupla identificadora, usada para representar algo imutável e único
      identificador = (codigo, i)

      # Dicionário que representa os dados da caixa
      caixa = {
          "codigo": codigo,
          "nome": f"{codigo} - 📦 Caixa {i} do {local}",
          "local": local,
          "identificador": identificador
      }

      # Mostra ao usuário as informações da caixa gerada
      print(f"✅ Caixa gerada: {caixa['nome']}")
      print(f"🔑 Código: {caixa['codigo']}, Local: {caixa['local']}, ID: {caixa['identificador']}")
      input("🛑 Pausa para comentar esta etapa. Pressione Enter para continuar...\n")

      #este append é para exemplificar a utilização do return
      lista_caixas_return.append(caixa)

      # yield permite retornar a caixa sem encerrar a função — ela 'pausa' aqui
      yield caixa

      # Incrementa o contador da próxima caixa
      i += 1

  #print (lista_caixa_return)
  # explicar a diferença do return e do print

  #return permite retornar a lista completa. Quando o return é executado a função é terminada
  return lista_caixas_return


  print("\n✅ Todas as caixas foram geradas com sucesso!")
  input("👉 Pressione Enter para encerrar o Grupo 1...\n")