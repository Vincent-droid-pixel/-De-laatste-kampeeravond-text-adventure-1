import os
import sys
import time
from Gebieden import kamers


#TO-do
# - bugs fixen
# - typfouten oplossen
# - (kamers nummeren?)



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
    time.sleep(2)
    os.system('clear')
    hoofdmenu()
  elif choice.lower() == "nee":
    speler.typemachine = "false"
    os.system('clear')
    print("typemachine animatie staat nu uit")
    time.sleep(2)
    os.system('clear')
    hoofdmenu()
  else:
    os.system('clear')
    opties()

def opties_in_game():
  print('=' * 40)
  print("Wil je een typemachine animatie bij de tekst?")
  print("ja/nee")
  print('=' * 40)
  choice = input('')
  if choice.lower() == "ja":
    speler.typemachine = "true"
    os.system('clear')
    print("typemachine animatie staat nu aan")
    time.sleep(2)
    os.system('clear')
    print_location()
  elif choice.lower() == "nee":
    speler.typemachine = "false"
    os.system('clear')
    print("typemachine animatie staat nu uit")
    time.sleep(2)
    os.system('clear')
    print_location()
  else:
    os.system('clear')
    opties()

# Kamers #
Titel = "titel"
Location = "location"
Beschrijving = "beschrijving"
Beschrijving2 = "beschrijving2"
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

#spelerinformatie
class speler:
    def __init__(self):
        self.name = ''
        self.health = "100%"   
        self.inventory = ["kompas"]      
        self.usable = []
        self.location = 'RivierMetBrug'
        self.typemachine = 'true'
        self.bezochteKamers = [""]
        self.gewonnen = "false"
speler = speler()


#inventory laten zien
def inventory():
  os.system('clear')
  print ("- - - - - - - - - - - - - - - - \ndit heb je op dit moment bij je: \n" + str(speler.inventory), "\n-------------------------------")
  time.sleep(3)
  print_location()

#health laten zien
def health():
  os.system('clear')
  print ("- - - - - - - - - - - - - - - - \ndit is hoeveel health je op dit moment hebt: \n",speler.health,"\n-------------------------------")
  time.sleep(3)
  print_location()

#get item functie 
def get():
  os.system("clear")
  print("In deze kamer liggen de volgende items:")
  for i in (kamers[speler.location][Items]):
    print(i)
  print("Welk item wil je oppakken? (of typ [terug] als je terug wil gaan)")
  #welke items je kan oppakken \/
  choice = input("")
  if choice.lower() == "eenhoorn":
    print("je probeert de eenhoorn op te pakken maar hij steekt je met zijn hoorn. Je gaat langzaam dood Druk op [enter] om door te gaan")
    choice = input('')
    if choice.lower() == "":
      dood()
    else:
      dood()
  elif choice.lower() in kamers[speler.location][Items]:
    kamers[speler.location][Items].remove(choice.lower())
    speler.inventory.append(choice.lower())
    speler.usable.append(choice.lower())
    print("je hebt het item opgepakt. Druk op [enter] om verder te gaan")
    choice = input('')
    if choice.lower() == "":
      print_location()
    else:
      print_location()
  elif choice.lower() == "terug":
    print_location()
  else:
    os.system("clear")
    print("vul een item in dat aanwezig is in de kamer!")
    time.sleep(1.5)
    get()

#drop item functie
def drop():
  os.system("clear")
  print("Je hebt de volgende items bij je:")
  for i in (speler.inventory):
    print(i)
  print("welk item wil je droppen?(of typ [terug] om terug te gaan)")
  #welke items je kan droppen \/
  choice = input("")
  if choice.lower() == "kompas":
    os.system("clear")
    print("=" * 40)
    print("Nadat je het kompas hebt weggegooid verdwaal je in het bos en niemand heeft je daarna ooit nog gevonden.")
    print("=" * 40)
    print("Typ [enter] om door te gaan")
    choice = input('')
    if choice.lower() == "":
      dood()
    else:
      dood()
  elif choice.lower() in speler.inventory:
    kamers[speler.location][Items].append(choice.lower())
    speler.inventory.remove(choice.lower())
    speler.usable.remove(choice.lower())
    print("je hebt het item neergelegd in de kamer. Druk op [enter] om verder te gaan")
    choice = input('')
    if choice.lower() == "":
      print_location()
    else:
      print_location()
  elif choice.lower() == "terug":
    print_location()
  else:
    os.system("clear")
    print("vul een item in dat je bij je hebt!")
    time.sleep(1.5)
    drop()


