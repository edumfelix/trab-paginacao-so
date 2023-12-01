from random import randint


def gera_sequencia_referencias(numero_paginas):
  sequencia = []
  for _ in range(numero_paginas):
    sequencia.append(randint(0, numero_paginas - 1))
  return sequencia


def paginacao_fifo(sequencia_referencias, numero_molduras):
  faltas = 0
  molduras = [-1] * numero_molduras
  for pagina in sequencia_referencias:
    if pagina not in molduras:
      faltas += 1
      moldura_a_substituir = molduras.pop(0)
      molduras.append(pagina)
  return faltas


def paginacao_envelhecimento(sequencia_referencias, numero_molduras):
  faltas = 0
  molduras = [-1] * numero_molduras
  tempos_de_acesso = [0] * numero_molduras
  for pagina in sequencia_referencias:
    if pagina not in molduras:
      faltas += 1
      moldura_a_substituir = -1
      for i in range(numero_molduras):
        if tempos_de_acesso[i] < tempos_de_acesso[moldura_a_substituir]:
          moldura_a_substituir = i
      molduras[moldura_a_substituir] = pagina
      tempos_de_acesso[moldura_a_substituir] = 0
    else:
      tempos_de_acesso[molduras.index(pagina)] = 0
  return faltas


def escrever_em_arquivo(referencias_pagina, nome_arquivo):
  try:
    with open(nome_arquivo, 'r+') as arquivo:
      arquivo.seek(0, 2)
      arquivo.write('\nSequência de referências de páginas:\n')
      for i, pagina in enumerate(referencias_pagina):
        if i % 10 == 0:
          arquivo.write('\n')
        arquivo.write(str(pagina) + ',')
      arquivo.write('\n\n')
  except FileNotFoundError:
    with open(nome_arquivo, 'w') as arquivo:
      arquivo.write('\nSequência de referências de páginas:\n')
      for i, pagina in enumerate(referencias_pagina):
        if i % 10 == 0:
          arquivo.write('\n')
        arquivo.write(str(pagina) + ',')
      arquivo.write('\n\n')


def main():

  numero_paginas = 100
  numero_molduras = 10

  for i in range(1000):
    # Gera a sequência de referências de páginas.
    sequencia_referencias = gera_sequencia_referencias(numero_paginas)

    # Escreve a sequência de referências de páginas no arquivo.
    escrever_em_arquivo(sequencia_referencias, 'referencias_pagina.txt')

    # Executa a paginação FIFO.
    faltas_fifo = paginacao_fifo(sequencia_referencias, numero_molduras)

    # Executa a paginação de envelhecimento.
    faltas_envelhecimento = paginacao_envelhecimento(sequencia_referencias,
                                                     numero_molduras)
    print(f"{i+1}º vez executando")
    print("Número de páginas:", numero_paginas)
    print("Número de molduras:", numero_molduras)
    print("Faltas FIFO:", faltas_fifo)
    print("Faltas envelhecimento:", faltas_envelhecimento)
    print("\n\n")


if __name__ == "__main__":
  main()
