import os
import sys
import time

#TO-do
# - Get/Drop item systeem
# - overige kamers toevoegen in data
# - forloops weghalen
# - bugs fixen

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
    "richtingen" : "1: De brug naar het noorden \n2: Het rivierpad naar het oosten",
    A : "BrugNaarNoorden",
    B : "RivierpadNaarOosten",
    C : "RivierMetBrug",
    D : "RivierMetBrug",
    "items" : [""],
    "acties" : "d (drop item) \nh (health) \ni (inventory) \n? (help) \nq (quit)",
    "dood" : "no",
    "win" : "no"
  },
  "BrugNaarNoorden" : {
    "titel" : "de brug",
    "doodsbeschrijving" : "Je loopt er overheen. De brug breekt door en je valt in het ijskoude water. Je weet er uiteindelijk nog wel uit te klimmen, maar uiteindelijk ga je toch dood door onderkoeling.",
    "beschrijving" : "Je loopt er overheen. De brug breekt door en je valt in het ijskoude water. Je weet er uiteindelijk nog wel uit te klimmen en overleeft het maar net. Je gaat snel terug naar het vorige kruispunt",
    A : "RivierMetBrug",
    "dood" : "yes",
    "win" : "no"
  },
  "RivierpadNaarOosten" :{
    "titel" : "Het rivierpad naar het Oosten",
    "beschrijving" : "Je loopt langs het pad en komt een klein meisje tegen in witte gewaden. Het lijkt bijna alsof ze gloeit zo licht zijn haar gewaden. Zodra het meisje je ziet loopt ze weg richting het zuiden. Je twijfelt of je haar zal volgen of dat je het rivier pad moet volgen.",
    "richtingen" : ["A: Verder naar het oosten", "B: Meisje naar zuiden", "C: De rivier bij de brug"],
    A : "VerderNaarOosten",
    B : "MeisjeZuiden",
    C : "RivierMetBrug",
    D : "RivierpadNaarOosten",
    "items" : "",
    "acties" : "g/d (get/drop item), \nh (health), \ni (inventory), \n? (help), \nq (quit)",
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

#get item functie 
def get():
  os.system("clear")
  print("In deze kamer liggen de volgende items:")
  print (kamers[speler.location][Items])
  print("Welk item wil je oppakken? (of typ [terug] als je terug wil gaan)")
  choice = input("")
  if choice.lower() == "":
    kamers[speler.location][Items].remove()
    speler.inventory.append()
  elif choice.lower == "terug":
    print_location()
  else:
    os.system("clear")
    print("vul een item in dat aanwezig is in de kamer!")
    time.sleep(3)
    get()

#drop item filter
def drop():
  os.system("clear")
  print("Je hebt de volgende items bij je:")
  print(speler.inventory)
  print("welk item wil je droppen?")
  choice = input("")
  if choice.lower() == "kompas":
    os.system("clear")
    print("=" * 40)
    print("Nadat je het kompas hebt weggegooid verdwaal je in het bos en niemand heeft je daarna ooit nog gevonden.")
    print("=" * 40)
    time.sleep(4)
    dood()
  else:
    os.system("clear")
    print("vul een item in dat je bij je hebt!")
    time.sleep(2.5)
    drop()


###DE GAME-LOOP###

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
    print(kamers[speler.location][Acties])
    print("~" * 30)
    print("je kunt de volgende richtingen op:")
    #for (x) in (RICHTINGEN):
    print (kamers[speler.location][Richtingen])
    print("~" * 30)
    keuze()
  elif kamers[speler.location][Dood] == ("yes") and speler.health == "100%":
    os.system('clear')
    speler.health = "50%"
    print("=" * 40)
    print(kamers[speler.location][Beschrijving])
    print("=" * 40)
    time.sleep(8)
    move_dest = kamers[speler.location][A]
    move_player(move_dest)
  elif kamers[speler.location][Dood] == ("yes") and speler.health == "50%":
    os.system('clear')
    print("=" * 40)
    print(kamers[speler.location][Doodsbeschrijving])
    print("=" * 40)
    time.sleep(8)
    dood()
  elif kamers[speler.location][Win] == ("yes"):
    os.system('clear')
    print("=" * 40)
    print(kamers[speler.location][Beschrijving])
    print("=" * 40)

#keuzemenu
def keuze():
  print ('Wat wil je doen?')
  option = input('')
  if option == "1":
    move_dest = kamers[speler.location][A]
    move_player(move_dest)
  elif option == "2":
    move_dest = kamers[speler.location][B]
    move_player(move_dest)
  elif option == "3":
    move_dest = kamers[speler.location][C]
    move_player(move_dest)
  elif option == "4":
    move_dest = kamers[speler.location][D]
    move_player(move_dest)
  elif option.lower() == "?":
    help_in_game()
  elif option.lower() ==  "i":
      inventory()
  elif option.lower() == "g":
      get()
  elif option.lower() == "d":
      drop()
  elif option.lower() == "h":
      health()
  elif option.lower() == "q":
      quit()
  else:
    os.system('clear')
    print("Vul aub een geldig antwoord in!")
    time.sleep(1.5)
    os.system('clear')
    print_location()
    keuze()

#========================================

#MENU'S
  
#dood-menu
def dood():
  os.system('clear')
  animation = ["Je", "Je bent", "Je bent dood.","Je bent dood. Wil","Je bent dood. Wil je", "Je bent dood. Wil je nog", "Je bent dood. Wil je nog een", "Je bent dood. Wil je nog een keer", "Je bent dood. Wil je nog een keer spelen?"]
  for x in range(len(animation)):
    time.sleep(0.5)
    sys.stdout.write("\r" + animation[x % len(animation)])
  print("_")
  choice = (input(''))
  if choice.lower() == "ja":
    os.system('clear')
    NaamInvullen()
  elif choice.lower() == "nee":
    os.system('clear')
    sys.exit
  else:
    print("vul een geldig antwoord in!")
    time.sleep(1.5)
    dood()

#quit-menu
def quit():
  os.system('clear')
  choice = (input("weet je zeker dat je wil stoppen?\n"))
  if choice.lower() == "ja":
    os.system('clear')
    hoofdmenu()
  elif choice.lower() == "nee":
    os.system('clear')
    print_location()
  else:
    print("vul een geldig antwoord in!")
    print("______________________________")
    quit()

#intro-menu
def intro():
  print("====================================================== \nJe bent gezellig met vrienden aan het kamperen in het bos. \nHelaas kon je niet slapen. \nJe dacht: 'laat ik even een boswandeling maken, zodat ik beter kan slapen.' \nHet enige wat je meeneemt is een kompas. \nNa een kwartier te hebben gelopen kom je opeens tot het besef dat je niet meer weet waar je bent! \nJe denkt bij jezelf: ‘ik moet mijn vrienden terugvinden!’ \n======================================================")
  choice = input(""" Schrijf [ok] als je verder wil gaan: """)
  if choice.lower() == "ok":
    os.system('clear')
    print_location()
  else:
    os.system('clear')
    print("============================================= \n|       vul een geldig antwoord in!!!       |")
    intro()

#naam-menu
def NaamInvullen():
  print("============================================= \n|                                           | \n|                                           | \n|                                           | \n|              wat is je naam?              | \n|                                           | \n|                                           | \n|                                           | \n=============================================")

  speler_naam = input()
  speler.naam = speler_naam

  format_string = "Hallo %s, leuk dat je deze text adventure speelt!"
  print(format_string % speler.naam)
  time.sleep(2)
  os.system('clear')
  intro()
  
#help-menu voor in een kamer
def help_in_game():
  os.system('clear')
  print("============================================= \nJe hebt verschillende controls in deze text adventure. \nTen eerste kan je met help [?] dit menu zien en met quit [q] kan je stoppen. \nVerder kun je met ‘get item [g]’ en ‘drop item [d]’ items oppakken en laten vallen / neerleggen. \nDaarnaast kan je met ‘inventory [i]’ alle items zien die je hebt opgepakt. \nOok kan je nog met de gegeven windrichtingen (Noord [n], Oost [o], Zuid [z], West [w]) bij elk gebied, naar het volgende gebied gaan. \nTenslotte kan je met ‘health [h]’ je health zien. \nAl deze controls kan je tijdens het gehele spel gebruiken. \n=============================================")
  choice = input(" Typ 'terug' als je terug naar het spel wil gaan: ")
  if choice.lower() == "terug":
    os.system('clear')
    print_location()
  else:
    os.system('clear')
    print("============================================= \n|       vul een geldig antwoord in!!!       |")
    help_in_game()

#help-menu voor in het hoofdmenu
def help():
  print("============================================= \nJe hebt verschillende controls in deze text adventure. \nTen eerste kan je met help [?] dit menu zien en met quit [q] kan je stoppen. \nVerder kun je met ‘get item [g]’ en ‘drop item [d]’ items oppakken en laten vallen / neerleggen. \nDaarnaast kan je met ‘inventory [i]’ alle items zien die je hebt opgepakt. \nOok kan je nog met de gegeven windrichtingen (Noord [n], Oost [o], Zuid [z], West [w]) bij elk gebied, naar het volgende gebied gaan. \nTenslotte kan je met ‘health [h]’ je health zien. \nAl deze controls kan je tijdens het gehele spel gebruiken. \n=============================================")
  choice = input(""" Typ 'menu' als je terug naar het menu wil gaan: """)
  if choice.lower() == "menu":
    os.system('clear')
    hoofdmenu()
  else:
    os.system('clear')
    print("============================================= \n|       vul een geldig antwoord in!!!       |")
    help()

#stop-menu
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
    print("============================================= \n|       vul een geldig antwoord in!!!       |")
    stop()

#hoofdmenu
def hoofdmenu():
  print("============================================= \n|                                           | \n|                                           | \n|     ----------------------------------    | \n|     || Welkom bij de text adventure ||    | \n|     ||    van Sannah en Vincent     ||    | \n|     ----------------------------------    | \n|                 Kies uit:                 | \n|                                           |\n|                  -start                   | \n|                  -stop                    | \n|                  -help                    | \n =============================================")
  choice = input("""           Vul je keuze in:  """)   
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
    print("============================================= \n|       vul een geldig antwoord in!!!       |")
    hoofdmenu()
                                        

hoofdmenu()

class speler:
    def __init__(self):
        self.name = ''
        self.health = "100%"   
        self.inventory = ["kompas"]      
        self.location = 'RivierMetBrug'
speler = speler()