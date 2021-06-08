import os
import sys
import time
##TABEL##
#from tabulate import tabulate
#table = [[]]
#print(tabulate(table, tablefmt='grid'))


#TO-do
# - overige kamers toevoegen in data
# - bugs fixen

#opties-menu 
def opties():
  print('=' * 40)
  print("Wil je een typemachine animatie bij de tekst?")
  print("ja/nee")
  print('=' * 40)
  choice = input('')
  if choice.lower() == "ja":
    speler.typemachine = "true"
    os.system('clear')
    print("typemachine animatie staat nu aan")
    time.sleep(2.5)
    os.system('clear')
    hoofdmenu()
  elif choice.lower() == "nee":
    speler.typemachine = "false"
    os.system('clear')
    print("typemachine animatie staat nu uit")
    time.sleep(2.5)
    os.system('clear')
    hoofdmenu()
  else:
    os.system('clear')
    opties()

# Kamers #
Titel = "titel"
Location = "location"
Beschrijving = "beschrijving"
Doodsbeschrijving = "doodsbeschrijving"
Items = "items"
Benodigdheden = "benodigdheden"
Richtingen = "richtingen"
Dood = "dood"
Win = "win"
Acties = "acties"
A = "a"
B = "b"
C = "c"
D = "d"
E = "e"

class speler:
    def __init__(self):
        self.name = ''
        self.health = "100%"   
        self.inventory = ["","kompas"]      
        self.location = 'RivierMetBrug'
        self.typemachine = 'false'
speler = speler()



