import os
import sys
import time

#TO-do
# - Get/Drop item systeem
# - overige kamers toevoegen in data


# Kamers #
Titel = "titel"
Location = "location"
Beschrijving = "beschrijving"
Doodsbeschrijving = "doodsbeschrijving"
Items = "items"
Richtingen = "richtingen"
Dood = "dood"
Win = "win"
Acties = "acties"
A = "a"
B = "b"
C = "c"
D = "d"


class speler:
    def __init__(self):
        self.name = ''
        self.health = "100%"   
        self.inventory = ["kompas"]      
        self.location = 'RivierMetBrug'
speler = speler()


#kamers
kamers = {
  "RivierMetBrug" : {
    "titel" : "een rivier met een brug.",
    "beschrijving" : "Het is een gammele houten brug die naar het noorden over de rivier loopt. Je weet niet of je er eigenlijk wel overheen kunt lopen zonder dat hij doorbreekt. Je ziet ook nog een pad langs het water stroomopwaarts richting het oosten lopen.",
    "richtingen" : ["A: De brug naar het noorden", "B: Het rivierpad naar het oosten"],
    A : "BrugNaarNoorden",
    B : "RivierpadNaarOosten",
    C : "RivierMetBrug",
    D : "RivierMetBrug",
    "items" : "X",
    "acties" : ["g (get item)", "d (drop item)", "h (health)", "i (inventory)"],
    "dood" : "no",
    "win" : "no"
  },
  "BrugNaarNoorden" : {
    "titel" : "de brug",
    "doodsbeschrijving" : "Je loopt er overheen. De brug breekt door en je valt in het ijskoude water. Je weet er uiteindelijk nog wel uit te klimmen, maar uiteindelijk ga je toch dood door onderkoeling.",
    "beschrijving" : "Je loopt er overheen. De brug breekt door en je valt in het ijskoude water. Je weet er uiteindelijk nog wel uit te klimmen en overleeft het maar net. Je gaat snel terug naar het vorige kruispunt",
    A : "RivierMetBrug",
    "richtingen" : "",
    "acties" : "",
    "dood" : "yes",
    "win" : "no"
  },
  "RivierpadNaarOosten" :{
    "titel" : "Het rivierpad naar het Oosten",
    "beschrijving" : "Je loopt langs het pad en komt een klein meisje tegen in witte gewaden. Het lijkt bijna alsof ze gloeit zo licht zijn haar gewaden. Zodra het meisje je ziet loopt ze weg richting het zuiden. Je twijfelt of je haar zal volgen of dat je het rivier pad moet volgen.",
    "richtingen" : "z, o",
    "items" : "",
    "acties" : ["g (get item)", "d (drop item)", "h (health)", "i (inventory)"],
    "dood" : "no",
    "win" : "no"
  }
}

#inventory laten zien
def inventory():
  os.system('clear')
  print ("- - - - - - - - - - - - - - - - \ndit heb je op dit moment bij je: \n",speler.inventory, "\n-------------------------------")
  time.sleep(5)
  print_location()

#health laten zien
def health():
  os.system('clear')
  print ("- - - - - - - - - - - - - - - - \ndit is hoeveel health je op dit moment hebt: \n",speler.health,"\n-------------------------------")
  time.sleep(5)
  print_location()


#doodsfunctie
def dood():
  print("wil je nog een keer spelen?")
  choice = (input())
  if choice.lower == "ja":
    NaamInvullen()
  elif choice.lower == "nee":
    sys.exit
  else:
    print("vul een geldig antwoord in!")
    print("___________________________________________")
    dood()



#quitmenu
def quit():
  os.system('clear')
  choice = (input("weet je zeker dat je wil stoppen?"))
  if choice.lower == "ja":
    hoofdmenu()
  elif choice.lower == "nee":
    print_location()
  else:
    print("vul een geldig antwoord in!")
    print("______________________________")
    quit()



#de gameloop
#locatie informatie verkrijgen
ITEMS = kamers[speler.location][Items]
ACTIES = kamers[speler.location][Acties]
RICHTINGEN = kamers[speler.location][Richtingen]


#speler verplaatsen
def move_player(move_dest):
	speler.location = move_dest
	print_location()

# print locatie 
def print_location():
  if kamers[speler.location][Dood] == ("no") and kamers[speler.location][Win] == ("no"):
    os.system('clear')
    print(kamers[speler.location][Titel])
    print("=" * 40)
    print(kamers[speler.location][Beschrijving])
    print("=" * 40)
    print("Op deze locatie liggen de volgende items:")
    for (i) in (ITEMS):
      print(i)
    print("~" * 30)
    print("je kunt de volgende dingen doen:")
    for (a) in (ACTIES):
      print(a)
    print("~" * 30)
    print("je kunt de volgende richtingen op:")
    for (x) in (RICHTINGEN):
      print (x)
    print("~" * 30)
    keuze()
  elif kamers[speler.location][Dood] == ("yes") and speler.health == "100%":
    os.system('clear')
    speler.health = "50%"
    print("=" * 40)
    print(kamers[speler.location][Beschrijving])
    print("=" * 40)
    time.sleep(10)
    move_dest = kamers[speler.location][A]
    move_player(move_dest)
  elif kamers[speler.location][Dood] == ("yes") and speler.health == "50%":
    os.system('clear')
    print("=" * 40)
    print(kamers[speler.location][Doodsbeschrijving])
    print("=" * 40)
    time.sleep(10)
    dood()
  elif kamers[speler.location][Win] == ("yes"):
    os.system('clear')
    print("yay")

