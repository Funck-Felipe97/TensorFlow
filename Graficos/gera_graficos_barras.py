# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:10:00 2019

@author: funck
"""

import xlrd
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

faixaPorcentagem = ['0-14', '15-29', '30-44', '45-59', '60-74', '75-89', '90-100']
vetor_geral_ferrugem = [0, 0, 0, 0, 0, 0, 0]
vetor_geral_saudavel = [0, 0, 0, 0, 0, 0, 0]

def plotGrafico(titulo, dados):
    plt.bar(faixaPorcentagem, dados, color='red')
    plt.xticks(faixaPorcentagem)
    plt.xlabel('Porcentagem mínima e máxima de chances da folha estar com ferrugem')
    plt.ylabel('Quantidade de folhas')
    plt.title(titulo)
    
def plotGraficoGeral(dados_ferrugem, dados_saudaveis):
    
    #Definindo largura das barras
    barWidth = 0.30
    
    #Aumentando o gráfico
    plt.figure(figsize=(10,5))
    
    #Definindo a posição das barras
    r1 = np.arange(len(dados_ferrugem))
    r2 = [x + barWidth for x in r1]
    
    #Criando barras
    plt.bar(r1, dados_ferrugem, color='red', width=barWidth, label='Folhas com ferrugem')
    plt.bar(r2, dados_saudaveis, color='blue', width=barWidth, label='Folhas sem  ferrugem')
    
    #Adicionando legendas as barras
    plt.xlabel('Intervalos mínimos e máximos de confiança')
    plt.xticks([r + barWidth for r in range(len(faixaPorcentagem))], faixaPorcentagem)
    plt.ylabel('Classificação realizada')
    
    #Criando a legenda e exibindo o gráfico
    plt.legend()
    plt.title('Gráfico geral com as classificações realizadas')
    ##plt.savefig('grefico_barras_geral.png')
    plt.show()
    
def gerarGraficoFerrugem():

    planilha = xlrd.open_workbook(r"C:\Users\funck\Desktop\Documentos\UTFPR\Semestre8\TCC2\resultados\resultados_ferrugem.xlsx","r")
    
    sh = planilha.sheet_by_index(0)
    
    vetor_ferrugem = [0, 0, 0, 0, 0, 0, 0]
    
    for linha in range(1, sh.nrows):
        valor = (sh.cell_value(rowx=linha, colx=1) + sh.cell_value(rowx=linha, colx=2)) / 2
        if valor >= 90:
            vetor_ferrugem[6] = vetor_ferrugem[6] + 1
            vetor_geral_ferrugem[6] = vetor_geral_ferrugem[6] + 1
        elif valor >= 75:
            vetor_ferrugem[5] = vetor_ferrugem[5] + 1
            vetor_geral_ferrugem[5] = vetor_geral_ferrugem[5] + 1
        elif valor >= 60:
            vetor_ferrugem[4] = vetor_ferrugem[4] + 1
            vetor_geral_ferrugem[4] = vetor_geral_ferrugem[4] + 1
        elif valor >= 45:
            vetor_ferrugem[3] = vetor_ferrugem[3] + 1
            vetor_geral_ferrugem[3] = vetor_geral_ferrugem[3] + 1
        elif valor >= 35:
            vetor_ferrugem[2] = vetor_ferrugem[2] + 1
            vetor_geral_ferrugem[2] = vetor_geral_ferrugem[2] + 1
        elif valor >= 15:
            vetor_ferrugem[1] = vetor_ferrugem[1] + 1
            vetor_geral_ferrugem[1] = vetor_geral_ferrugem[1] + 1
        elif valor >= 0: 
            vetor_ferrugem[0] = vetor_ferrugem[0] + 1
            vetor_geral_ferrugem[0] = vetor_geral_ferrugem[0] + 1
        
        plotGrafico('Classificações de folhas com ferrugem', vetor_ferrugem)
        
def gerarGraficoSaudaveis():

    planilha = xlrd.open_workbook(r"C:\Users\funck\Desktop\Documentos\UTFPR\Semestre8\TCC2\resultados\resultado_saudaveis.xlsx","r")
    
    sh = planilha.sheet_by_index(0)
    
    vetor_saudaveis = [0, 0, 0, 0, 0, 0, 0]
    
    for linha in range(1, sh.nrows):
        valor = (sh.cell_value(rowx=linha, colx=1) + sh.cell_value(rowx=linha, colx=2)) / 2
        if valor >= 90:
            vetor_saudaveis[6] = vetor_saudaveis[6] + 1
            vetor_geral_saudavel[6] = vetor_geral_saudavel[6] + 1
        elif valor >= 75:
            vetor_saudaveis[5] = vetor_saudaveis[5] + 1
            vetor_geral_saudavel[5] = vetor_geral_saudavel[5] + 1
        elif valor >= 60:
            vetor_saudaveis[4] = vetor_saudaveis[4] + 1
            vetor_geral_saudavel[4] = vetor_geral_saudavel[4] + 1
        elif valor >= 45:
            vetor_saudaveis[3] = vetor_saudaveis[3] + 1
            vetor_geral_saudavel[3] = vetor_geral_saudavel[3] + 1
        elif valor >= 35:
            vetor_saudaveis[2] = vetor_saudaveis[2] + 1
            vetor_geral_saudavel[2] = vetor_geral_saudavel[2] + 1
        elif valor >= 15:
            vetor_saudaveis[1] = vetor_saudaveis[1] + 1
            vetor_geral_saudavel[1] = vetor_geral_saudavel[1] + 1
        elif valor >= 0: 
            vetor_saudaveis[0] = vetor_saudaveis[0] + 1
            vetor_geral_saudavel[0] = vetor_geral_saudavel[0] + 1
        
        plotGrafico('Classificações de folhas saudáveis', vetor_saudaveis)
        
def gerarGraficoOutros():

    planilha = xlrd.open_workbook(r"C:\Users\funck\Desktop\Documentos\UTFPR\Semestre8\TCC2\resultados\resultados_outros.xlsx","r")
    
    sh = planilha.sheet_by_index(0)
    
    vetor_outros = [0, 0, 0, 0, 0, 0, 0]
    
    for linha in range(1, sh.nrows):
        valor = (sh.cell_value(rowx=linha, colx=1) + sh.cell_value(rowx=linha, colx=2)) / 2
        if valor >= 90:
            vetor_outros[6] = vetor_outros[6] + 1
            vetor_geral_saudavel[6] = vetor_geral_saudavel[6] + 1
        elif valor >= 75:
            vetor_outros[5] = vetor_outros[5] + 1
            vetor_geral_saudavel[5] = vetor_geral_saudavel[5] + 1
        elif valor >= 60:
            vetor_outros[4] = vetor_outros[4] + 1
            vetor_geral_saudavel[4] = vetor_geral_saudavel[4] + 1
        elif valor >= 45:
            vetor_outros[3] = vetor_outros[3] + 1
            vetor_geral_saudavel[3] = vetor_geral_saudavel[3] + 1
        elif valor >= 35:
            vetor_outros[2] = vetor_outros[2] + 1
            vetor_geral_saudavel[2] = vetor_geral_saudavel[2] + 1
        elif valor >= 15:
            vetor_outros[1] = vetor_outros[1] + 1
            vetor_geral_saudavel[1] = vetor_geral_saudavel[1] + 1
        elif valor >= 0: 
            vetor_outros[0] = vetor_outros[0] + 1
            vetor_geral_saudavel[0] = vetor_geral_saudavel[0] + 1
        
        plotGrafico('Classificações de folhas com manchas não identificadas', vetor_outros)
        

def gerarGraficoManchaParda():

    planilha = xlrd.open_workbook(r"C:\Users\funck\Desktop\Documentos\UTFPR\Semestre8\TCC2\resultados\resultado_mancha_parda.xlsx","r")
    
    sh = planilha.sheet_by_index(0)
    
    vetor_mancha_parda = [0, 0, 0, 0, 0, 0, 0]
    
    for linha in range(1, sh.nrows):
        valor = (sh.cell_value(rowx=linha, colx=1) + sh.cell_value(rowx=linha, colx=2)) / 2
        if valor >= 90:
            vetor_mancha_parda[6] = vetor_mancha_parda[6] + 1
            vetor_geral_saudavel[6] = vetor_geral_saudavel[6] + 1
        elif valor >= 75:
            vetor_mancha_parda[5] = vetor_mancha_parda[5] + 1
            vetor_geral_saudavel[5] = vetor_geral_saudavel[5] + 1
        elif valor >= 60:
            vetor_mancha_parda[4] = vetor_mancha_parda[4] + 1
            vetor_geral_saudavel[4] = vetor_geral_saudavel[4] + 1
        elif valor >= 45:
            vetor_mancha_parda[3] = vetor_mancha_parda[3] + 1
            vetor_geral_saudavel[3] = vetor_geral_saudavel[3] + 1
        elif valor >= 35:
            vetor_mancha_parda[2] = vetor_mancha_parda[2] + 1
            vetor_geral_saudavel[2] = vetor_geral_saudavel[2] + 1
        elif valor >= 15:
            vetor_mancha_parda[1] = vetor_mancha_parda[1] + 1
            vetor_geral_saudavel[1] = vetor_geral_saudavel[1] + 1
        elif valor >= 0: 
            vetor_mancha_parda[0] = vetor_mancha_parda[0] + 1
            vetor_geral_saudavel[0] = vetor_geral_saudavel[0] + 1
        
        plotGrafico('Classificações de folhas com mancha parda', vetor_mancha_parda)
        
def gerarGraficoOlhoRa():

    planilha = xlrd.open_workbook(r"C:\Users\funck\Desktop\Documentos\UTFPR\Semestre8\TCC2\resultados\resultados_olho_ra.xlsx","r")
    
    sh = planilha.sheet_by_index(0)
    
    vetor_olho_ra = [0, 0, 0, 0, 0, 0, 0]
    
    for linha in range(1, sh.nrows):
        valor = (sh.cell_value(rowx=linha, colx=1) + sh.cell_value(rowx=linha, colx=2)) / 2
        if valor >= 90:
            vetor_olho_ra[6] = vetor_olho_ra[6] + 1
            vetor_geral_saudavel[6] = vetor_geral_saudavel[6] + 1
        elif valor >= 75:
            vetor_olho_ra[5] = vetor_olho_ra[5] + 1
            vetor_geral_saudavel[5] = vetor_geral_saudavel[5] + 1
        elif valor >= 60:
            vetor_olho_ra[4] = vetor_olho_ra[4] + 1
            vetor_geral_saudavel[4] = vetor_geral_saudavel[4] + 1
        elif valor >= 45:
            vetor_olho_ra[3] = vetor_olho_ra[3] + 1
            vetor_geral_saudavel[3] = vetor_geral_saudavel[3] + 1
        elif valor >= 35:
            vetor_olho_ra[2] = vetor_olho_ra[2] + 1
            vetor_geral_saudavel[2] = vetor_geral_saudavel[2] + 1
        elif valor >= 15:
            vetor_olho_ra[1] = vetor_olho_ra[1] + 1
            vetor_geral_saudavel[1] = vetor_geral_saudavel[1] + 1
        elif valor >= 0: 
            vetor_olho_ra[0] = vetor_olho_ra[0] + 1
            vetor_geral_saudavel[0] = vetor_geral_saudavel[0] + 1
        
        plotGrafico('Classificações de folhas com olho de rã', vetor_olho_ra)
        
def gerarGraficoOidioSoja():

    planilha = xlrd.open_workbook(r"C:\Users\funck\Desktop\Documentos\UTFPR\Semestre8\TCC2\resultados\resultado_oidio_soja.xlsx","r")
    
    sh = planilha.sheet_by_index(0)
    
    vetor_oidio_soja = [0, 0, 0, 0, 0, 0, 0]
    
    for linha in range(1, sh.nrows):
        valor = (sh.cell_value(rowx=linha, colx=1) + sh.cell_value(rowx=linha, colx=2)) / 2
        if valor >= 90:
            vetor_oidio_soja[6] = vetor_oidio_soja[6] + 1
            vetor_geral_saudavel[6] = vetor_geral_saudavel[6] + 1
        elif valor >= 75:
            vetor_oidio_soja[5] = vetor_oidio_soja[5] + 1
            vetor_geral_saudavel[5] = vetor_geral_saudavel[5] + 1
        elif valor >= 60:
            vetor_oidio_soja[4] = vetor_oidio_soja[4] + 1
            vetor_geral_saudavel[4] = vetor_geral_saudavel[4] + 1
        elif valor >= 45:
            vetor_oidio_soja[3] = vetor_oidio_soja[3] + 1
            vetor_geral_saudavel[3] = vetor_geral_saudavel[3] + 1
        elif valor >= 35:
            vetor_oidio_soja[2] = vetor_oidio_soja[2] + 1
            vetor_geral_saudavel[2] = vetor_geral_saudavel[2] + 1
        elif valor >= 15:
            vetor_oidio_soja[1] = vetor_oidio_soja[1] + 1
            vetor_geral_saudavel[1] = vetor_geral_saudavel[1] + 1
        elif valor >= 0: 
            vetor_oidio_soja[0] = vetor_oidio_soja[0] + 1
            vetor_geral_saudavel[0] = vetor_geral_saudavel[0] + 1
        
        plotGrafico('Classificações de folhas com oídio da soja', vetor_oidio_soja)
        
        
gerarGraficoFerrugem()
gerarGraficoManchaParda()
gerarGraficoOidioSoja()
gerarGraficoOlhoRa()
gerarGraficoSaudaveis()
gerarGraficoOutros()
plotGraficoGeral(vetor_geral_ferrugem, vetor_geral_saudavel)



