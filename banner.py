import pyfiglet as pyg
from termcolor import colored
text = "INSTASCRAPE"
by = "BY:"
name = "crazyoh123"
print(colored(pyg.figlet_format(text, font="xsbook",direction="left",justify="auto",width=100), 'red')+"\n")
print(colored(by, 'green')+"\n")
print(colored(name+"//", 'green')+"\n")