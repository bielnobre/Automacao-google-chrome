
"""		Pyautomator Framework de teste 

			AutCalc"""

from Pyautomators.desk import Desk
from Pyautomators.mouse_teclado import Teclado
from Pyautomators.mouse_teclado import Mouse
from Pyautomators.Verifica import Valida
from Pyautomators import Ambiente
from pages.pages.chrome import Chrome

from Pyautomators import *
from time import sleep

def before_all(context):
	context.app = Desk('C:\Program Files (x86)\Google\Chrome\Application\chrome.exe', Driver_Winium='driver\Winium.Desktop.Driver.exe')
	context.chrome = Chrome(context.app)


def before_feature(context,feature):
	pass

def before_scenario(context,scenario):
	pass

def before_step(context,step):
	pass

def after_step(context,step):
	pass

def after_scenario(context,scenario):
	pass

def after_feature(context,feature):
	pass

def after_all(context):
	context.app.fechar_programa()

