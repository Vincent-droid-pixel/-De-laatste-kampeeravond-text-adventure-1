import os
import sys
import time

#health
playerhealth = "100%"

#inventory
playerinventory = ["kompas"]

#kamers
kamers = {
  "RivierMetBrug" : {
    "titel" : "een rivier met een brug.",
    "beschrijving" : "Het is een gammele houten brug die naar het noorden over de rivier loopt. Je weet niet of je er eigenlijk wel overheen kunt lopen zonder dat hij doorbreekt. Je ziet ook nog een pad langs het water stroomopwaarts richting het oosten lopen.",
    "windrichtingen" : ["noorden", "oosten"],
    "aangrenzende gebieden" : ["BrugNaarNoorden", "RivierpadNaarOosten"],
    "acties" : ["g (get item)", "d (drop item)", "h (health)", "i (inventory)"],
    "death" : "no",
    "win" : "no"
  },
  "BrugNaarNoorden" : {
    "titel" : "de brug",
    "doodsbeschrijving" : "Je loopt er overheen. De brug breekt door en je valt in het ijskoude water. Je weet er uiteindelijk nog wel uit te klimmen, maar uiteindelijk ga je toch dood door onderkoeling.",
    "nietdoodsbeschrijving" : "Je loopt er overheen. De brug breekt door en je valt in het ijskoude water. Je weet er uiteindelijk nog wel uit te klimmen en overleeft het maar net.",
    "windrichtingen" : "",
    "acties" : "",
    "death" : "yes",
    "win" : "no"
  },
  "RivierpadNaarOosten" :{
    "titel" : "Het rivierpad naar het Oosten",
    "beschrijving" : "Je loopt langs het pad en komt een klein meisje tegen in witte gewaden. Het lijkt bijna alsof ze gloeit zo licht zijn haar gewaden. Zodra het meisje je ziet loopt ze weg richting het zuiden. Je twijfelt of je haar zal volgen of dat je het rivier pad moet volgen.",
    "windrichtingen" : "z, o",
    "acties" : ["g (get item)", "d (drop item)", "h (health)", "i (inventory)"],
    "death" : "no",
    "win" : "no"
  }
}

#inventory laten zien
def inventory():
  print ("                      |- - - - - - - - - - - - - - - -")
  print ("                      |dit heb je op dit moment bij je:")
  print ("                      |",playerinventory)
  print ("                      |-------------------------------")
  time.sleep(3)
  choice = (input("typ wat je wil doen: "))
  if choice ==  "i":
    inventory()
  #elif choice == "g":
  #  getitem()
  #elif choice == "d":
  #  dropitem()
  elif choice == "h":
    health()

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

#health laten zien
def health():
  print ("                      |- - - - - - - - - - - - - - - -")
  print ("                      |dit is hoeveel % health je op dit moment hebt:")
  print ("                      | ",playerhealth)
  print ("                      |-------------------------------")
  time.sleep(3)
  choice = (input("typ wat je wil doen: "))
  if choice ==  "i":
    inventory()
  #elif choice == "g":
  #  getitem()
  #elif choice == "d":
  #  dropitem()
  elif choice == "h":
    health()

#quitmenu
def quit():
  os.system('clear')
  choice = (input("weet je zeker dat je wil stoppen?"))
  if choice.lower == "ja":
    hoofdmenu()
  elif choice.lower == "nee":
    game()
  else:
    print("vul een geldig antwoord in!")
    print("______________________________")
    quit()


#de gameloop
def game(gebied):
  locatie = kamers[gebied]

  #titel en beschrijving van kamer verkrijgen#
  titel = locatie["titel"]
  beschrijving = locatie["beschrijving"]
  #nietdoodsbeschrijving = locatie["nietdoodsbeschrijving"]
  windrichtingen = locatie["windrichtingen"]
  acties = locatie["acties"]
  dood = locatie["death"]
  winnen = locatie["win"]

  #kamer beschrijven
  os.system('clear')
  doodgaan = (dood)


    
  if doodgaan == "no":
    print("=============================================")
    print(f"je bent bij {titel}")
    print(beschrijving)
    print("=============================================")
    print("de windrichtingen waar je heen kan gaan zijn:")
    for (i, w) in enumerate(windrichtingen):
      print (i+1, w)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("de acties die je kunt uitvoeren zijn:")
    for (a) in (acties):
      print(a)
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    #choice = int(input('Typ je keuze:'))
    #(gebied) = "aangrenzende gebieden"[choice - 1]
    choice = (input("typ wat je wil doen: "))
    if choice ==  "i":
      inventory()
    #elif choice == "g":
    #  getitem()
    #elif choice == "d":
    #  dropitem()
    elif choice == "h":
      health()
    elif choice == "q":
      quit()
    else:
      gebied = locatie
      game(gebied)
  elif doodgaan == "yes" and playerhealth == "100%":
    #playerhealth = "50%"
    print(nietdoodsbeschrijving)
  elif doodgaan == "yes" and playerhealth == "50%":
    print(beschrijving)
    time.sleep(5)
    dood()
  



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
    game("RivierMetBrug")
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


class speler:
  def  spelernaam(zelf):
    zelf.naam = ''

speler = speler()




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