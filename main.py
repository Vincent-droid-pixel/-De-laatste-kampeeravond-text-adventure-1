import os
import sys

def hoofdmenu():
  print("=============================================")
  print("|                                           |")
  print("|                                           |")
  print("|     ----------------------------------    |")
  print("|     || Welkom bij de text adventure ||    |")
  print("|     ||    van Sannah en Vincent     ||    |")
  print("|     ----------------------------------    |")
  print("|                 Kies uit:                 |")
  choice = input("""|                                           |
|                  Start                    |
|                  Stop                     |
|                  Help                     |  
=============================================               
           Vul je keuze in:  """)   
  if choice == "Start":
    print("Start")
  elif choice == "Stop":
    sys.exit
  elif choice == "Stop":
    print("help")
  else:
    os.system('clear')
    print("=============================================")
    print("|       vul een geldig antwoord in!!!       |")
    hoofdmenu()


hoofdmenu()