#use item functie#
def use():
  os.system('clear')
  print("Je kunt de volgende items die je bij je hebt gebruiken:")
  for u in [speler.usable]:
    print (u)
  print("Welk item wil je gebruiken? (of typ terug om terug te gaan)")
  choice = input()
  if choice.lower() == "ehbo-kit":
    speler.inventory.remove('EHBO-kit')
    speler.usable.remove('EHBO-kit')
    print("Je hebt de EHBO-kit gebruikt.")
    speler.health = "100%"
    print("Je hebt het item gebruikt. Je health is weer 100%. Druk op [enter] om door te gaan")
    choice = input("")
    if choice.lower() == "":
      print_location()
    else:
      print_location()
  elif choice.lower() == "machete":
    speler.inventory.remove('machete')
    speler.usable.remove('machete')
    print("Je pakt de machete vast. Maar meteen bij je eerste zwaai snij je je arm eraf. Je bloed langzaam dood.")
    dood()
    choice = input("")
    if choice.lower() == "":
      print_location()
    else:
      print_location()
  elif choice.lower() == "terug":
    print_location()
  else:
    print("vul een geldig antwoord in!")
    use()                                      






###DE GAME-LOOP###

# print locatie waarbij rekening wordt gehouden of er bij opties is aangezet dat er een typemachine animatie is of niet. 
#En of een speler al op een locatie is geweest. 
#En of een speler er dood kan gaan of er kan winnen.
def print_location():
  #if-statement kijk of speler dood kan gaan in de kamer
  if kamers[speler.location][Dood] == ("no") and kamers[speler.location][Win] == ("no"):
    #if-statement kijkt of een item nodig is om in kamer te gaan
    if kamers[speler.location][Benodigdheden] in speler.inventory:
      os.system('clear')
      print(kamers[speler.location][Titel])
      print("=" * 40)
      #if-statement kijkt of kamer al een keer is bezocht
      if kamers[speler.location][Titel] not in speler.bezochteKamers:
        #if-statement kijkt of typemachine animatie aan staat
        if speler.typemachine == "true" and kamers[speler.location][Titel] not in speler.bezochteKamers:
          for char in (kamers[speler.location][Beschrijving]):
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(0.03)
        #elif-statement kijkt of typemachine animatie uit staat
        elif speler.typemachine == "false" or kamers[speler.location][Titel] in speler.bezochteKamers:
          print(kamers[speler.location][Beschrijving])
        print("\n"+"=" * 40)
      #elif-statement kijk of speler al wel in kamer is geweest
      elif kamers[speler.location][Titel] in speler.bezochteKamers:
        print(kamers[speler.location][Beschrijving2]) 
        print("\n"+"=" * 40)
      tekst="Op deze locatie liggen de volgende items: \n"
      #if-statement kijkt of typemachine animatie aan staat
      if speler.typemachine == "true" and kamers[speler.location][Titel] not in speler.bezochteKamers:
        for char in (tekst):
          sys.stdout.write(char)            
          sys.stdout.flush()
          time.sleep(0.03)
      #elif-statement kijkt of typemachine animatie uit staat
      elif speler.typemachine == "false" or kamers[speler.location][Titel] in speler.bezochteKamers:
        print(tekst)
      #print de items in een kamer \/
      for (i) in (kamers[speler.location][Items]):
        print(i) 
      print("~" * 30)
      Tekst="je kunt de volgende dingen doen: \n"
      #if-statement kijkt of typemachine animatie aan staat
      if speler.typemachine == "true" and kamers[speler.location][Titel] not in speler.bezochteKamers:
        for char in (Tekst):
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.03)
      #elif-statement kijkt of typemachine animatie uit staat
      elif speler.typemachine == "false" or kamers[speler.location][Titel] in speler.bezochteKamers:
        print(Tekst)
      #if-statement kijkt of typemachine animatie aan staat
      if speler.typemachine == "true" and kamers[speler.location][Titel] not in speler.bezochteKamers:
        for char in (kamers[speler.location][Acties]):
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.03)
      #elif-statement kijkt of typemachine animatie uit staat
      elif speler.typemachine == "false" or kamers[speler.location][Titel] in speler.bezochteKamers:
        print(kamers[speler.location][Acties])
      print("\n"+"~" * 30)
      TEKST="je kunt de volgende richtingen op: \n"
      #if-statement kijkt of typemachine animatie aan staat
      if speler.typemachine == "true" and kamers[speler.location][Titel] not in speler.bezochteKamers:
        for char in (TEKST):
          sys.stdout.write(char)
          sys.stdout.flush()
        time.sleep(0.03)
      #elif-statement kijkt of typemachine animatie uit staat
      elif speler.typemachine == "false" or kamers[speler.location][Titel] in speler.bezochteKamers:
        print("je kunt de volgende richtingen op: \n")
      #if-statement kijkt of typemachine animatie aan staat
      if speler.typemachine == "true" and kamers[speler.location][Titel] not in speler.bezochteKamers:
        for char in (kamers[speler.location][Richtingen]):
          sys.stdout.write(char)
          sys.stdout.flush()
          time.sleep(0.03)
      #elif-statement kijkt of typemachine animatie uit staat
      elif speler.typemachine == "false" or kamers[speler.location][Titel] in speler.bezochteKamers:
        print(kamers[speler.location][Richtingen])
      print("\n"+"~" * 30)
      #start de keuze-functie \/
      if kamers[speler.location][Titel] not in speler.bezochteKamers:
        #voegt de kamer toe aan lijst van bezochte kamers \/
        speler.bezochteKamers.append(kamers[speler.location][Titel])
      keuze()
    ##als er een item nodig is in een kamer:##
    else:
      os.system('clear')
      print("Je hebt een item nodig om naar deze kamer te gaan")
      print("Druk op [enter] om terug te gaan")
      choice = input("")
      if choice.lower() == "":
        move_dest = kamers[speler.location][E]
        move_player(move_dest)
        print_location()
      else:
        move_dest = kamers[speler.location][E]
        move_player(move_dest)
        print_location()
  #elif-statement kijkt of je er dood kan gaan en 100% health hebt
  elif kamers[speler.location][Dood] == ("yes") and speler.health == "100%":
    os.system('clear')
    speler.health = "50%"
    print("=" * 40)
    #if-statement kijkt of typemachine animatie aan staat
    if speler.typemachine == "true":
      for char in (kamers[speler.location][Beschrijving]):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    #elif-statement kijkt of typemachine animatie uit staat
    elif speler.typemachine == "false":
      print(kamers[speler.location][Beschrijving])
    print("=" * 40)
    print("druk [enter] om terug te gaan")
    choice = input('')
    if choice.lower() == "":  
      move_dest = kamers[speler.location][A]
      move_player(move_dest)
    else:
      move_dest = kamers[speler.location][A]
      move_player(move_dest)  
  #elif-statement kijkt of je er dood kunt gaan en 50% health hebt      
  elif kamers[speler.location][Dood] == ("yes") and speler.health == "50%":
    os.system('clear')
    print("=" * 40)
    #if-statement kijkt of typemachine animatie aan staat
    if speler.typemachine == "true":
      for char in (kamers[speler.location][Doodsbeschrijving]):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    #elif-statement kijkt of typemachine animatie uit staat
    elif speler.typemachine == "false":
      print(kamers[speler.location][Doodsbeschrijving])
    print("=" * 40)
    print("Druk op [enter] om door te gaan")
    choice = input('')
    if choice.lower() == "":
      dood()
    else:
      dood()
  #elif statement kijkt of een speler kan winnen in een kamer
  elif kamers[speler.location][Win] == ("yes"):
    os.system('clear')
    print("=" * 40)
    #if-statement kijkt of typemachine animatie aan staat
    if speler.typemachine == "true":
      for char in (kamers[speler.location][Beschrijving]):
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(0.03)
    #elif-statement kijkt of typemachine animatie uit staat
    elif speler.typemachine == "false":
      print(kamers[speler.location][Beschrijving])
    print("=" * 40)
    choice = input('')
    if choice.lower() == "":
      win()
    else:
      win()

