# -*- coding: utf-8 -*-
from abre_texto import split_into_sentences as splitT
from selenium import webdriver
from time import sleep

import win32clipboard

def paste():
    win32clipboard.OpenClipboard()
    data = win32clipboard.GetClipboardData(win32clipboard.CF_UNICODETEXT)
    win32clipboard.CloseClipboard()
    return data

browser = webdriver.Chrome(executable_path='E:\chromedriver')
browser.implicitly_wait(10)

url = 'https://www.deepl.com/translator'


browser.get(url)
sleep(5)

#endereçando os botões
escolher_idioma_traducao = browser.find_element_by_xpath('/html/body/div[2]/div[1]/div[1]/div[3]/div[1]/div/button')
idioma_ingles = browser.find_element_by_xpath( '/html/body/div[2]/div[1]/div[1]/div[3]/div[1]/div/div/button[2]')

escolha_idioma_traduzido = browser.find_element_by_xpath( '/html/body/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/button/span')
idioma_a_traduzir =browser.find_element_by_xpath( '/html/body/div[2]/div[1]/div[1]/div[4]/div[1]/div[1]/div[1]/div/button[6]')

#escolhendo o idioma ingles como fonte de tradução
escolher_idioma_traducao.click()
sleep(1)
idioma_ingles.click()
sleep(0.5)
#escolhendo o idioma portugues
escolha_idioma_traduzido.click()
sleep(1)
idioma_a_traduzir.click()
cookie = browser.find_element_by_xpath( '/html/body/div[7]/div/div/div/span/div[2]/button[2]').click()

#----------------------------------------------------------------------------------------------------------
#definindo arquivos a serem trabalhados
l1 = ['towers-of-midnight.txt'] 
l2 = ['torres_da_meia_noite.txt']

#definindo entrada e saida 
entrada = browser.find_element_by_xpath( '/html/body/div[2]/div[1]/div[1]/div[3]/div[2]/div/textarea')


sleep(0.5)


contador=0
for i in l1:
    texto = splitT(i)
    with open(l2[contador],'w') as traducao:
        for p in texto:
            entrada.send_keys(p)
            sleep(5)            
            saida = browser.find_element_by_css_selector('#dl_translator > div.lmt__sides_container > div.lmt__side_container.lmt__side_container--target > div.lmt__textarea_container > div.lmt__target_toolbar.lmt__target_toolbar--visible > div.lmt__target_toolbar__copy > button').click()
            print(paste())
            elemento = paste()
            traducao.writelines(elemento)
            entrada.clear()
            sleep(1)  
                        
browser.close()


