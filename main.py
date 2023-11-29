from random import randint


def fifo(referencias_pagina, num_quadros):
  faltas_pagina = 0
  conjunto_quadros = set()
  fila_paginas = []

  for pagina in referencias_pagina:
    if pagina not in conjunto_quadros:
      faltas_pagina += 1
      if len(conjunto_quadros) < num_quadros:
        conjunto_quadros.add(pagina)
        fila_paginas.append(pagina)
      else:
        pagina_removida = fila_paginas.pop(0)
        conjunto_quadros.remove(pagina_removida)
        conjunto_quadros.add(pagina)
        fila_paginas.append(pagina)

  return faltas_pagina


def envelhecimento(referencias_pagina, num_quadros, bits_envelhecimento):
  faltas_pagina = 0
  conjunto_quadros = set()
  registro_idade = {}

  for pagina in referencias_pagina:
    if pagina not in conjunto_quadros:
      faltas_pagina += 1
      if len(conjunto_quadros) < num_quadros:
        conjunto_quadros.add(pagina)
        registro_idade[pagina] = 0
      else:
        while True:
          pagina_menor_idade = min(registro_idade, key=registro_idade.get)
          if pagina_menor_idade in conjunto_quadros:
            conjunto_quadros.remove(pagina_menor_idade)
            conjunto_quadros.add(pagina)
            registro_idade[pagina] = 0
            break
          else:
            del registro_idade[pagina_menor_idade]

    for quadro in list(conjunto_quadros):
      registro_idade[quadro] >>= 1
      if quadro == pagina:
        registro_idade[quadro] |= (1 << (bits_envelhecimento - 1))

  return faltas_pagina


def gerar_referencias_pagina(num_referencias, num_paginas):
  return [randint(0, num_paginas - 1) for _ in range(num_referencias)]


def escrever_em_arquivo(referencias_pagina, nome_arquivo):
  with open(nome_arquivo, 'w') as arquivo:
    for pagina in referencias_pagina:
      arquivo.write(str(pagina) + '\n')


def main():
  num_referencias = 1000
  num_paginas = 20
  bits_envelhecimento = 8
  num_quadros_valores = [1, 2, 3, 4, 5]

  referencias_pagina = gerar_referencias_pagina(num_referencias, num_paginas)
  escrever_em_arquivo(referencias_pagina, 'referencias_pagina.txt')

  for num_quadros in num_quadros_valores:
    faltas_pagina_fifo = fifo(referencias_pagina, num_quadros)
    faltas_pagina_envelhecimento = envelhecimento(referencias_pagina,
                                                  num_quadros,
                                                  bits_envelhecimento)

    print(
        f'Num Quadros: {num_quadros}, Faltas de Página (FIFO): {faltas_pagina_fifo}, Faltas de Página (Envelhecimento): {faltas_pagina_envelhecimento}'
    )


if __name__ == "__main__":
  main()