#speler verplaatsen
def move_player(move_dest):
  speler.location = move_dest
  print_location()


#keuzemenu
def keuze():
  print ('Wat wil je doen?')
  option = input('')
  MogelijkeOpties = "NnOoZzWw?/IiGgDdHhQqUu"
  if len(option) != 1 or option not in MogelijkeOpties:
    os.system('clear')
    print("Vul aub een geldig antwoord in!")
    time.sleep(1)
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
  elif option.lower() == "/":
    os.system('clear')
    opties_in_game()
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
  elif option.lower() == "u":
    use()
#========================================

#MENU'S#
  
#dood-menu
def dood():
  os.system('clear')
  animation = ["Je", "Je bent", "Je bent dood.","Je bent dood. Bedankt","Je bent dood. Bedankt voor", "Je bent dood. Bedankt voor het", "Je bent dood. bedankt voor het spelen!!!"]
  for x in range(len(animation)):
    time.sleep(0.5)
    sys.stdout.write("\r" + animation[x % len(animation)])
  sys.exit

#win-functie
def win():
  speler.gewonnen = "true"
  print("Yess!!! \nJe hebt het spel uitgespeeld! \nGoed gedaan!")
  i = 1
  while speler.gewonnen == "true" and i < 15:
    os.system('clear')
    print("   _______    ")
    print("  /  . .  \ ")
    print("  | \___/  | ")
    print("  \ ______/")
    print("      |")
    print("     /|\__ ")
    print("   _/ |  ")
    print("     /-\ ")
    print("    /   |")
    print("   |==  |==")
    print("_ _ _ _ _ _ _ _")
    print("   JEFF  ")
    time.sleep(0.2)
    os.system('clear')
    print("   _______    ")
    print("  /  . .  \ ")
    print("  | \___/  | ")
    print("  \ ______/")
    print("      |")
    print("     /|\  ")
    print("    | | | ")
    print("     /-\ ")
    print("    |   | ")
    print("    |== |==")
    print(" _ _ _ _ _ _ _ _")
    print("   JEFF  ")
    time.sleep(0.2)
    os.system('clear')
    print("   _______    ")
    print("  /  . .  \ ")
    print("  | \___/  | ")
    print("  \ ______/")
    print("      |")
    print("   __/|\  ")
    print("      | \_ ")
    print("     /-\ ")
    print("    |   \ ")
    print("    |==  |==")
    print(" _ _ _ _ _ _ _ _")
    print("   JEFF  ")
    time.sleep(0.2)
    os.system('clear')
    print("   _______    ")
    print("  /[0] [0]\ ")
    print("  | /---\  | ")
    print("  | \---/  | ")
    print("  \ ______/")
    print("      |")
    print("   __/|\  ")
    print("      | \_ ")
    print("     /-\ ")
    print("    |   \ ")
    print("    |==  |==")
    print(" _ _ _ _ _ _ _ _")
    print("   JEFF  ")
    time.sleep(0.05)
    i += 1
  os.system('clear')
  print("   _______    ")
  print("  /[0] [0]\ ")
  print("  | /---\  | ")
  print("  | \---/  | ")
  print("  \ ______/")
  print("      |")
  print("   __/|\  ")
  print("      | \_ ")
  print("     /-\ ")
  print("    |   \ ")
  print("    |==  |==")
  print(" _ _ _ _ _ _ _ _")
  print("   JEFF  ")
  time.sleep(2)
  os.system('clear')
  credits()

