import os
import sys
#kamers
kamers = {
  "RivierMetBrug" : {
    "titel" : "een rivier met een gammele brug.",
    "beschrijving" : "Het is een gammele houten brug die naar het noorden over de rivier loopt. Je weet niet of je er eigenlijk wel overheen kunt lopen zonder dat hij doorbreekt. Je ziet ook nog een pad langs het water stroomopwaarts richting het oosten lopen.",
    "opties" : ["n", "o"]
  },
}
#de gameloop
def game(gebied):
  locatie = kamers[gebied]
  #titel en beschrijving van kamer verkrijgen#
  titel = locatie["titel"]
  beschrijving = locatie["beschrijving"]
  #kamer beschrijven
  os.system('clear')
  print("=============================================")
  print(f"Je komt aan bij {titel}")
  print(beschrijving)
  print("=============================================")
  print("typ de windrichting waar je heen wil gaan: ")

#naam invullen#
def NaamInvullen():
  print("=============================================")
  print("|                                           |")
  print("|                                           |")
  print("|                                           |")
  print("|              wat is je naam?              |")
  print("|                                           |")
  print("|                                           |")
  print("|                                           |")
  print("=============================================")
  speler_naam = input()
  speler.naam = speler_naam
  format_string = "Hallo %s, leuk dat je deze text adventure speelt!"
  print(format_string % speler.naam)

  choice = input(""" Typ een willekeurige letter om verder te gaan: """)
  if choice == "":
    game("RivierMetBrug")
  else:
    game("RivierMetBrug")
  
class speler:
  def  spelernaam(zelf):
    zelf.naam = ''
speler = speler()

#intro#
def intro():
  print("======================================================")
  print("Je bent gezellig met vrienden aan het kamperen in het bos. Helaas kon je niet slapen. Je dacht: 'laat ik even een boswandeling maken, zodat ik beter kan slapen.' Het enige wat je meeneemt is een kompas.")
  print("")
  print("======================================================")
  choice = input(""" Schrijf OK als je verder wil gaan: """)
  if choice == "OK":
    os.system('clear')
    #zorgt dat de speler naam kan invullen
    NaamInvullen()
  else:
    os.system('clear')
    print("=============================================")
    print("|       vul een geldig antwoord in!!!       |")
    intro()

#helpmenu
def help():
  print("=============================================")
  print("Je hebt verschillende controls in deze text adventure. Zo kun je met ‘get item [g]’ en ‘drop item [d]’ items oppakken en laten vallen / neerleggen. Verder kan je met ‘inventory [i]’ alle items zien die je hebt opgepakt. Ook kan je nog met de gegeven windrichtingen (Noord [n], Oost [o], Zuid [z], West [w]) bij elk gebied, naar het volgende gebied gaan. (Ten slotte kan je met ‘health [h]’ je health zien.) Al deze controls kan je tijdens het gehele spel gebruiken.")
  print("=============================================")
  choice = input(""" Typ 'Menu' als je terug naar het menu wil gaan: """)
  if choice == "Menu":
    os.system('clear')
    hoofdmenu()
  else:
    os.system('clear')
    print("=============================================")
    print("|       vul een geldig antwoord in!!!       |")
    help()


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
    os.system('clear')
    intro()
  elif choice == "start":
    os.system('clear')
    intro()
  elif choice == "Stop":
    sys.exit
  elif choice == "help":
    os.system('clear')
    help()
  else:
    os.system('clear')
    print("=============================================")
    print("|       vul een geldig antwoord in!!!       |")
    hoofdmenu()
                                        
hoofdmenu()