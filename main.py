import os
import sys

#kamerbeschrijving#
def kamerbeschrijving():
  os.system('clear')
  print("=============================================")

  print("=============================================")

#intro#
def intro():
  os.system('clear')
  print("======================================================")
  print("Je bent gezellig met vrienden aan het kamperen in het bos. Helaas kon je niet slapen. Je dacht: 'laat ik even een boswandeling maken, zodat ik beter kan slapen.' Het enige wat je meeneemt is een kompas.")
  print("")
  print("======================================================")
  choice = input(""" Schrijf OK als je verder wil gaan: """)
  if choice == "OK":
    kamerbeschrijving()

#hoofdmenu#
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
  #keuzes van het hoofdmenu#
  if choice == "Start":
        intro()
  elif choice == "start":
    intro()
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