#creditsmenu
def credits():
  print("\n \n \n \n*Credits*")
  time.sleep(1.5)
  os.system('clear')
  print("\n \n \n*Credits* \nMet dank aan:")
  time.sleep(1.5)
  os.system('clear')
  print("\n \n*Credits* \nMet dank aan: \nSannah Kuip - Voor het meehelpen met de code en het verhaal schrijven")
  time.sleep(1.5)
  os.system('clear')
  print("\n*Credits* \nMet dank aan: \nSannah Kuip - Voor het meehelpen met de code en het verhaal schrijven \nVincent Rink - Voor het schrijven van een groot deel van de code")
  time.sleep(1.5)
  os.system('clear')
  print(f"*Credits* \nMet dank aan: \nSannah Kuip - Voor het meehelpen met de code en het verhaal schrijven \nVincent Rink - Voor het schrijven van een groot deel van de code \n{speler.naam} - voor het spelen van ons spel")
  time.sleep(1.5)
  os.system('clear')
  print(f"Met dank aan: \nSannah Kuip - Voor het meehelpen met de code en het verhaal schrijven \nVincent Rink - Voor het schrijven van een groot deel van de code \n{speler.naam} - voor het spelen van ons spel \nEn...")
  time.sleep(1.5)
  os.system('clear')
  print(f"Sannah Kuip - Voor het meehelpen met de code en het verhaal schrijven \nVincent Rink - Voor het schrijven van een groot deel van de code \n{speler.naam} - voor het spelen van ons spel \nEn... \nTim Logtenberg - voor het geven van deze leuke opdracht")
  time.sleep(1.5)
  os.system('clear')
  print(f"Vincent Rink - Voor het schrijven van een groot deel van de code \n{speler.naam} - voor het spelen van ons spel \nEn... \nTim Logtenberg - voor het geven van deze leuke opdracht")
  time.sleep(1.5)
  os.system('clear')
  print(f"{speler.naam} - voor het spelen van ons spel \nEn... \nTim Logtenberg - voor het geven van deze leuke opdracht")
  time.sleep(1.5)
  os.system('clear')
  print("En... \nTim Logtenberg - voor het geven van deze leuke opdracht")
  time.sleep(1.5)
  os.system('clear')
  print("Tim Logtenberg - voor het geven van deze leuke opdracht")
  time.sleep(3)
  os.system('clear')
  time.sleep(2)
  sys.exit

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
  tekst = "====================================================== \nJe bent gezellig met vrienden aan het kamperen in het bos. \nHelaas kon je niet slapen. \nJe dacht: 'laat ik even een boswandeling maken, zodat ik beter kan slapen.' \nHet enige wat je meeneemt is een kompas. \nNa een kwartier te hebben gelopen kom je opeens tot het besef dat je niet meer weet waar je bent! \nJe denkt bij jezelf: ‘ik moet mijn vrienden terugvinden!’ \n======================================================"
  #if-statement kijkt of typemachine animatie aan staat
  if speler.typemachine == "true":
    for char in (tekst):
      sys.stdout.write(char)            
      sys.stdout.flush()
      time.sleep(0.03)
      #elif-statement kijkt of typemachine animatie uit staat
  elif speler.typemachine == "false":
    print(tekst)


  choice = input(" \nDruk op [enter] als je verder wil gaan: ")
  if choice.lower() == "":
    os.system('clear')
    print_location()
  else:
    os.system('clear')
    print("============================================= \n|       Druk op [enter]!!!       |")
    intro()

