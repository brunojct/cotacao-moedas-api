import tkinter as tk
from tkinter import ttk
from tkcalendar import DateEntry
import requests
from datetime import datetime
from tkinter.filedialog import askopenfilename
import pandas as pd

# CONSUMO DA API DE COTAÇÕES DE MOEDAS E CRIAÇÃO DAS FUNÇÕES

# criando uma lista com o nome de todas as moedas disponíveis
requisicao = requests.get('https://economia.awesomeapi.com.br/all')
dicionario_moedas = requisicao.json()
lista_moedas = list(dicionario_moedas.keys())

# algumas variáveis que serão utilizadas no programa
nome_moeda = ''
lista_dias = []
dicionario_cotacoes = {}
dicionario_final = {}

#função para pegar a cotaçao de uma única moeda para um único dia
def pegar_cotacao():
    data = data_unicodia.get()
    data_covertida = datetime.strptime(data, '%d/%m/%Y')
    data_covertida = datetime.strftime(data_covertida, '%Y%m%d')
    moeda_unica = combobox_umamoeda.get()
    requisitar_cotacao_unica = requests.get(f'https://economia.awesomeapi.com.br/json/daily/{moeda_unica}-BRL?start_date={data_covertida}&end_date={data_covertida}')
    dicionario_requisicao = (requisitar_cotacao_unica.json())
    if dicionario_requisicao == []:
        label_resposta_cotacao['text'] = 'Cotação indisponível para essa data'
    else:
        valor_moeda = float(dicionario_requisicao[0]['bid'])
        texto_valor_moeda = f'Cotação do {combobox_umamoeda.get()} no dia {data_unicodia.get()}: R$ {valor_moeda:.2f}'
        label_resposta_cotacao['text'] = texto_valor_moeda

#função para selecionar o arquivo em excel para pegar a cotação de múltiplas moedas
def selecionar_arquivo():
    caminho_arquivo = askopenfilename(title='Selecione o arquivo em Excel')
    var_caminhoarquivo.set(caminho_arquivo)
    lista_caminho_arquivo = caminho_arquivo.split('/')
    nome_arquivo = lista_caminho_arquivo[-1]
    if nome_arquivo:
        label_arquivo_selecionado['text'] = f'{nome_arquivo} selecionado com sucesso.'

#função que executa todo o processo de buscar as multiplas cotações e criar um arquivo excel com os valores
def buscar_multiplas_cotacoes():
    #abrir o arquivo inicial do excel
    arquivo_nome_moedas = pd.read_excel(var_caminhoarquivo.get())
    for nome_moeda in arquivo_nome_moedas['MOEDA']:

        dicionario_cotacoes[nome_moeda] = []
        dicionario_final[nome_moeda] = []

        #pegando todas as datas dentro do intervalo de datas escolhido pela pessoa
        data_inicial = selecionar_datainicial.get()
        data_inicial = datetime.strptime(data_inicial, '%d/%m/%Y')
        data_final = selecionar_datafinal.get()
        data_final = datetime.strptime(data_final, '%d/%m/%Y')
        range_datas = pd.date_range(start = data_inicial, end = data_final)

        #buscando a cotação em cada data do intervalo selecionado (pois a API não busca todo o intervalo somente de uma vez de forma eficaz)
        for data in range_datas:
            link = requests.get(f'https://economia.awesomeapi.com.br/'
                                f'json/daily/{nome_moeda}-BRL?start_date={data.year}{data.month:02d}{data.day:02d}'
                                f'&end_date={data.year}{data.month:02d}{data.day:02d}')
            dicionario_requisicao = link.json()
            dicionario_cotacoes[nome_moeda].append(dicionario_requisicao)

        #preenchendo o dicionário com o nome da moeda e todas as cotações do intervalo desejado
        for i in range (len(range_datas)):
            preco = float(dicionario_cotacoes[nome_moeda][i][0]["bid"])
            dicionario_final[nome_moeda].append(f'{preco:.2f}')
    #criando uma lista com todas as datas dentro do intervalo
    for i in range(len(range_datas)):
        dia = f'{range_datas[i]:%d/%m/%Y}'
        lista_dias.append(dia)

    #criando o dataframe a partir do dicionário com o nome da moeda e suas cotações
    dataframe = pd.DataFrame.from_dict(dicionario_final)
    #adicionando as datas a partir da lista que foi criada anteriormente
    dataframe['Data']=lista_dias
    dataframe = dataframe.set_index('Data')
    #salvando o arquivo excel e avisando o usuário que o arquivo já foi gerado
    dataframe.to_excel('Cotacao.xlsx')
    label_resposta_cotacaomultipla['text'] = 'Arquivo gerado com sucesso.'


