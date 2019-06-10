"""
Created on Mon May 27 11:33:37 2019
@author: funck
"""

import xlrd
import matplotlib.pyplot as plt
import numpy as np
%matplotlib inline

vetor_geral_ferrugem_x = []
vetor_geral_ferrugem_y = []
vetor_geral_outros_x = []
vetor_geral_outros_y = []

def plotGrafico(x, y, titulo, label_x, label_y, nameImage):
    plt.figure(figsize=(7,5))
    plt.plot(x, y, 'o',color = 'red')
    plt.title(titulo) 
    plt.xlabel(label_x)
    plt.ylabel(label_y)
    #plt.savefig(nameImage)
    plt.show()
    
def plotGraficoGeral(x_ferrugem, y_ferrugem, x_outros, y_outros):
    plt.figure(figsize=(7,5))
    plt.plot(x_outros, y_outros, 'o',color = 'blue', label='Folhas sem ferrugem')
    plt.plot(x_ferrugem, y_ferrugem, 'o',color = 'red', label='Folhas com ferrugem')
    plt.title('Classificações gerais de folhas com e sem ferrugem') 
    plt.xlabel('Chances míminas de ferrugem %')
    plt.ylabel('Chances máximas de ferrugem %')
    plt.legend(bbox_to_anchor=(1.0,0.16))
    plt.show()
    
    
def gerarGraficoFerrugem():

    planilha = xlrd.open_workbook(r"C:\Users\funck\Desktop\Documentos\UTFPR\Semestre8\TCC2\resultados\resultados_ferrugem.xlsx","r")
    
    sh = planilha.sheet_by_index(0)
    
    vetor_ferrugem_x = []
    vetor_ferrugem_y = []
    VP = 0
    FN = 0
    
    # Lendo porcentagem de chance da folha ter ferrugem ou ser saudavel na base de folhas com ferrugem
    for linha in range(1, sh.nrows):
        vetor_ferrugem_x.append(sh.cell_value(rowx=linha, colx=1))
        vetor_ferrugem_y.append(sh.cell_value(rowx=linha, colx=2))
        
        vetor_geral_ferrugem_x.append(sh.cell_value(rowx=linha, colx=1))
        vetor_geral_ferrugem_y.append(sh.cell_value(rowx=linha, colx=2))
        
        valor_linha = (sh.cell_value(rowx=linha, colx=1) + sh.cell_value(rowx=linha, colx=2)) / 2
        if valor_linha >= 50:
            VP = VP + 1
        else:
            FN = FN + 1
        
    vetor_ferrugem_x = np.array(vetor_ferrugem_x)
    vetor_ferrugem_y = np.array(vetor_ferrugem_y)
    
    print ("Verdadeiros positivos: " + str(VP))
    print ("falsos negativos: " + str(FN))
    
    plotGrafico(
            vetor_ferrugem_x,
            vetor_ferrugem_y,
            'Folhas com ferrugem',
            'Chances míminas de ferrugem %',
            'Chances máximas de ferrugem %',
            'grafico_pontinhos_ferrugem.png'
    )
    
def gerarGraficoSaudaveis():

    planilha = xlrd.open_workbook(r"C:\Users\funck\Desktop\Documentos\UTFPR\Semestre8\TCC2\resultados\resultado_saudaveis.xlsx","r")
    
    sh = planilha.sheet_by_index(0)
    
    vetor_saudaveis_x = []
    vetor_saudaveis_y = []
    
    VN = 0
    FP = 0
    
    # Lendo porcentagem de chance da folha ter ferrugem ou ser saudavel na base de folhas saudaveis
    for linha in range(1, sh.nrows):
        vetor_saudaveis_x.append(sh.cell_value(rowx=linha, colx=1))
        vetor_saudaveis_y.append(sh.cell_value(rowx=linha, colx=2))
        
        vetor_geral_outros_x.append(sh.cell_value(rowx=linha, colx=1))
        vetor_geral_outros_y.append(sh.cell_value(rowx=linha, colx=2))
        
        valor_linha = (sh.cell_value(rowx=linha, colx=1) + sh.cell_value(rowx=linha, colx=2)) / 2
        if valor_linha <= 50:
            VN = VN + 1
        else:
            FP = FP + 1
        
    vetor_saudaveis_x = np.array(vetor_saudaveis_x)
    vetor_saudaveis_y = np.array(vetor_saudaveis_y)
    
    print ("Verdadeiros negativos saudaveis: " + str(VN))
    print ("falsos positivos saudaveis: " + str(FP))
    
    plotGrafico(
            vetor_saudaveis_x,
            vetor_saudaveis_y,
            'Folhas saudáveis',
            'Chances míminas de ferrugem %',
            'Chances máximas de ferrugem %',
            'grafico_pontinhos_saudavel.png'
    )
    
