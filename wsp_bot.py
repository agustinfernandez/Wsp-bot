#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  2 15:43:18 2021

@author: agf
"""

from selenium import webdriver
import time

browser = webdriver.Chrome(executable_path= '/home/agf/alerta_bot_dengue_wsp/wsp_bot/driver/chromedriver')



def seleccionarChat(nombre : str):
    while True:
        
        print('buscando chat')
        elements = browser.find_elements_by_tag_name("span")
        for element in elements:
            if element.text == nombre:
                print('chat encontrado')
                element.click()
                return True
                break


def enviar():

    element = browser.find_element_by_xpath('/html/body/div[1]/div[1]/div[1]/div[4]/div[1]/footer/div[1]/div/span[2]/div/div[2]/div[2]/button')
    element.click()
    print("mensaje enviado")


def enviarMensaje(mensaje:str):
    
    chatbox = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')
    chatbox.send_keys(mensaje)
    time.sleep(2)
    enviar()


def leerArchivo(ruta:str):
    archivo = open(ruta, mode = 'r', encoding = 'utf-8')
    chatbox = browser.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/span[2]/div/div[2]/div[1]/div/div[2]')

    for linea in archivo.readlines():
        print("Mensaje: ", linea)
        chatbox.send_keys(linea)
    
    archivo.close()

def validaQR():
    try:
        element = browser.find_element_by_tag_name("canvas")
    except:
        return False
    return True


def botWhatsapp():
    browser.get("https://web.whatsapp.com/")
    time.sleep(5)
    
    espera = True
    while espera:
        print('Estoy esperando')
        espera = validaQR()
        time.sleep(2)
        if espera == False:
            print('Se autentico')
    seleccionarChat('Mel')
    leerArchivo('/home/agf/alerta_bot_dengue_wsp/wsp_bot/resource/pruebaBot.txt')
    
            
    

botWhatsapp()

