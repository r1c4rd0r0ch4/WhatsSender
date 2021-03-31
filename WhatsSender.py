from time import sleep
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
import socket

message_text='Olá tudo bem?' # message

no_of_message=1 # número de vezes
moblie_no_list=[5519971204567,5515996333479] # Lista dos números de telefone

def element_presence(by,xpath,time):
    element_present = EC.presence_of_element_located((By.XPATH, xpath))
    WebDriverWait(driver, time).until(element_present)

def is_connected():
    try:
        # faz uma conexão com um host e retorna se está acessível ou não
        socket.create_connection(("www.google.com", 80))
        return True
    except :
        is_connected()
driver = webdriver.Firefox()
driver.get("https://web.whatsapp.com")
input('Após ler o QR Code pressione ENTER')

def send_whatsapp_msg(phone_no,text):
    driver.get("https://web.whatsapp.com/send?phone={}&source=&data=#".format(phone_no))
    try:
        driver.switch_to.alert.accept()
    except Exception as e:
        pass

    try:
        element_presence(By.XPATH,'//*[@id="main"]/footer/div[1]/div[2]/div/div[2]',30)
        txt_box=driver.find_element(By.XPATH , '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
        global no_of_message
        for x in range(no_of_message):
            txt_box.send_keys(text +Keys.ENTER)
            txt_box.send_keys('Eu me chamo fulano, essa é uma mensagem de teste\n')
            txt_box.send_keys('Ao receber essa mensagem me mande uma mensagem de volta' + Keys.ENTER)
            sleep(1)
    except Exception as e:
        print("Numero de telefone invalido :"+str(phone_no))

for moblie_no in moblie_no_list:
    try:
        send_whatsapp_msg(moblie_no,message_text)

    except Exception as e:
        sleep(10)
        is_connected()