# CRIAÇÃO DO PROGRAMA

#criação da janela
janela = tk.Tk()
janela.title('Sistema de Cotações')

#cotação de uma moeda específica
label_cotacao_umamoeda = tk.Label(text='Cotação de 1 moeda específica', borderwidth=2, relief='solid')
label_cotacao_umamoeda.grid(row=0, column=0, columnspan=3, sticky='NSEW', pady=10, padx=10)

label_selecao_umamoeda = tk.Label(text='Selecione a moeda que deseja consultar')
label_selecao_umamoeda.grid(row=1, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10)

combobox_umamoeda = ttk.Combobox(values=lista_moedas)
combobox_umamoeda.grid(row=1, column=2, sticky='NSEW', padx=10, pady=10 )

label_selecao_unicodia = tk.Label(text='Selecione o dia que deseja pegar a cotação')
label_selecao_unicodia.grid(row=2, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10)

data_unicodia = DateEntry(year=2022, locale='pt_br')
data_unicodia.grid(row=2, column=2, pady=10, padx=10, sticky='NSEW')

label_resposta_cotacao = tk.Label(text='')
label_resposta_cotacao.grid(row=3, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10)

botao_buscarunicacotacao = tk.Button(text='Buscar Cotação', command=pegar_cotacao)
botao_buscarunicacotacao.grid(row=3, column=2, pady=10, padx=10, sticky='NSEW')

#pegar multiplas cotações
label_cotacao_variasmoedas = tk.Label(text='Cotação de multiplas moedas', borderwidth=2, relief='solid')
label_cotacao_variasmoedas.grid(row=4, column=0, columnspan=3, sticky='NSEW', padx=10, pady=10)

label_selecionar_documento = tk.Label(text='Selecione um arquivo em Excel com as moedas na coluna A')
label_selecionar_documento.grid(row=5, column=0, columnspan=2, sticky='NSEW', padx=10, pady=10)

var_caminhoarquivo = tk.StringVar()
botao_selecionararquivo = tk.Button(text='Selecionar Arquivo', command =selecionar_arquivo)
botao_selecionararquivo.grid(row=5, column=2, pady=10, padx=10, sticky='NSEW')

label_arquivo_selecionado = tk.Label(text='Arquivo selecionado: Nenhum Arquivo', anchor='e')
label_arquivo_selecionado.grid(row=6, column=0, columnspan=3, sticky='NSEW', padx=10, pady=10)

label_data_inicial = tk.Label(text='Data Inicial')
label_data_inicial.grid(row=7, column=0, pady=10, padx=10, sticky='NSEW')

selecionar_datainicial = DateEntry(year=2022, locale='pt_br')
selecionar_datainicial.grid(row=7, column=1, padx=10, pady=10, sticky='NSEW')

label_data_final = tk.Label(text='Data Final')
label_data_final.grid(row=8, column=0, pady=10, padx=10, sticky='NSEW')

selecionar_datafinal = DateEntry(year=2022, locale='pt_br')
selecionar_datafinal.grid(row=8, column=1, padx=10, pady=10, sticky='NSEW')

botao_buscarvariascotacoes = tk.Button(text='Atualizar Cotações', command=buscar_multiplas_cotacoes)
botao_buscarvariascotacoes.grid(row=9, column=0, pady=10, padx=10, sticky='NSEW')

label_resposta_cotacaomultipla = tk.Label(text='')
label_resposta_cotacaomultipla.grid(row=9, column=1, columnspan=2, sticky='NSEW', padx=10, pady=10)

botao_fechar = tk.Button(text='Fechar', command=janela.quit)
botao_fechar.grid(row=10, column=2, sticky='NSEW', padx=10, pady=10)

#é necessário deixar esse comando ao final do programa para manter o programa aberto enquanto não clicarmos para fechar
janela.mainloop()