#naam-menu
def NaamInvullen():
  print("============================================= \n|                                           | \n|                                           | \n|                                           | \n|              wat is je naam?              | \n|                                           | \n|                                           | \n|                                           | \n=============================================")

  speler_naam = input()
  speler.naam = speler_naam
  if len(speler.naam) == 0:
    print("vul een naam in!")
    time.sleep(1)
    os.system('clear')
    NaamInvullen()
  else:
    format_string = "Hallo %s, leuk dat je deze text adventure speelt!"
    print(format_string % speler.naam)
    if speler.naam == "sannAH":
      win()
    elif speler.naam.lower() == "vinciento":
      win()
    else:
      print("druk op [enter] om door te gaan")
      choice = input('')
      if choice.lower() == "":
        os.system('clear')
        intro()
      else:
        os.system('clear')
        intro()
  
#help-menu voor in een kamer
def help_in_game():
  os.system('clear')
  print("============================================= \nJe hebt verschillende controls in deze text adventure. \nTen eerste kan je met help [?] dit menu zien en met quit [q] kan je stoppen. \nDaarnaast kan je ook nog met opties [/] naar het opties menu. \nVerder kun je met ‘get item [g]’ en ‘drop item [d]’ items oppakken en laten vallen / neerleggen. \nDaarnaast kan je met ‘inventory [i]’ alle items zien die je hebt opgepakt en met use [u] kun je een item gebruiken.  \nOok kan je nog met de gegeven windrichtingen (Noord [n], Oost [o], Zuid [z], West [w]) bij elk gebied, naar het volgende gebied gaan. \nTenslotte kan je met ‘health [h]’ je health zien. \nAl deze controls kan je tijdens het gehele spel gebruiken. \n=============================================")
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
  print("============================================= \nJe hebt verschillende controls in deze text adventure. \nTen eerste kan je met help [?] dit menu zien en met quit [q] kan je stoppen. \nDaarnaast kan je ook nog met opties [/] naar het opties menu. \nVerder kun je met ‘get item [g]’ en ‘drop item [d]’ items oppakken en laten vallen / neerleggen. \nDaarnaast kan je met ‘inventory [i]’ alle items zien die je hebt opgepakt en met use [u] kun je een item gebruiken.  \nOok kan je nog met de gegeven windrichtingen (Noord [n], Oost [o], Zuid [z], West [w]) bij elk gebied, naar het volgende gebied gaan. \nTenslotte kan je met ‘health [h]’ je health zien. \nAl deze controls kan je tijdens het gehele spel gebruiken. \n=============================================")
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
  print("============================================= \n|         DE LAATSTE KAMPEERAVOND           | \n|                                           | \n|     ----------------------------------    | \n|     || Welkom bij de text adventure ||    | \n|     ||    van Sannah en Vincent     ||    | \n|     ----------------------------------    | \n|                 Kies uit:                 | \n|                                           |\n|                  -start                   | \n|                  -stop                    | \n|                  -help                    | \n|                  -opties                  | \n=============================================")
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