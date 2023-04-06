{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyN6t55d+HQ9ZURPiOJldFZ/"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "Yy9JD4rs8St8"
      },
      "outputs": [],
      "source": [
        "#MUNDO 03 PYTHON"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "lanche = ('hambúrguer','pizza','pudim','suco','refri')\n",
        "\n",
        "for c in range(0, len(lanche)):\n",
        "  print(f'nós temos {lanche[c]}')\n",
        "\n",
        "for c in lanche:\n",
        "  print(f'nós temos {c}')"
      ],
      "metadata": {
        "id": "b4IpscxE8YY8"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 72\n",
        "\n",
        "contagem = ('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez','Onze','Doze','Treze','Catorze','Quinze','Dezesseis','Dezessete','Dezoito','Dezenove','Vinte')\n",
        "\n",
        "while True:\n",
        "  num = int(input('Digite um número entre 0 e 20: '))\n",
        "  if num >= 0 and num <= 20:\n",
        "    print(f'''\n",
        "Você digitou {num}, que se escreve {contagem[num]}''')\n",
        "    a = input('''\n",
        "Quer continuar? [s/n] ''').lower()\n",
        "    if a == 's':\n",
        "      print('Muito bem.')\n",
        "    elif a == 'n':\n",
        "      print('Ok.')\n",
        "      break\n",
        "    else:\n",
        "      print('O meu senhor, tu é burro')\n",
        "      break\n",
        "  else:\n",
        "    print('Preste atenção!')\n"
      ],
      "metadata": {
        "id": "3Xxo2O8k8ZcU"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 73\n",
        "\n",
        "times = ('Palmeiras','Internacional','Flamengo','Fluminense','Corinthians','Athletico-PR','Atlético-MG','América-MG',\n",
        "'Fortaleza','Botafogo','Santos','São Paulo','Bragantino','Goiás','Coritiba','Ceará SC','Cuiabá','Atlético-GO','Avaí','Juventude')\n",
        "\n",
        "print(times)\n",
        "print(f'''\n",
        "{times[:5]} são os times que formam o G5.''')\n",
        "print(f'''\n",
        "{times[-4:]} são os times que serão rebaixados''')\n",
        "print(f'''\n",
        "Os times em ordem alfabética: {sorted(times)}''')\n",
        "\n",
        "for cont in range(0, len(times)):\n",
        "  if cont == 13:\n",
        "    print(f'''\n",
        "{times[cont]} está na 14ª posição.''')\n",
        "    \n",
        "#print(f'Goiás está na {times.index(\"Goiás\")+1}ª posição.')"
      ],
      "metadata": {
        "id": "mRtT6NLi8aza"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 74\n",
        "from random import randint\n",
        "\n",
        "lista = (randint(0,99),randint(0,99),randint(0,99),randint(0,99),randint(0,99))\n",
        "#print(f'{lista} foram os número sorteados.')\n",
        "\n",
        "for n in lista:\n",
        "  \n",
        " print(f'{n} ', end='')\n",
        "\n",
        "print(f'''\n",
        "\\nO maior Valor foi {max(lista)}''')\n",
        "print(f'O Menor Valor foi {min(lista)}')\n",
        "    "
      ],
      "metadata": {
        "id": "4YyDn5FLPKVv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 75\n",
        "\n",
        "cont = 0 #contagem de 9\n",
        "par = 0 # numeros pares\n",
        "\n",
        "a = int(input('Digite um valor: '))\n",
        "if a == 9:\n",
        "  cont += 1\n",
        "elif a % 2 == 0:\n",
        "  par += 1\n",
        "b = int(input('Digite um valor: '))\n",
        "if b == 9:\n",
        "  cont += 1\n",
        "elif b % 2 == 0:\n",
        "  par += 1\n",
        "c = int(input('Digite um valor: '))\n",
        "if c == 9:\n",
        "  cont += 1\n",
        "elif c % 2 == 0:\n",
        "  par += 1\n",
        "d = int(input('Digite um valor: '))\n",
        "if d == 9:\n",
        "  cont += 1\n",
        "elif d % 2 == 0:\n",
        "  par += 1\n",
        "\n",
        "lista = (a, b, c, d)\n",
        "\n",
        "n3  = []\n",
        "if a == 3:\n",
        "  n3.append(1)\n",
        "if b == 3:\n",
        "  n3.append(2)\n",
        "if c == 3:\n",
        "  n3.append(3)\n",
        "if d == 3:\n",
        "  n3.append(4)\n",
        "\n",
        "\n",
        "print(f'''\n",
        "\n",
        "Os valores escolhidos foram: {lista}''')\n",
        "print(f'''\n",
        "O valor 9 apareceu {cont} vezes.''')\n",
        "print(f'{par} número(s) par(es) foram digitados.')\n",
        "print(f'O número 3 apareceu nas posições {n3}')"
      ],
      "metadata": {
        "id": "o2cvlEsEWB-b"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Resolução Guanabara - desafio 75\n",
        "num = ((int(input('Digite o número: ')), (int(input('Digite o número: '))), (int(input('Digite o número: '))), (int(input('Digite o número: ')))))\n",
        "\n",
        "print(f'Você digitou os valores {num}')\n",
        "\n",
        "print(f'O valor 9 apareceu {num.count(9)} vezes.')\n",
        "\n",
        "if 3 in num:\n",
        "  print(f'O valor 3 apareceu na {num.index(3)+1}ª posição.')\n",
        "else:\n",
        "  print('Não foi digitado o número 3.')\n",
        "print(f'Os valores pares digitados foram ', end='')\n",
        "for n in num:\n",
        "  if n % 2 == 0:\n",
        "    print(n, end=' ')"
      ],
      "metadata": {
        "id": "EciisHI-pwAn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 76\n",
        "\n",
        "from tabulate import tabulate\n",
        "\n",
        "produtos = ( ['Caneta bic', 1.90], ['Apagador de quadro', 5.99], ['Caderno s/pauta', 13.99], ['Borracha', 1.35], ['Pillot', 4.50], ['Grafite 0.5', 3.99])\n",
        "\n",
        "print(tabulate(produtos, headers = ['Produto', 'Preço R$']))"
      ],
      "metadata": {
        "id": "LchVtigIDa5v"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#Resolução Guanabara - desafio 76\n",
        "\n",
        "produtos = ( 'Caneta bic', 1.90, \n",
        "            'Apagador de quadro', 5.99, \n",
        "            'Caderno s/pauta', 13.99, \n",
        "            'Borracha', 1.35, \n",
        "            'Pillot', 4.50, \n",
        "            'Grafite 0.5', 3.99)\n",
        "\n",
        "print('-'*40)\n",
        "print(f'{\"PRODUTOS\":^40}')\n",
        "print('-'*40)\n",
        "\n",
        "for c in range(0, len(produtos)):\n",
        "  if c % 2 == 0:\n",
        "    print(f'{produtos[c]:.<30}', end='')\n",
        "  else:\n",
        "    print(f'R${produtos[c]:>7.2f}')"
      ],
      "metadata": {
        "id": "orUNn7ORvs__"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 77\n",
        "\n",
        "palavra = ('ameixa', 'vinho', 'azeite', 'ferro', 'abacate', 'miojo', \n",
        "           'pizza', 'beterraba', 'arroz', 'feijao', 'farofa', \n",
        "           'carne', 'leite', 'curso', 'papel')\n",
        "\n",
        "for c in palavra:\n",
        "  print(f'\\nNa palavra {c.upper()} temos as vogais: ', end='')\n",
        "  for letra in c:\n",
        "    if letra.lower() in 'aeiou':\n",
        "      print(letra, end =' ')\n"
      ],
      "metadata": {
        "id": "JwPbMfRGGG2b"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#INTRODUÇÃO A VARIÁVEIS COMPOSTAS (LISTAS PARTE 1)"
      ],
      "metadata": {
        "id": "-Jqu4ZZDrB5A"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "'''lista = [1,2,3,4,5,6,7,8,9,0]\n",
        "print(lista)\n",
        "\n",
        "lista[0] = int(input('Novo valor: '))   # para substituir um valor específico da lista\n",
        "print(lista)\n",
        "\n",
        "lista.append(9999)    #para acrescentar um novo valor na lista pelo final\n",
        "print(lista)\n",
        "\n",
        "lista.insert(0,0)   #adicionando um novo valor na posição 0 reenumerando os outros valores\n",
        "print(lista)\n",
        "\n",
        "#formas de eliminar valores da lista\n",
        "\n",
        "#del lista[3] #deleta o terceiro valor\n",
        "\n",
        "#lista.pop() # deleta o um valor na posição indicada\n",
        "\n",
        "#lista.remove(3) #remove o valor 3 da lista\n",
        "\n",
        "#print(lista)'''\n",
        "\n",
        "#para entender melhor\n",
        "import time\n",
        "\n",
        "faculdade = ['medicina', 'direito', 'engenharia', 'física', 'geografia', 'enfermagem', 'ciência de dados', 'educação física']\n",
        "print('-'*40)\n",
        "print(f'{\"BEM-VINDO A NOSSA FACULDADE\":^40}')\n",
        "print('-'*40)\n",
        "print('''\n",
        "Catalogo de cursos: \n",
        "''')\n",
        "for n in range(0, len(faculdade)):\n",
        "  print(f'{faculdade[n]}')\n",
        "\n",
        "novo = str(input('Ficou faltando algum curso? [s/n] ')).lower()\n",
        "\n",
        "while True:\n",
        "  if novo == 's':\n",
        "    faculdade.append(str(input('Qual curso gostaria de incluir? ')))\n",
        "  elif novo == 'n':\n",
        "    print('''\n",
        "Fim''')\n",
        "    break\n",
        "  else:\n",
        "    print('''\n",
        "Error''')\n",
        "    break\n",
        "  print('''\n",
        "Aguarde enquanto incluimos o novo curso''')\n",
        "\n",
        "  time.sleep(4)\n",
        "\n",
        "  print('''\n",
        "\n",
        "Lista de cursos atualizada!!!\n",
        "  ''')\n",
        "  time.sleep(2)\n",
        "\n",
        "  print('''\n",
        "Catalogo de cursos: \n",
        "  ''')\n",
        "  for n in range(0, len(faculdade)):\n",
        "    print(f'{faculdade[n]}')\n",
        "  break"
      ],
      "metadata": {
        "id": "Lxwj9QefrRgy"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 78\n",
        "lista = list()\n",
        "\n",
        "for c in range(0,5):\n",
        "  num = lista.append(int(input(f'{c+1}º valor da lista: ')))\n",
        "\n",
        "\n",
        "print(f'*'*30)\n",
        "print(f'O maior valor digitado foi: {max(lista)} e está nas posições: ', end='')\n",
        "for i, v in enumerate(lista):\n",
        "  if v == max(lista):\n",
        "    print(f'{i+1} ', end='')\n",
        "\n",
        "print(f'''\n",
        "O menor valor digitado foi: {min(lista)} e está nas posições: ''',end='')\n",
        "for i, v in enumerate(lista):\n",
        "  if v == min(lista):\n",
        "    print(f'{i+1} ', end='')\n",
        "print()\n",
        "print('*'*30)\n"
      ],
      "metadata": {
        "id": "mxeQ9Uib5Ldw"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desagio 79\n",
        "import time\n",
        "lista = list()\n",
        "\n",
        "while True:\n",
        "  num = int(input('Digite um número: '))\n",
        "  if num not in lista:\n",
        "    lista.append(num)\n",
        "    time.sleep(0.5)\n",
        "    print('Valor adicionado com sucesso!')\n",
        "  else:\n",
        "    time.sleep(0.5)\n",
        "    print('Valor duplicado! Não foi adicionado novamente.')\n",
        "  cont = input('Gostari de continuar? [s/n] ').lower()\n",
        "  if cont == 'n':\n",
        "    break\n",
        "  elif cont != 's' and cont != 'n':\n",
        "    print('error')\n",
        "    break\n",
        "\n",
        "print(f'Você adicionou os valores {sorted(lista)}')"
      ],
      "metadata": {
        "id": "aS6RgWVUGbVj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 80 - lista organizada sem o sort\n",
        "\n",
        "#Resolução Guanabara\n",
        "lista = []\n",
        "for c in range(0,5):\n",
        "  n = int(input('Digite um valor: '))\n",
        "  if c == 0 or n > lista[-1]:\n",
        "    lista.append(n)\n",
        "  else:\n",
        "    pos = 0\n",
        "    while pos < len(lista):\n",
        "      if n <= lista[pos]:\n",
        "        lista.insert(pos, n)\n",
        "        print(f'Adicinado na posição {pos}')\n",
        "        break\n",
        "      pos += 1\n",
        "\n",
        "print('-='*30)\n",
        "print(f'Os valores digitados em ordem foram: {lista}')"
      ],
      "metadata": {
        "id": "dpi-xdvkJ2_W"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 81\n",
        "\n",
        "lista = []\n",
        "g = False\n",
        "\n",
        "\n",
        "while True:\n",
        "  num = int(input('Digite um número: '))\n",
        "  if num == 5:\n",
        "    g = True\n",
        "  lista.append(num)\n",
        "  cont = input('Deseja continuar? [s/n] ').lower()\n",
        "  if cont == 'n':\n",
        "    break\n",
        "  if cont != 's' and cont != 'n':\n",
        "    print('ERROR')\n",
        "    break\n",
        "\n",
        "print(f'''\n",
        "Os valores digitados foram {lista}''')\n",
        "print(f'''\n",
        "Foram digitados: {len(lista)} valores''')\n",
        "\n",
        "lista.sort(reverse = True)\n",
        "print(f'''\n",
        "Os valores em ordem decrescente: {lista}''')\n",
        "\n",
        "if g == True:\n",
        "  print('''\n",
        "O número 5 está na lista.''')\n",
        "else:\n",
        "  print('''\n",
        "O número 5 não está na lista.''')"
      ],
      "metadata": {
        "id": "ahq5trAw9bE0"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "valores = ['8','2','5','4','9','3','0']\n",
        "valores.sort(reverse = True)\n",
        "print(valores)"
      ],
      "metadata": {
        "id": "DMBrl57Q8LIk"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 82\n",
        "\n",
        "lista = list()\n",
        "par = list()\n",
        "impar = list()\n",
        "\n",
        "while True:\n",
        "  num = int(input('Digite um valor: '))\n",
        "  lista.append(num)\n",
        "  if num % 2 == 0:\n",
        "    par.append(num)\n",
        "  else: \n",
        "    impar.append(num)\n",
        "  cont = input('Deseja continuar? [s/n] ').lower()\n",
        "  if cont == 'n':\n",
        "    break\n",
        "  elif cont != 'n' and cont != 's':\n",
        "    print('error')\n",
        "    break\n",
        "\n",
        "print(f'''A lista digitada foi: {sorted(lista)}\n",
        "Valores pares: {sorted(par):}\n",
        "Valores impares: {sorted(impar):}''')"
      ],
      "metadata": {
        "id": "dhSDt0w89AVh"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 83 -  verificação de parenteses na frase\n",
        "\n",
        "exp = str(input('Digite a sua expressão: '))\n",
        "lista = list()\n",
        "\n",
        "for simb in exp:\n",
        "  if simb == '(':\n",
        "    lista.append('(')\n",
        "  elif simb == ')':\n",
        "    if len(lista) > 0:\n",
        "      lista.pop()\n",
        "    else:\n",
        "      lista.append(')')\n",
        "      break\n",
        "if len(lista) == 0:\n",
        "  print('Sua expressão está correta.')\n",
        "else:\n",
        "  print('Sua expressão está errada.')\n",
        "\n",
        "\n"
      ],
      "metadata": {
        "id": "XJJeTkI2-uqG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#time 3x3 LoL\n",
        "import random\n",
        "nomes = ['Fã do Billy Joel', 'xcopox', 'Mytologicbn', 'Guziin', 'Rmlx926', 'Titanio22']\n",
        "random.shuffle(nomes)\n",
        "\n",
        "A = list()\n",
        "B = list()\n",
        "\n",
        "player = 0\n",
        "\n",
        "for cont in nomes:\n",
        "  player += 1\n",
        "  if player <= 3:\n",
        "    A.append(cont)\n",
        "  else:\n",
        "    B.append(cont)\n",
        "\n",
        "print(f'''Time Azul: {A}\n",
        "\n",
        "Time Vermelho: {B}''')\n"
      ],
      "metadata": {
        "id": "1TyxW6PpkqK4"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a = [5,10,15,1,13,8]\n",
        "b = ['janeiro','fevereiro','março','abril','maio','junho']\n",
        "import matplotlib.pyplot as plt\n",
        "\n",
        "plt.scatter(b,a)\n",
        "\n",
        "plt.xlabel('mês')\n",
        "plt.ylabel('Dias de chuva')\n",
        "plt.title('Dias com chuva em 2022')\n",
        "\n",
        "plt.show()"
      ],
      "metadata": {
        "id": "eEpdFjgOzaac"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#aula 18"
      ],
      "metadata": {
        "id": "0CaYuqRTCCvj"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "teste = list()\n",
        "teste.append('Gustavo')\n",
        "teste.append(40)\n",
        "galera = list()\n",
        "galera.append(teste)\n",
        "print(galera)"
      ],
      "metadata": {
        "id": "Ru0HbFgYGMyd"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 84 - cadastro\n",
        "pessoas = list()\n",
        "dados = list()\n",
        "maiorpeso = list()\n",
        "menorpeso = list()\n",
        "\n",
        "num = 0\n",
        "\n",
        "while True:\n",
        "  n = input('Nome: ')\n",
        "  i = int(input('Peso (kg): '))\n",
        "  num += 1\n",
        "  dados.append(n)\n",
        "  dados.append(i)\n",
        "  pessoas.append(dados[:])\n",
        "  dados.clear()\n",
        "  cont = input('Deseja continuar? [s/n]').lower()\n",
        "  if cont != 's':\n",
        "    break\n",
        "\n",
        "for pessoa in pessoas:\n",
        "  if pessoa[1] >=80:\n",
        "    maiorpeso.append(pessoa[0])\n",
        "  else:\n",
        "    menorpeso.append(pessoa[0])\n",
        "\n",
        "print(f'Foram cadastradas {num} pessoas.')\n",
        "print(f'As pessoas de peso maior que 80kg são: {maiorpeso}')\n",
        "print(f'As pessoas de peso menor que 80kg são: {menorpeso}')"
      ],
      "metadata": {
        "id": "33scQY9hZ_jR"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#resolução guanabara desafio 84\n",
        "temp = []\n",
        "princ = []\n",
        "mai = men = 0\n",
        "\n",
        "while True:\n",
        "  temp.append(str(input('Nome: ')))\n",
        "  temp.append(float(input('Peso: ')))\n",
        "  if len(princ) == 0:\n",
        "    mai = men = temp[1]\n",
        "  else:\n",
        "    if temp [1] > mai:\n",
        "      mai = temp[1]\n",
        "    if temp[1] < men:\n",
        "      men = temp[1]\n",
        "    princ.append(temp[:])\n",
        "    temp.clear()\n",
        "    resp = str(input('Quer continuar? [s/n]'))\n",
        "    if resp in 'Nn':\n",
        "      break\n",
        "\n",
        "print('-='*30)\n",
        "print(f'Ao todo, você cadastrou {len(princ)} pessoas.')\n",
        "print(f'O maior peso foi de {mai}kg. Peso de ', end='')\n",
        "for p in princ:\n",
        "  if p[1] == mai:\n",
        "    print(f'[{p[0]}]', end='')\n",
        "print()\n",
        "print(f'O menor peso foi de {men}kg. Peso de ',end='')\n",
        "for p in princ:\n",
        "  if p[1] == men:\n",
        "    print(f'[{p[0]}]', end='')\n",
        "print()"
      ],
      "metadata": {
        "id": "tsO1R2ZfNlIV"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 85 - soma de impar e par\n",
        "total = list()\n",
        "par = list()\n",
        "impar = list()\n",
        "\n",
        "\n",
        "for c in range(0,7):\n",
        "  total.append(int(input('Digite um número: ')))\n",
        "  total.sort()\n",
        "\n",
        "for n in range(0,7):\n",
        "  if total[n] % 2 == 0:\n",
        "    par.append(total[n])\n",
        "  else:\n",
        "    impar.append(total[n])\n",
        "\n",
        "print(f'Os número pares digitados foram: {par}')\n",
        "print(f'Os números impares digitados foram: {impar}')"
      ],
      "metadata": {
        "id": "LY_2Fy8acEpG"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#DESAFIO 85 - soma de impar e par\n",
        "total = [[],[]]\n",
        "for c in range(0,7):\n",
        "  num = int(input('digite o número: '))\n",
        "  if num % 2 == 0:\n",
        "    total[0].append(num)\n",
        "  else:\n",
        "    total[1].append(num)\n",
        "  \n",
        "total[0].sort()\n",
        "total[1].sort()\n",
        "print(f'Os número pares digitados foram: {total[0]}')\n",
        "print(f'Os números impares digitados foram: {total[1]}')"
      ],
      "metadata": {
        "id": "uG-RvYGefi5Z"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#DESAFIO 86 - matriz\n",
        "\n",
        "matriz = [[0,0,0], [0,0,0], [0,0,0]]\n",
        "for l in range(0, 3):\n",
        "  for c in range(0, 3):\n",
        "    matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))\n",
        "\n",
        "print('-='*30)\n",
        "for l in range(0,3):\n",
        "  for c in range(0, 3):\n",
        "    print(f'[{matriz[l][c]:^5}]', end='')\n",
        "  print()"
      ],
      "metadata": {
        "id": "MmmCN63ykFFD"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#DESAFIO 87 - matriz\n",
        "\n",
        "matriz = [[0,0,0], [0,0,0], [0,0,0]]\n",
        "spar = mai = scol = 0\n",
        "#codigo para formar a matriz\n",
        "for l in range(0, 3):\n",
        "  for c in range(0, 3):\n",
        "    matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))\n",
        "#codigo para formatar a matriz na tela\n",
        "print('-='*30)\n",
        "for l in range(0,3):\n",
        "  for c in range(0, 3):\n",
        "    print(f'[{matriz[l][c]:^5}]', end='')\n",
        "    if matriz[l][c] % 2 == 0:\n",
        "      spar += matriz[l][c]\n",
        "  print()\n",
        "print('-='*30)\n",
        "print(f'a soma dos valores pares é: {spar}')\n",
        "for l in range(0, 3):\n",
        "  scol += matriz[l][2]\n",
        "print(f'a soma da terceira coluna é: {scol}')\n",
        "for c in range(0 ,3):\n",
        "  if c == 0:\n",
        "    mai = matriz[1][c]\n",
        "  elif matriz[1][c] > mai:\n",
        "    mai =matriz[1][c]\n",
        "print(f'O maior valor da segunda linha é: {mai}')"
      ],
      "metadata": {
        "id": "wM9Iw-DEEy82"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#DESAFIO 88 - jogos da mega-sena\n",
        "import random\n",
        "from time import sleep\n",
        "mega = list()\n",
        "jogos = list()\n",
        "print('-'*30)\n",
        "print('     JOGO DA MEGA SENA     ')\n",
        "print('-'*30)\n",
        "quantidade = int(input('Quantos jogos você quer? '))\n",
        "total = 1\n",
        "while total <= quantidade:\n",
        "  c = 0\n",
        "  while True:\n",
        "    num = random.randint(1, 60)\n",
        "    if num not in mega:\n",
        "      mega.append(num)\n",
        "      c += 1\n",
        "    if c >= 6:\n",
        "      break\n",
        "  mega.sort()\n",
        "  jogos.append(mega[:])\n",
        "  mega.clear()\n",
        "  total += 1\n",
        "print()\n",
        "print('-='*4, 'JOGOS GERADOS', '-='*4)\n",
        "for i, l in enumerate(jogos):\n",
        "  print(f'Jogo {i+1}: {l}')\n",
        "  sleep(1)\n",
        "print('-='*5, 'BOA SORTE!', '-='*5)"
      ],
      "metadata": {
        "id": "KgJsswavGmH6"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#jogo do bicho\n",
        "import random\n",
        "from time import sleep\n",
        "mega = list()\n",
        "jogos = list()\n",
        "print('-'*30)\n",
        "print('     JOGO DO BICHO     ')\n",
        "print('-'*30)\n",
        "quantidade = int(input('Quantos jogos você quer? '))\n",
        "total = 1\n",
        "while total <= quantidade:\n",
        "  c = 0\n",
        "  while True:\n",
        "    num = random.randint(1, 99)\n",
        "    if num not in mega:\n",
        "      mega.append(num)\n",
        "      c += 1\n",
        "    if c >= 3:\n",
        "      break\n",
        "  mega.sort()\n",
        "  jogos.append(mega[:])\n",
        "  mega.clear()\n",
        "  total += 1\n",
        "print()\n",
        "print('-='*4, 'JOGOS GERADOS', '-='*4)\n",
        "for i, l in enumerate(jogos):\n",
        "  print(f'Jogo {i+1}: {l}')\n",
        "  sleep(1)\n",
        "print('-='*5, 'BOA SORTE!', '-='*5)"
      ],
      "metadata": {
        "id": "Ah_jXv8_Lgvn"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 89\n",
        "notas = list()\n",
        "\n",
        "while True:\n",
        "  aluno = str(input('Aluno: '))\n",
        "  n1 = float(input('Nota 1: '))\n",
        "  n2 = float(input('Nota 2: '))\n",
        "  media = (n1 + n2)/2\n",
        "  notas.append([aluno, [n1, n2], media])\n",
        "  cont = str(input('Deseja continuar? [s/n] '))\n",
        "  if cont in 'Nn':\n",
        "    break\n",
        "\n",
        "print('-='*30)\n",
        "print(f'{\"No.\":<4}{\"NOME\":<10}{\"MÉDIA\":>8}')\n",
        "print('-'*26)\n",
        "\n",
        "for i, a in enumerate(notas):\n",
        "  print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')\n",
        "while True:\n",
        "  print('-'*35)\n",
        "  opc  = int(input('Mostrar notas de qual aluno? (999 interrompe): '))\n",
        "  if opc == 999:\n",
        "    break\n",
        "  if opc <= len(notas) - 1:\n",
        "    print(f'Notas de {notas[opc][0]} são {notas[opc][1]}: ')\n",
        "print('FINALIZADO')"
      ],
      "metadata": {
        "id": "B-feWSdTLyzP"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#aula 19\n",
        "dados = dict()\n",
        "dados = {'nome':'Pedro', 'idade':'25'}\n",
        "dados['sexo']='M'\n",
        "del dados['idade']\n",
        "\n",
        "print(dados)\n",
        "\n",
        "\n",
        "valorant = {'Duelista':'Reyna', 'Controlador':'Cypher','Sentinela':'Viper', 'Iniciador':'Fade'}\n",
        "print(valorant.keys())\n",
        "print(valorant.values())\n",
        "print(valorant.items())\n",
        "\n",
        "for p,d in valorant.items():\n",
        "  print(f'A personagem {d} é {p}')\n"
      ],
      "metadata": {
        "id": "jXa3AhSO3oCT"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "brasil = list()\n",
        "Estado1 = {'Estado':'Rio de Janeiro', 'Capital':'Rio de Janeiro', 'Região':'Sudeste'}\n",
        "Estado2 = {'Estado':'São Paulo', 'Capital':'São Paulo', 'Região':'Sudeste'}\n",
        "Estado3 = {'Estado':'Bahia','Capital':'Salvador','Região':'Nordeste'}\n",
        "Estado4 = {'Estado':'Amazonas','Capital':'Manaus','Região':'Norte'}\n",
        "brasil.append(Estado1)\n",
        "brasil.append(Estado2)\n",
        "brasil.append(Estado3)\n",
        "brasil.append(Estado4)\n",
        "print(brasil)"
      ],
      "metadata": {
        "id": "VegQ4lRZ5XgF"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "players = dict()\n",
        "lista = list()\n",
        "\n",
        "for c in range (0, 3):\n",
        "  players['nickname'] = str(input('Nickname: '))\n",
        "  players['elo'] = str(input('Rank: '))\n",
        "  lista.append(players.copy())\n",
        "\n",
        "for c in lista:\n",
        "  for k, v in c.items():\n",
        "    print(f'{k}: {v}  ', end=' ')\n",
        "  print()\n"
      ],
      "metadata": {
        "id": "mxwQVTE--hSC"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 90\n",
        "\n",
        "aluno = dict()\n",
        "\n",
        "aluno['Nome'] = str(input('Nome do Aluno: '))\n",
        "aluno['Media'] = float(input(f'Média do aluno {aluno[\"Nome\"]}: '))\n",
        "if aluno['Media'] >= 7.0:\n",
        "  aluno['Resultado'] = 'Aprovado'\n",
        "elif 4.0 <= aluno['Media'] < 7.0:\n",
        "  aluno['Resultado'] = 'Prova final'\n",
        "else:\n",
        "  aluno['Resultado'] = 'Reprovado'\n",
        "\n",
        "print('-'*30)\n",
        "print(f'Aluno: {aluno[\"Nome\"]}')\n",
        "print(f'Média: {aluno[\"Media\"]}'),\n",
        "print(f'Situação: {aluno[\"Resultado\"]}')"
      ],
      "metadata": {
        "id": "yUMP1hPEQdSt"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 91\n",
        "from random import randint\n",
        "from time import sleep\n",
        "from operator import itemgetter\n",
        "\n",
        "jogo  = {'Jogador 1': randint(1,6),\n",
        "         'Jogador 2': randint(1,6),\n",
        "         'Jogador 3': randint(1,6),\n",
        "         'Jogador 4': randint(1,6),}\n",
        "ranking = list()\n",
        "        \n",
        "print('Valores Sorteados: ')\n",
        "print()\n",
        "for k, v in jogo.items():\n",
        "  print(f'O {k} tirou {v} no dado')\n",
        "  sleep(1)\n",
        "print()\n",
        "print('-='*20)\n",
        "print(' == RANKING DOS JOGADORES ==')\n",
        "print()\n",
        "ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)\n",
        "for i, v in enumerate(ranking):\n",
        "  print(f'{i+1}º Lugar: {v[0]} com {v[1]}')\n",
        "  sleep(1)"
      ],
      "metadata": {
        "id": "4QI7Pvul585a"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 92\n",
        "\n",
        "cadastro = dict()\n",
        "\n",
        "cadastro['Nome'] = str(input('Nome: '))\n",
        "cadastro['Ano'] = int(input('Ano de Nascimento: '))\n",
        "cadastro['CTPS'] = int(input('CTPS (0 caso não tenha): '))\n",
        "if cadastro['CTPS'] != 0:\n",
        "  cadastro['Contratacao'] = int(input('Ano de contratação: '))\n",
        "  cadastro['Salario'] = float(input('Salário: R$'))\n",
        "  cadastro['Aposentadoria'] = int(cadastro['Contratacao'] - cadastro['Ano'] + 35)\n",
        "\n",
        "print('-='*30)\n",
        "for k, v in cadastro.items():\n",
        "  print(f'{k} tem o valor de {v}')"
      ],
      "metadata": {
        "id": "j4HqvHruSG1O"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 93\n",
        "\n",
        "jogador = dict()\n",
        "partidas = list()\n",
        "\n",
        "jogador['nome'] = str(input('Nome do Jogador: '))\n",
        "tot = int(input(f'Quantas partidas {jogador[\"nome\"]} jogou? '))\n",
        "for c in range(0, tot):\n",
        "  partidas.append(int(input(f'Quantos gols na partida {c+1}: ')))\n",
        "jogador['gols'] = partidas[:]\n",
        "jogador['total'] = sum(partidas)\n",
        "\n",
        "for k,v in jogador.items():\n",
        "  print(f'O campo {k} em o valor {v}')\n",
        "\n",
        "print(jogador)\n",
        "\n",
        "print('-='*30)\n",
        "print(f'O jogador {jogador[\"nome\"]} jogou {tot} partidas.')\n",
        "for i,a in enumerate(jogador['gols']):\n",
        "  print(f' --- na partida {i+1}, fez {a} gols.')\n",
        "print(f'No total ele marcou {jogador[\"total\"]} gols.')"
      ],
      "metadata": {
        "id": "V2Ddxo3PemXv"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#desafio 94\n",
        "\n",
        "pessoa = dict()\n",
        "lista = list()\n",
        "media = list()\n",
        "mulheres = list()\n",
        "aaaa = list()\n",
        "num = 1\n",
        "\n",
        "while True:\n",
        "  pessoa['nome'] = str(input('Nome: '))\n",
        "  while True:\n",
        "    pessoa['sexo'] = str(input('Sexo: [m/f] '))\n",
        "    if pessoa['sexo'] not in 'MmFf':\n",
        "      print('ERROR, porfavor digite apenas m ou f')\n",
        "    if pessoa['sexo'] == 'f':\n",
        "      mulheres.append(pessoa['nome'])\n",
        "    if pessoa['sexo'] in 'MmFf':\n",
        "      break\n",
        "  pessoa['idade'] = int(input('Idade: '))\n",
        "  media.append(pessoa['idade'])\n",
        "  lista.append(pessoa.copy())\n",
        "  cont = str(input('Deseja continuar? [s/n] '))\n",
        "  if cont in 'Ss':\n",
        "    num += 1\n",
        "  elif cont in 'Nn':\n",
        "    break\n",
        "  else: \n",
        "    print('ERROR')\n",
        "    break\n",
        "print(f'{num} pessoas se cadastraram.')\n",
        "meedia = (float(sum(media)/num))\n",
        "print(f'A média das idades cadastradas é: {meedia}')\n",
        "print(f'Mulheres cadastradas: {mulheres}')\n"
      ],
      "metadata": {
        "id": "sbAQslD8nDm9"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "#resolução guanabara desafio 94\n",
        "\n",
        "galera = list()\n",
        "pessoa = dict()\n",
        "soma = média = 0\n",
        "while True:\n",
        "  pessoa.clear()\n",
        "  pessoa['nome'] = str(input('Nome: '))\n",
        "  while True:\n",
        "    pessoa['sexo'] = str(input('Sexo: ')).upper() [0]\n",
        "    if pessoa['sexo'] in 'MF':\n",
        "      break\n",
        "    print('ERROR! Digite somente M ou F.')\n",
        "  pessoa['idade'] = int(input('Idade: '))\n",
        "  soma += pessoa['idade']\n",
        "  galera.append(pessoa.copy())\n",
        "  while True:\n",
        "    resp = str(input('Deseja continuar? [s/n] ')).upper() [0]\n",
        "    if resp in 'SN':\n",
        "      break\n",
        "    print('ERROR! Digite apenas S ou N.')\n",
        "  if resp == 'N':\n",
        "    break\n",
        "print('-='*30)\n",
        "print(f'A) Ao todo {len(galera)} pessoas cadastradas.')\n",
        "média = soma / len(galera)\n",
        "print(f'B) A média de idade é de {média:5.2f} anos')\n",
        "print(f'C) As mulheres cadastradas foram ', end='')\n",
        "for p in galera:\n",
        "  if p['sexo'] in 'Ff':\n",
        "    print(f'{p[\"nome\"]}', end=' ')\n",
        "print()\n",
        "print('D) Lista das pessoas que estão acima de média: ')\n",
        "for p in galera:\n",
        "  if p['idade'] >= média:\n",
        "    print('   ')\n",
        "    for k,v in p.items():\n",
        "      print(f'{k} = {v}', end=' ')\n",
        "    print()\n",
        "print('<< ENCERRADO >>')\n"
      ],
      "metadata": {
        "id": "pLJQH8T3-4hQ"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "\n",
        "#desafio 95\n",
        "\n",
        "time = list()\n",
        "jogador = dict()\n",
        "partidas = list()\n",
        "\n",
        "while True:\n",
        "  jogador.clear()\n",
        "  jogador['nome'] = str(input('Nome do Jogador: '))\n",
        "  tot = int(input(f'Quantas partidas {jogador[\"nome\"]} jogou? '))\n",
        "  partidas.clear()\n",
        "  for c in range(0, tot):\n",
        "    partidas.append(int(input(f'      Quantos gols na partida {c}? ')))\n",
        "  jogador['gols'] = partidas[:]\n",
        "  jogador['total'] = sum(partidas)\n",
        "  time.append(jogador.copy())\n",
        "  while True:\n",
        "    resp = str(input('Deseja continuar [s/n]? ')).upper() [0]\n",
        "    if resp in 'SN':\n",
        "      break\n",
        "    print('ERRO! Responda apenas S ou N.')\n",
        "  if resp == 'N':\n",
        "    break\n",
        "print('-='*30)\n",
        "print('cod ', end='')\n",
        "for i in jogador.keys():\n",
        "  print(f'{i:<15}', end='')\n",
        "print()\n",
        "print('-'*40)\n",
        "for k, v in enumerate(time):\n",
        "  print(f'{k:>3} ', end='')\n",
        "  for d in v.values():\n",
        "    print(f'{str(d):<15}', end='')\n",
        "  print()\n",
        "print('-'*40)\n",
        "while True:\n",
        "  busca = int(input('Mostrar dados de qual jogador? '))\n",
        "  if busca == 999:\n",
        "    break\n",
        "  if busca >= len(time):\n",
        "    print(f'Error! não existe jogador com o código {busca}')\n",
        "  else:\n",
        "    print(f'-- LEVANTAMENTO DOS DADOS DO JOGADOR {time[busca][\"nome\"]}:')\n",
        "    for i, g in enumerate(time[busca]['gols']):\n",
        "      print(f'    No jogo {i+1} fez {g} gols.')\n",
        "print('-'*40)\n",
        "print('VOLTE SEMPRE!')"
      ],
      "metadata": {
        "id": "66SAkpBc-7y6"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}