def gerarGraficoOutros():

    planilha = xlrd.open_workbook(r"C:\Users\funck\Desktop\Documentos\UTFPR\Semestre8\TCC2\resultados\resultados_outros.xlsx","r")
    
    sh = planilha.sheet_by_index(0)
    
    vetor_outros_x = []
    vetor_outros_y = []
    
    VN = 0
    FP = 0
    
    # Lendo porcentagem de chance da folha ter ferrugem ou não na base outros
    for linha in range(1, sh.nrows):
        vetor_outros_x.append(sh.cell_value(rowx=linha, colx=1))
        vetor_outros_y.append(sh.cell_value(rowx=linha, colx=2))
        
        vetor_geral_outros_x.append(sh.cell_value(rowx=linha, colx=1))
        vetor_geral_outros_y.append(sh.cell_value(rowx=linha, colx=2))
        
        valor_linha = (sh.cell_value(rowx=linha, colx=1) + sh.cell_value(rowx=linha, colx=2)) / 2
        if valor_linha <= 50:
            VN = VN + 1
        else:
            FP = FP + 1
        
    vetor_outros_x = np.array(vetor_outros_x)
    vetor_outros_y = np.array(vetor_outros_y)
    
    print ("Verdadeiros negativos outros: " + str(VN))
    print ("falsos positivos outros: " + str(FP))
    
    plotGrafico(
            vetor_outros_x,
            vetor_outros_y,
            'Folhas não identificadas',
            'Chances míminas de ferrugem %',
            'Chances máximas de ferrugem %',
            'grafico_pontinhos_outros.png'
    )
    
def gerarGraficoOlhoRa():

    planilha = xlrd.open_workbook(r"C:\Users\funck\Desktop\Documentos\UTFPR\Semestre8\TCC2\resultados\resultados_olho_ra.xlsx","r")
    
    sh = planilha.sheet_by_index(0)
    
    vetor_olho_ra_x = []
    vetor_olho_ra_y = []
    
    VN = 0
    FP = 0
    
    # Lendo porcentagem de chance da folha ter ferrugem ou não na base olho de rã
    for linha in range(1, sh.nrows):
        vetor_olho_ra_x.append(sh.cell_value(rowx=linha, colx=1))
        vetor_olho_ra_y.append(sh.cell_value(rowx=linha, colx=2))
        
        vetor_geral_outros_x.append(sh.cell_value(rowx=linha, colx=1))
        vetor_geral_outros_y.append(sh.cell_value(rowx=linha, colx=2))
        
        valor_linha = (sh.cell_value(rowx=linha, colx=1) + sh.cell_value(rowx=linha, colx=2)) / 2
        if valor_linha <= 50:
            VN = VN + 1
        else:
            FP = FP + 1
        
    vetor_olho_ra_x = np.array(vetor_olho_ra_x)
    vetor_olho_ra_y = np.array(vetor_olho_ra_y)
    
    print ("Verdadeiros negativos olho de rã: " + str(VN))
    print ("falsos positivos olho de rã: " + str(FP))
    
    plotGrafico(
            vetor_olho_ra_x,
            vetor_olho_ra_y,
            'Folhas com olho de rã',
            'Chances míminas de ferrugem %',
            'Chances máximas de ferrugem %',
            'grafico_pontinhos_olho_ra.png'
    )
    