#kamers
kamers = {
  "RivierMetBrug" : {
    "titel" : "Je komt bij een rivier met een brug.",
    "beschrijving" : "Het is een gammele houten brug die naar het noorden over de rivier loopt. \nJe weet niet of je er eigenlijk wel overheen kunt lopen zonder dat hij doorbreekt. \nJe ziet ook nog een pad langs het water stroomopwaarts richting het oosten lopen.",
    "richtingen" : "N: De brug naar het noorden \nO: Het rivierpad naar het oosten",
    A : "BrugNaarNoorden",
    B : "RivierpadNaarOosten",
    C : "RivierMetBrug",
    D : "RivierMetBrug",
    "items" : [""],
    "benodigdheden" : "",
    "acties" : "d (drop item) \nh (health) \ni (inventory) \n? (help) \nq (quit)",
    "dood" : "no",
    "win" : "no"
  },
  "BrugNaarNoorden" : {
    "titel" : "de brug",
    "doodsbeschrijving" : "Je loopt er overheen. De brug breekt door en je valt in het ijskoude water. Je weet er uiteindelijk nog wel uit te klimmen, maar uiteindelijk ga je toch dood door onderkoeling.",
    "beschrijving" : "Je loopt er overheen. De brug breekt door en je valt in het ijskoude water. Je weet er uiteindelijk nog wel uit te klimmen en overleeft het maar net. Je gaat snel terug naar het vorige kruispunt",
    A : "RivierMetBrug",
    "benodigdheden" : "",
    "dood" : "yes",
    "win" : "no"
  },
  "RivierpadNaarOosten" :{
    "titel" : "Het rivierpad naar het Oosten",
    "beschrijving" : "Je loopt langs het pad en komt een klein meisje tegen in witte gewaden. Het lijkt bijna alsof ze gloeit zo licht zijn haar gewaden. Zodra het meisje je ziet loopt ze weg richting het zuiden. Je twijfelt of je haar zal volgen of dat je het rivier pad moet volgen.",
    "richtingen" : "O: Verder naar het oosten \nZ: Meisje naar zuiden \nW: De rivier bij de brug",
    A : "RivierpadNaarOosten",
    B : "RotsmuurInOosten",
    C : "MeisjeZuiden",
    D : "RivierMetBrug",
    "items" : [""],
    "benodigdheden" : "",
    "acties" : "d (drop item), \nh (health), \ni (inventory), \n? (help), \nq (quit)",
    "dood" : "no",
    "win" : "no"
  },
  "MeisjeZuiden" :{
    "titel" : "Meisje in het zuiden",
    "doodsbeschrijving" : "Je komt op een open plaats en ziet het meisje nog net verdwijnen tussen de bosjes. Opeens komt er uit diezelfde bosjes een groot gruwelijk monster (details nog uitwerken). Het monster verslindt je met huid en haar en je gaat dood.",
    "beschrijving" : "Je komt op een open plaats en ziet het meisje nog net verdwijnen tussen de bosjes. \nOpeens komt er uit diezelfde bosjes een groot gruwelijk monster (details nog uitwerken). \nJe weet net op tijd weg te rennen en komt weer uit bij het rivierpad",
    A : "RivierpadNaarOosten",
    "benodigdheden" : "",
    "dood" : "yes",
    "win" : "no"
  },
  "RotsmuurInOosten" :{
    "titel" : "Rotsmuur in het oosten",
    "beschrijving" : "Je komt bij een stenen helling van een berg die te steil is om te klimmen. \nDaar waar de rots overgaat in het gras zie je iets liggen. \nAls je goed kijkt blijkt het dat het een lijk is. \nMaar het is geen gewoon lijk. \nHet lijk is vastgegroeid aan de rots door een of andere schimmel. \nJe ziet dat het lijk iets in zijn handen heeft. \nHet blijkt een machete te zijn. \nDaarmee kun je planten wegslaan. \nJe kan vanaf hier alleen naar het zuiden want in het noorden loopt de rivier en in het oosten is de rotsmuur.",
    "richtingen" : "Z: Pad langs de rotsmuur naar het zuiden \nW: Rivierpad in het westen" ,
    A : "RotsmuurInOosten",
    B : "RotsmuurInOosten",
    C : "PadLangsRotsmuur",
    D : "RivierpadNaarOosten",
    "items" : ["machete"],
    "benodigdheden" : "",
    "acties" : "g/d (get/drop item), \nh (health), \ni (inventory), \n? (help), \nq (quit)",
    "dood" : "no",
    "win" : "no",
  },
  "PadLangsRotsmuur" :{
    "titel" : "Het pad langs de rotsmuur",
    "beschrijving" : "Je loopt op het pad en je ziet een verlaten huisje. \nJe loopt er naar toe en je betwijfelt of het wel een goede keuze is om naar binnen te gaan. \nJe denkt bij jezelf: “In horrorfilms zijn dit altijd de plekken waar het fout gaat.” \nDe ingang van het huisje is ten zuiden van jou. \nJe kan ook om het huisje heen via een pad ten westen van jou.",
    "richtingen" : "N: De Rotsmuur \nZ: Het huisje in het zuiden binnengaan \nW: Het pad om het huisje heen",
    A : "RotsmuurInOosten",
    B : "PadLangsRotsmuur",
    C : "Huisje",
    D : "PadLangsHuisje",
    "items" : [""],
    "benodigdheden" : "",
    "acties" : "d (drop item), \nh (health), \ni (inventory), \n? (help), \nq (quit)",
    "dood" : "no",
    "win" : "no"
  },
  "Huisje" :{
    "titel" : "In het huisje",
    "beschrijving" : "Je besluit om naar binnen te gaan. \nBij je eerste stap in het huis hoor je meteen de planken onder je voeten kraken. \nJe vraagt je af hoe oud dit huis eigenlijk is. \nOpeens hoor je een piano spelen in een kamer ten oosten van jou. \nJe weet niet of je daar heen moet gaan, maar misschien vind je dan eindelijk iemand anders in dit vreselijke bos. \nJe kan ook naar het zuiden de trap af naar de kelder.",
    "richtingen" : "N: Het huisje uit \nO: De kamer met de pianomuziek \nZ: De keldertrap af",
    A : "PadLangsRotsmuur",
    B : "Pianokamer",
    C : "Kelder",
    D : "Huisje",
    "items" : [""],
    "benodigdheden" : "",
    "acties" : "d (drop item), \nh (health), \ni (inventory), \n? (help), \nq (quit)",
    "dood" : "no",
    "win" : "no"
  },
  "Kelder" :{
    "titel" : "",
    "beschrijving" : "",
    "richtingen" : "",
    A : "",
    B : "",
    C : "",
    D : "",
    "items" : [""],
    "benodigdheden" : "",
    "acties" : "",
    "dood" : "",
    "win" : ""
  },
  "Pianokamer" :{
    "titel" : "",
    "beschrijving" : "",
    "richtingen" : "",
    A : "",
    B : "",
    C : "",
    D : "",
    "items" : [""],
    "benodigdheden" : "",
    "acties" : "",
    "dood" : "",
    "win" : ""
  },
  "PadLangsHuisje" :{
    "titel" : "Je bent op het pad naast het huisje",
    "beschrijving" : "Je bent nu in de achtertuin van het schimmige oude huisje. Er is hier niet veel te vinden, maar er ligt wel een lang stevig touw. Dat zou vast handig kunnen zijn. Opeens hoor je een soort gezang. Het lijkt vanuit zuidelijke richting te komen. Ook is de rotsmuur in oostelijke richting nu laag genoeg om er overheen te klimmen.",
    "richtingen" : "O: Terug naar de voortuin van het huisje \nZ: Het pad volgen naar het zuiden",
    A : "PadLangsHuisje",
    B : "PadLangsRotsmuur",
    C : "Achtertuin",
    D : "PadLangsHuisje",
    E : "PadLangsRotsmuur",
    "items" : [""],
    "benodigdheden" : "machete",
    "acties" : "",
    "dood" : "no",
    "win" : "no"
  },
    "" :{
    "titel" : "",
    "beschrijving" : "",
    "richtingen" : "",
    A : "",
    B : "",
    C : "",
    D : "",
    "items" : [""],
    "benodigdheden" : "",
    "acties" : "",
    "dood" : "",
    "win" : ""
  },
    "" :{
    "titel" : "",
    "beschrijving" : "",
    "richtingen" : "",
    A : "",
    B : "",
    C : "",
    D : "",
    "items" : [""],
    "benodigdheden" : "",
    "acties" : "",
    "dood" : "",
    "win" : ""
  },
    "" :{
    "titel" : "",
    "beschrijving" : "",
    "richtingen" : "",
    A : "",
    B : "",
    C : "",
    D : "",
    "items" : [""],
    "benodigdheden" : "",
    "acties" : "",
    "dood" : "",
    "win" : ""
  },
    "" :{
    "titel" : "",
    "beschrijving" : "",
    "richtingen" : "",
    A : "",
    B : "",
    C : "",
    D : "",
    "items" : [""],
    "benodigdheden" : "",
    "acties" : "",
    "dood" : "",
    "win" : ""
  },
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
  if choice.lower() == "machete":
    kamers[speler.location][Items].remove("machete")
    speler.inventory.append("machete")
    print("je hebt het item opgepakt")
    time.sleep(2)
    print_location()
  elif choice.lower() == "terug":
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
  elif choice.lower() == "machete":
    os.system("clear")
    kamers[speler.location][Items].append("machete")
    speler.inventory.remove("machete")
    print("je hebt het item gedropt")
    time.sleep(2)
    print_location()
  else:
    os.system("clear")
    print("vul een item in dat je bij je hebt!")
    time.sleep(2.5)
    drop()


###DE GAME-LOOP###


#speler verplaatsen
def move_player(move_dest):
	speler.location = move_dest
	print_location()

# print locatie waarbij rekening wordt gehouden of er bij opties is aangezet dat er een typemachine animatie is of niet
def print_location():
  if kamers[speler.location][Dood] == ("no") and kamers[speler.location][Win] == ("no"):
    if kamers[speler.location][Benodigdheden] in speler.inventory:
      os.system('clear')
      print(kamers[speler.location][Titel])
      print("=" * 40)
      if speler.typemachine == "true":
        for char in (kamers[speler.location][Beschrijving]):
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.03)
      elif speler.typemachine == "false":
        print(kamers[speler.location][Beschrijving])
      print("\n"+"=" * 40)
      tekst="Op deze locatie liggen de volgende items: \n"
      if speler.typemachine == "true":
        for char in (tekst):
          sys.stdout.write(char)            
          sys.stdout.flush()
          time.sleep(0.03)
      elif speler.typemachine == "false":
        print(tekst)
      for (i) in (kamers[speler.location][Items]):
        print(i) 
      print("~" * 30)
      Tekst="je kunt de volgende dingen doen: \n"
      if speler.typemachine == "true":
        for char in (Tekst):
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.03)
      elif speler.typemachine == "false":
        print(Tekst)
      if speler.typemachine == "true":
        for char in (kamers[speler.location][Acties]):
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.03)
      elif speler.typemachine == "false":
        print(kamers[speler.location][Acties])
      print("\n"+"~" * 30)
      TEKST="je kunt de volgende richtingen op: \n"
      if speler.typemachine == "true":
        for char in (TEKST):
          sys.stdout.write(char)
          sys.stdout.flush()
        time.sleep(0.03)
      elif speler.typemachine == "false":
        print("je kunt de volgende richtingen op: \n")
      if speler.typemachine == "true":
        for char in (kamers[speler.location][Richtingen]):
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.03)
      elif speler.typemachine == "false":
        print(kamers[speler.location][Richtingen])
      print("\n"+"~" * 30)
      keuze()
    else:
      os.system('clear')
      print("Je hebt een item nodig om naar deze kamer te gaan")
      time.sleep(2)
      move_dest = kamers[speler.location][E]
      move_player(move_dest)
      print_location()
  elif kamers[speler.location][Dood] == ("yes") and speler.health == "100%":
    os.system('clear')
    speler.health = "50%"
    print("=" * 40)
    if speler.typemachine == "true":
      for char in (kamers[speler.location][Beschrijving]):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    elif speler.typemachine == "false":
      print(kamers[speler.location][Beschrijving])
    print("=" * 40)
    time.sleep(8)
    move_dest = kamers[speler.location][A]
    move_player(move_dest)
  elif kamers[speler.location][Dood] == ("yes") and speler.health == "50%":
    os.system('clear')
    print("=" * 40)
    if speler.typemachine == "true":
      for char in (kamers[speler.location][Doodsbeschrijving]):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    elif speler.typemachine == "false":
      print(kamers[speler.location][Doodsbeschrijving])
    print("=" * 40)
    time.sleep(8)
    dood()
  elif kamers[speler.location][Win] == ("yes"):
    os.system('clear')
    print("=" * 40)
    if speler.typemachine == "true":
      for char in (kamers[speler.location][Beschrijving]):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    elif speler.typemachine == "false":
      print(kamers[speler.location][Beschrijving])
    print("=" * 40)

