# -*- coding: utf-8 -*-
from abre_texto import split_into_sentences as splitT
from selenium import webdriver
from time import sleep

chrome_opt = webdriver.ChromeOptions()
chrome_opt.add_argument('--disable-gpu')
browser = webdriver.Chrome(executable_path='E:\chromedriver')
browser.implicitly_wait(10)


id_text_area = "source"
n1 ="/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[3]/div[1]/div[2]/div/span[1]/span[1]" 
n2='/html/body/div[2]/div[2]/div[1]/div[2]/div[1]/div[1]/div[2]/div[4]/div[1]/div[2]/div/span[1]'

url = 'https://translate.google.com.br/'


browser.get(url)

entrada = browser.find_element_by_id(id_text_area)
#browser.find_element_by_xpath('//*[@id="sugg-item-pt"]')

browser.find_element_by_xpath('//*[@id="sugg-item-en"]').click()
l1 = ['memory of light.txt'] 
l2 = ['a-memoria-da-luz.txt']

contador=0
for i in l1:
    texto = splitT(i)
    with open(l2[contador],'w') as traducao:
        for p in texto:
            entrada.send_keys(p)
            sleep(3)
            try:
                elemento=browser.find_element_by_xpath(n1)
            except:
                elemento=browser.find_element_by_xpath(n2)
            with open('ulimoTrecho.txt','w')as ultimo:
                ultimo.writelines(p)
            print(elemento.get_attribute('innerHTML'))
            traducao.writelines(elemento.get_attribute('innerHTML')+'\n')
            entrada.clear()
            sleep(1)  
                        
browser.close()