def gerarGraficoManchaParda():

    planilha = xlrd.open_workbook(r"C:\Users\funck\Desktop\Documentos\UTFPR\Semestre8\TCC2\resultados\resultado_mancha_parda.xlsx","r")
    
    sh = planilha.sheet_by_index(0)
    
    vetor_mancha_parda_x = []
    vetor_mancha_parda_y = []
    
    VN = 0
    FP = 0
    
    # Lendo porcentagem de chance da folha ter ferrugem ou não na base macha parda
    for linha in range(1, sh.nrows):
        vetor_mancha_parda_x.append(sh.cell_value(rowx=linha, colx=1))
        vetor_mancha_parda_y.append(sh.cell_value(rowx=linha, colx=2))
        
        vetor_geral_outros_x.append(sh.cell_value(rowx=linha, colx=1))
        vetor_geral_outros_y.append(sh.cell_value(rowx=linha, colx=2))
        
        valor_linha = (sh.cell_value(rowx=linha, colx=1) + sh.cell_value(rowx=linha, colx=2)) / 2
        if valor_linha <= 50:
            VN = VN + 1
        else:
            FP = FP + 1
        
    vetor_mancha_parda_x = np.array(vetor_mancha_parda_x)
    vetor_mancha_parda_y = np.array(vetor_mancha_parda_y)
    
    print ("Verdadeiros negativos mancha parda: " + str(VN))
    print ("falsos positivos mancha parda: " + str(FP))
    
    plotGrafico(
            vetor_mancha_parda_x,
            vetor_mancha_parda_y,
            'Folhas com mancha parda',
            'Chances míminas de ferrugem %',
            'Chances máximas de ferrugem %',
            'grafico_pontinhos_mancha_parda.png'
    )
    
def gerarGraficoOidioSoja():

    planilha = xlrd.open_workbook(r"C:\Users\funck\Desktop\Documentos\UTFPR\Semestre8\TCC2\resultados\resultado_oidio_soja.xlsx","r")
    
    sh = planilha.sheet_by_index(0)
    
    vetor_oidio_soja_x = []
    vetor_oidio_soja_y = []
    
    VN = 0
    FP = 0
    
    # Lendo porcentagem de chance da folha ter ferrugem ou não na base oídio de soja
    for linha in range(1, sh.nrows):
        vetor_oidio_soja_x.append(sh.cell_value(rowx=linha, colx=1))
        vetor_oidio_soja_y.append(sh.cell_value(rowx=linha, colx=2))
        
        vetor_geral_outros_x.append(sh.cell_value(rowx=linha, colx=1))
        vetor_geral_outros_y.append(sh.cell_value(rowx=linha, colx=2))
        
        valor_linha = (sh.cell_value(rowx=linha, colx=1) + sh.cell_value(rowx=linha, colx=2)) / 2
        if valor_linha <= 50:
            VN = VN + 1
        else:
            FP = FP + 1
        
    vetor_oidio_soja_x = np.array(vetor_oidio_soja_x)
    vetor_oidio_soja_y = np.array(vetor_oidio_soja_y)
    
    print ("Verdadeiros negativos oídio da soja: " + str(VN))
    print ("falsos positivos oídio da soja: " + str(FP))
    
    plotGrafico(
            vetor_oidio_soja_x,
            vetor_oidio_soja_y,
            'Folhas com oídio da soja',
            'Chances míminas de ferrugem %',
            'Chances máximas de ferrugem %',
            'grafico_pontinhos_oidio_soja.png'
    )
    

gerarGraficoFerrugem()
gerarGraficoManchaParda()
gerarGraficoOidioSoja()
gerarGraficoOlhoRa()
gerarGraficoOutros()
gerarGraficoSaudaveis()

plotGraficoGeral(
        np.array(vetor_geral_ferrugem_x),
        np.array(vetor_geral_ferrugem_y),
        np.array(vetor_geral_outros_x),
        np.array(vetor_geral_outros_y));

        



    
    
    

    