#keuzemenu
def keuze():
  print ('Wat wil je doen?')
  option = input('')
  MogelijkeOpties = "nozw?igdhq"
  if len(option) != 1 or option not in MogelijkeOpties:
    os.system('clear')
    print("Vul aub een geldig antwoord in!")
    time.sleep(1.5)
    os.system('clear')
    print_location()
    keuze()
  elif option.lower() == "n":
    move_dest = kamers[speler.location][A]
    move_player(move_dest)
  elif option.lower() == "o":
    move_dest = kamers[speler.location][B]
    move_player(move_dest)
  elif option.lower() == "z":
    move_dest = kamers[speler.location][C]
    move_player(move_dest)
  elif option.lower() == "w":
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
  print("============================================= \n|                                           | \n|                                           | \n|     ----------------------------------    | \n|     || Welkom bij de text adventure ||    | \n|     ||    van Sannah en Vincent     ||    | \n|     ----------------------------------    | \n|                 Kies uit:                 | \n|                                           |\n|                  -start                   | \n|                  -stop                    | \n|                  -help                    | \n|                  -opties                  | \n=============================================")
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
  elif choice.lower() == "opties":
    os.system('clear')
    opties()
  else:
    os.system('clear')
    print("============================================= \n|       vul een geldig antwoord in!!!       |")
    hoofdmenu()
                                        

hoofdmenu()