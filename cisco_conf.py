#encoding: utf-8
import getpass
from platform import mac_ver
from netmiko import ConnectHandler
from cisco import Switch

#def __init__(self):
#    self.connect = ConnectHandler(**Switch)
   

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
    global connect
    connect = ConnectHandler(**Switch)
    output = connect.find_prompt()

menu = "1"
while (menu <= "6"):
    menu = input("Deseja opção desejada: \n 1) V-lan de VOZ \n 2) V-lan de Dados \n 3) Verificar V-lans \n 4) Buscar porta \n 5) limpar porta \n 6) Sair: ")

    if menu == "1": # VLAN DE VOZ
        voice = input("Para qual v-lan deseja alterar: ")
        porta = input("Qual porta deseja alterar, ex: FX/X/X ou GX/X/X ")
        print ("configurando V-lan de Voz")
        alter_vlan = [
        'interface '+porta,
        'switch voice vlan ' +voice,

        ]

        output = connect.send_config_set(alter_vlan)
        print(output)
       
    if menu == "2": #VLAN DADOS
        dados = input("Para qual v-lan deseja alterar: ")
        porta = input("Qual porta deseja alterar, ex: F/X ou G/X ")

        alter_vlan = [
        'interface '+porta,
        'switch access vlan '+dados,
        ]

        output = connect.send_config_set(alter_vlan)
        print(output)
       

    if menu == "3": #MOSTRAR VLAN
        switch()
        output = connect.send_command("terminal length 0")
        output = connect.send_command("show vlan")
        print(output)
       
   
    if menu == "4": #Buscar porta
        mac = input("Digite o MAC:")
        output = connect.send_command("terminal length 0")
        output = connect.send_command("show mac address-table addres "+mac)
        print(output)
       

    if menu == "5": #limpar porta
        mac = input("Digite o MAC:")
        switch()
        output = connect.find_prompt()
        output = connect.send_command("terminal length 0")
        limpa_porta = ['clear port-security all address' +mac]
        output = connect.send_config_set(limpa_porta)
        print(output)
    else:
    #if menu == "6": #sair
        print("Saindo")
        #connect.disconnect()
        break