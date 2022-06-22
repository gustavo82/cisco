#encoding: utf-8
import getpass
from netmiko import ConnectHandler 
import PySimpleGUI as sg

class TelaPython:
	def __init__(self):
		# Layout
		layout = [
			[sg.Text('Usuario:',size=(7,0)),sg.Input(size=(13,0))],
			[sg.Text('Senha:',size=(7,0)),sg.Input(size=(13,0))], 
			[sg.Text('Switch:',size=(7,0)),sg.Input(size=(13,0),key='switch')],
			[sg.Text('Porta:',size=(7,0)), sg.Input(size=(13,0),key='porta')],
			[sg.Button('Alterar')],
			[sg.Button('Sair')],
			[sg.Output(size=(20,10))]
		]
		#Janela
		self.janela = sg.Window("Troca de Vlan").layout(layout)


	def Iniciar(self):	
		while True:
			#Extrair dados
			self.button, self.values = self.janela.Read()	
			switch = self.values['switch']
			porta = self.values['porta']


			print(f'switch: {switch}')
			print(f'porta: {porta}')

tela = TelaPython()
tela.Iniciar()