#keuzemenu
def keuze():
  print ('Wat wil je doen?')
  option = input('')
  if option.lower() == "a":
    move_dest = kamers[speler.location][A]
    move_player(move_dest)
  elif option.lower() == "b":
    move_dest = kamers[speler.location][B]
    move_player(move_dest)
  elif option.lower() == "c":
    move_dest = kamers[speler.location][C]
    move_player(move_dest)
  elif option.lower() == "d":
    move_dest = kamers[speler.location][D]
    move_player(move_dest)
  elif option.lower() ==  "i":
      inventory()
    #elif option.lower == "g":
    #  getitem()
    #elif option.lower == "d":
    #  dropitem()
  elif option.lower() == "h":
      health()
  elif option.lower() == "q":
      quit()
  else:
    print("Vul aub een geldig antwoord in")
    keuze()

  #location = kamers[gebied]

  #titel en beschrijving van kamer verkrijgen#
  #titel = locatie["titel"]
  #beschrijving = locatie["beschrijving"]
  #nietdoodsbeschrijving = locatie["nietdoodsbeschrijving"]
  #acties = locatie["acties"]
  #dood = locatie["death"]
  #winnen = locatie["win"]

  #kamer beschrijven
  #os.system('clear')
  #doodgaan = (dood)
    
  
  
    

  #elif doodgaan == "yes" and playerhealth == "100%":
    #playerhealth = "50%"
  #  print(nietdoodsbeschrijving)
  #elif doodgaan == "yes" and playerhealth == "50%":
  #  print(beschrijving)
  #  time.sleep(5)
  #  dood()
  

#intro#
def intro():
  print("======================================================")
  print("Je bent gezellig met vrienden aan het kamperen in het bos. Helaas kon je niet slapen. Je dacht: 'laat ik even een boswandeling maken, zodat ik beter kan slapen.' Het enige wat je meeneemt is een kompas.")
  print("")
  print("======================================================")
  choice = input(""" Schrijf ok als je verder wil gaan: """)
  if choice.lower() == "ok":
    os.system('clear')
    #zorgt dat de speler naam kan invullen
    print_location()
  else:
    os.system('clear')
    print("=============================================")
    print("|       vul een geldig antwoord in!!!       |")
    intro()

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
    os.system('clear')
    intro()
  else:
    os.system('clear')
    intro()


#helpmenu
def help():
  print("=============================================")
  print("Je hebt verschillende controls in deze text adventure. Zo kun je met ‘get item [g]’ en ‘drop item [d]’ items oppakken en laten vallen / neerleggen. Verder kan je met ‘inventory [i]’ alle items zien die je hebt opgepakt. Ook kan je nog met de gegeven windrichtingen (Noord [n], Oost [o], Zuid [z], West [w]) bij elk gebied, naar het volgende gebied gaan. (Ten slotte kan je met ‘health [h]’ je health zien.) Al deze controls kan je tijdens het gehele spel gebruiken.")
  print("=============================================")
  choice = input(""" Typ 'menu' als je terug naar het menu wil gaan: """)
  if choice.lower() == "menu":
    os.system('clear')
    hoofdmenu()
  else:
    os.system('clear')
    print("=============================================")
    print("|       vul een geldig antwoord in!!!       |")
    help()

#stopmenu
def stop():
  print("=============================================")
  choice = input("""     Weet je zeker dat je wil stoppen?  """)
  if choice.lower() == "ja":
    os.system('clear')
    print("bedankt voor het spelen!!!")
    sys.exit
  elif choice.lower() == "nee":
    os.system('clear')
    hoofdmenu()
  else:
    os.system('clear')
    print("=============================================")
    print("|       vul een geldig antwoord in!!!       |")
    stop()



#hoofdmenu
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
|                  start                    |
|                  stop                     |
|                  help                     |  
=============================================               
           Vul je keuze in:  """)   
  #keuzes van het hoofdmenu#
  if choice.lower() == "start":
    os.system('clear')
    NaamInvullen()
  elif choice.lower() == "stop":
    os.system('clear')
    stop()
  elif choice.lower() == "help":
    os.system('clear')
    help()
  else:
    os.system('clear')
    print("=============================================")
    print("|       vul een geldig antwoord in!!!       |")
    hoofdmenu()
                                        

hoofdmenu()