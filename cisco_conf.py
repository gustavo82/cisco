#encoding: utf-8
import getpass
from platform import mac_ver
from netmiko import ConnectHandler
from cisco import Switch

def __init__(self):
    self.connect = ConnectHandler(**Switch)

def switch():
    IP = input("Qual Switch deseja configurar: ")
    usuario = input("Digite seu Usuario: ")
    senha = getpass.getpass()

    Switch = {
    'device_type': 'cisco_ios',
    'host': IP,
    'username':usuario,
    'password':senha,
    }

    connect = ConnectHandler(**Switch)
    output = connect.find_prompt()

menu = "1"
while (menu != '4'):
    menu = input("Deseja opção desejada: \n 1) V-lan de VOZ \n 2) V-lan de Dados \n 3) Verificar V-lans \n 4) Buscar porta \n 5) limpar porta \n 6) Sair: ")

    if menu == "1": # VLAN DE VOZ
        voice = input("Para qual v-lan deseja alterar: ")
        porta = input("Qual porta deseja alterar, ex: FX/X/X ou GX/X/X ")
        print ("configurando V-lan de Voz")
        alter_vlan = [
        'interface '+porta,
        'switch voice vlan ' +voice,

        ]

        output = self.connect.send_config_set(alter_vlan)
        print(output)
       
    if menu == "2": #VLAN DADOS
        dados = input("Para qual v-lan deseja alterar: ")
        porta = input("Qual porta deseja alterar, ex: F/X ou G/X ")

        alter_vlan = [
        'interface '+porta,
        'switch access vlan '+dados,
        ]

        output = self.connect.send_config_set(alter_vlan)
        print(output)
       

    if menu == "3": #MOSTRAR VLAN
        switch()
        output = self.connect.send_command("terminal length 0")
        output = self.connect.send_command("show vlan")
        print(output)
       
   
    if menu == "4": #Buscar porta
        mac = input("Digite o MAC:")
        output = self.connect.send_command("terminal length 0")
        output = self.connect.send_command("show mac address-table addres "+mac)
        print(output)
       

    if menu == "5": #limpar porta
        output = self.connect.find_prompt()
        output = self.connect.send_command("terminal length 0")
        alter_vlan = [
        'interface '+porta,
        ' sh',
        'no shu',
        ]
        output = self.connect.send_config_set(alter_vlan)
        print(output)
    else:
    #if menu == "6": #sair
        print("Saindo")
        output = self.connect.disconnect()
        break