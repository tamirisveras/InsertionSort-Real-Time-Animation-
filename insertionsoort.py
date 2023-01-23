import streamlit as s
from random import randrange
import time
 
 
def random():
    lista = []
    for i in range(randrange(5, 15)):  # Sortear o tamanho da lista
        aux = randrange(1, 50)  # Sortear os valores da lista
        lista.append(aux)
 
    return lista
 
 
with s.sidebar:
    s.title('InsertionSort :rocket:')
    criar_lista = s.text_input('Insira a sua lista: ')
    ordenar = s.button('Ordenar')
    
    ordenado = s.radio('Ordenado:', 
    ['Aleatório', 
    'Crescente', 
    'Decrescente'], 
    horizontal=False)
 
    
    botao_lista_aleatoria = s.button("Sortear valores")
 
if criar_lista:
 
    lista = list(map(int, criar_lista.split(',')))
    aux = []
 
    for i in lista:
        aux.append(i)
 
    lista = aux
 
elif ordenado == "Aleatório":
    lista = random()
 
#  Verifica se foi selecionado a opção "Crescente", se estiver, ele ordena a lista aleatória gerada
elif ordenado == "Crescente":
    lista = random()
    lista.sort(reverse=False)
 
#  Verifica se foi selecionado a opção "Decrescente", se estiver, ele ordena a lista aleatória gerada
elif ordenado == "Decrescente":
    lista = random()
    lista.sort(reverse=True)
 
#  Sempre que o botão for acionado, ele entregara uma nova lista randômica
if botao_lista_aleatoria:
    criar_lista = random()
 
#  Cria um gráfico de barra com base na lista informada
grafico = s.bar_chart(
    data=lista,
    height=500,
    use_container_width=True
)
 
#  tempo = 2
 
 
def insertion_sort(lista):
 
    n = len(lista)
    
    for i in range(1, n):
        posicaoatual = lista[i]
        ordenados = posicaoatual - 1
 
        if ordenar == True:
            while ordenados > 0 and lista[ordenados] > posicaoatual:
                lista[ordenados+1] = lista[ordenados]
                ordenados = ordenados - 1
 
            lista[ordenados+1] = posicaoatual
 
            grafico = s.bar_chart(lista)
            time.sleep(8)
            grafico.empty()
 
 
if ordenar:
 
    for i in range(1, len(lista)):
        while lista[i-1] > lista[i] and i > 0:
            lista[i-1], lista[i] = lista[i], lista[i-1]
            i -= 1
            grafico.empty()
            grafico = s.bar_chart(lista)
            time.sleep(8)