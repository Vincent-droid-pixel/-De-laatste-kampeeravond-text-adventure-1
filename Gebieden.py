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

#kamers
kamers = {
    #alles voordat je het huisje in gaat#
    "RivierMetBrug": {
        "titel": "Een rivier met een brug.",
        "beschrijving":
        "Het is een gammele houten brug die naar het noorden over de rivier loopt. \nJe weet niet of je er eigenlijk wel overheen kunt lopen zonder dat hij doorbreekt. \nJe ziet ook nog een pad langs het water stroomopwaarts richting het oosten lopen.",
        "beschrijving2": "",
        "richtingen":
        "N: De brug naar het noorden \nO: Het rivierpad naar het oosten",
        A: "BrugNaarNoorden",
        B: "StenenPlein",
        C: "RivierMetBrug",
        D: "RivierMetBrug",
        "items": [""],
        "benodigdheden": "kompas",
        "acties":
        "d (drop item) \nu (use) \nh (health) \ni (inventory) \n? (help) \nq (quit) \n/ (opties)",
        "dood": "no",
        "win": "no"
    },
    "BrugNaarNoorden": {
        "titel": "De brug",
        "doodsbeschrijving":
        "Je loopt er overheen. De brug breekt door en je valt in het ijskoude water. Je weet er uiteindelijk nog wel uit te klimmen, maar uiteindelijk ga je toch dood door onderkoeling.",
        "beschrijving":
        "Je loopt er overheen. De brug breekt door en je valt in het ijskoude water. Je weet er uiteindelijk nog wel uit te klimmen en overleeft het maar net. Je gaat snel terug naar het vorige kruispunt",
        A: "RivierMetBrug",
        "benodigdheden": "kompas",
        "dood": "yes",
        "win": "no"
    },
    "StenenPlein": {
        "titel": "Stenen pleintje",
        "beschrijving":
        "Je loopt langs het pad en komt op een stenen pleintje. je komt een klein meisje tegen in witte gewaden. Het lijkt bijna alsof ze gloeit zo licht zijn haar gewaden. Zodra het meisje je ziet loopt ze weg richting het zuiden. Je twijfelt of je haar zal volgen of dat je het rivier pad moet volgen. Verder zie je ook nog bij een stenen pilaar een EHBO-kit liggen.",
        "beschrijving2": "",
        "richtingen":
        "O: Verder naar het oosten \nZ: Meisje naar zuiden \nW: De rivier bij de brug",
        A: "StenenPlein",
        B: "RotsmuurInOosten",
        C: "MeisjeZuiden",
        D: "RivierMetBrug",
        "items": ["ehbo-kit"],
        "benodigdheden": "kompas",
        "acties":
        "g/d (get/drop item) \nu (use) \nh (health) \ni (inventory) \n? (help) \nq (quit) \n/ (opties)",
        "dood": "no",
        "win": "no"
    },
    "MeisjeZuiden": {
        "titel": "Meisje",
        "doodsbeschrijving":
        "Je komt op een open plaats en ziet het meisje nog net verdwijnen tussen de bosjes. Opeens komt er uit diezelfde bosjes een groot gruwelijk monster (details nog uitwerken). Het monster verslindt je met huid en haar en je gaat dood.",
        "beschrijving":
        "Je komt op een open plaats en ziet het meisje nog net verdwijnen tussen de bosjes. \nOpeens komt er uit diezelfde bosjes een groot gruwelijk monster (details nog uitwerken). \nJe weet net op tijd weg te rennen en komt weer uit bij het rivierpad \n",
        A: "StenenPlein",
        "benodigdheden": "kompas",
        "dood": "yes",
        "win": "no"
    },
    "RotsmuurInOosten": {
        "titel": "Rotsmuur",
        "beschrijving":
        "Je komt bij een stenen helling van een berg die te steil is om te klimmen. \nDaar waar de rots overgaat in het gras zie je iets liggen. \nAls je goed kijkt blijkt het dat het een lijk is. \nMaar het is geen gewoon lijk. \nHet lijk is vastgegroeid aan de rots door een of andere schimmel. \nJe ziet dat het lijk iets in zijn handen heeft. \nHet blijkt een machete te zijn. \nDaarmee kun je planten wegslaan. \nJe kan vanaf hier alleen naar het zuiden want in het noorden loopt de rivier en in het oosten is de rotsmuur.",
        "beschrijving2": "",
        "richtingen":
        "Z: Pad langs de rotsmuur naar het zuiden \nW: Rivierpad in het westen",
        A: "RotsmuurInOosten",
        B: "RotsmuurInOosten",
        C: "PadLangsRotsmuur",
        D: "StenenPlein",
        "items": ["machete"],
        "benodigdheden": "kompas",
        "acties":
        "g/d (get/drop item) \nu (use) \nh (health) \ni (inventory) \n? (help) \nq (quit) \n/ (opties)",
        "dood": "no",
        "win": "no",
    },
    "PadLangsRotsmuur": {
        "titel": "Het pad langs de rotsmuur",
        "beschrijving":
        "Je loopt op het pad en je ziet een verlaten huisje. \nJe loopt er naar toe en je betwijfelt of het wel een goede keuze is om naar binnen te gaan. \nJe denkt bij jezelf: “In horrorfilms zijn dit altijd de plekken waar het fout gaat.” \nDe ingang van het huisje is ten zuiden van jou. \nJe kan ook om het huisje heen via een pad ten westen van jou.",
        "beschrijving2": "",
        "richtingen":
        "N: De Rotsmuur \nO: Op de rotsmuur \nZ: Het huisje in het zuiden binnengaan \nW: Het pad om het huisje heen",
        A: "RotsmuurInOosten",
        B: "OpDeRotsmuur",
        C: "Huisje",
        D: "PadLangsHuisje",
        "items": [""],
        "benodigdheden": "kompas",
        "acties":
        "d (drop item) \nu (use) \nh (health) \ni (inventory) \n? (help) \nq (quit) \n/ (opties)",
        "dood": "no",
        "win": "no"
    },
  "OpDeRotsmuur": {
        "titel": "Op de rotsmuur",
        "beschrijving": "Je loopt richting de rotsmuur. Je bent aan het denken over hoe je deze muur gaat beklimmen. Dan besef je dat je nog dat touw hebt wat je had gevonden achter het huisje. Je klimt over de rotsmuur en staat nu op een hoog stuk grond. In het Noorden zie je een bos waar je een machete voor nodig hebt en in het oosten zie je een vallei.",
        "beschrijving2": "Je staat boven op de rotsmuur. In het westen hangt nogsteeds het touw dat je hebt opgehangen.",
        "richtingen": "N: Bos \nO: Vallei \nW: Pad langs de rotsmuur",
        A: "Bos",
        B: "Vallei",
        C: "OpDeRotsmuur",
        D: "PadLangsRotsmuur",
        "items": [""],
        "benodigdheden": "",
        "acties": "",
        "dood": "no",
        "win": "no"
    },
  "Vallei": {
        "titel": "De vallei",
        "beschrijving": "Je loopt de vallei binnen. Het is er prachtig!!! Je ziet overal eenhoorns en regenbogen. De bomen zijn gemaakt van suikerspin en de meren zijn gevuld met limonade. Het liefts blijf je voor altijd hier. Helaas kan dat niet. Je kan alleen weer naar dezelfde kant als waar je vandaan kwam.",
        "beschrijving2": "",
        "richtingen": "W: Boven op de rotsmuur",
        A: "Vallei",
        B: "Vallei",
        C: "Vallei",
        D: "OpDeRotsmuur",
        "items": ["suikerspin", "chocolade", "lolly's", "eenhoorn"],
        "benodigdheden": "",
        "acties": "g/d (get/drop item) \nu (use) \nh (health) \ni (inventory) \n? (help) \nq (quit) \n/ (opties",
        "dood": "no",
        "win": "no"
    },
  "Bos": {
        "titel": "Het bos",
        "beschrijving": "Je loopt richting het bos. De doornen en uitstekende takken doen je gedachtes niet veel goeds, totdat je bedenkt dat je nog die machete hebt die je gevonden hebt in de grot! “Deze tocht heeft wel lang genoeg geduurd..” denk je. Je gebruikt je laatste beetje kracht en slaat je weg door het bos heen met de machete. Je ziet de de tent waar je vrienden in liggen.",
        "beschrijving2": "",
        "richtingen": "",
        A: "",
        B: "",
        C: "",
        D: "",
        "items": [""],
        "benodigdheden": "machete",
        "acties": "d (drop item) \nu (use) \nh (health) \ni (inventory) \n? (help) \nq (quit) \n/ (opties)",
        "dood": "no",
        "win": "yes"
    },
    #alles vanaf dat je in het huisje komt
    "Huisje": {
        "titel": "In het huisje",
        "beschrijving":
        "Je besluit om naar binnen te gaan. \nBij je eerste stap in het huis hoor je meteen de planken onder je voeten kraken. \nJe vraagt je af hoe oud dit huis eigenlijk is. \nOpeens hoor je een piano spelen in een kamer ten oosten van jou. \nJe weet niet of je daar heen moet gaan, maar misschien vind je dan eindelijk iemand anders in dit vreselijke bos. \nJe kan ook naar het zuiden de trap af naar de kelder.",
        "beschrijving2": "",
        "richtingen":
        "N: Het huisje uit \nO: De kamer met de pianomuziek \nZ: De keldertrap af",
        A: "PadLangsRotsmuur",
        B: "Pianokamer",
        C: "Kelder",
        D: "Huisje",
        "items": [""],
        "benodigdheden": "kompas",
        "acties":
        "d (drop item) \nu (use) \nh (health) \ni (inventory) \n? (help) \nq (quit) \n/ (opties)",
        "dood": "no",
        "win": "no"
    },
    "Kelder": {
        "titel": "De kelder",
        "beschrijving":
        "Je staat in de kelder. Je ziet hier wat botten liggen en wat tonnen waarvan je hoopt dat er gewoon wijn in zit en geen bloed. (Oh wat heb je toch een grote fantasie.) Verder zie je als je goed kijkt opeens een tunnel aan de andere kant van de kelder. Het ziet er erg donker uit",
        "beschrijving2": "",
        "richtingen": "N: Weer uit de kelder \n Z: De donkere tunnel in",
        A: "Huisje",
        B: "Kelder",
        C: "Tunnel",
        D: "Kelder",
        "items": [""],
        "benodigdheden": "kompas",
        "acties":
        "d (drop item) \nu (use) \nh (health) \ni (inventory) \n? (help) \nq (quit) \n/ (opties)",
        "dood": "no",
        "win": "no"
    },
    "Pianokamer": {
        "titel": "De pianokamer",
        "beschrijving":
        "Je loopt de kamer voorzichtig in en je ziet een platenspeler spelen. Daar kwam de pianomuziek dus vandaan! Maar wie heeft die plaat erop gelegd? Er zijn geen andere uitgangen uit de kamer behalve de deuropening waar je doorheen bent gekomen. Verder zie je een tafel met een zaklamp erop liggen.",
        "beschrijving2": "",
        "richtingen": "W: De ingang van het huisje",
        A: "Pianokamer",
        B: "Pianokamer",
        C: "Pianokamer",
        D: "Huisje",
        "items": ["zaklamp"],
        "benodigdheden": "kompas",
        "acties":
        "g/d (get/drop item) \nu (use) \nh (health) \ni (inventory) \n? (help) \nq (quit) \n/ (opties",
        "dood": "no",
        "win": "no"
    },
    "Tunnel": {
        "titel": "De donkere tunnel",
        "beschrijving":
        "Het is erg donker en je ziet niet waar je heengaat. Gelukkig heb je die zaklamp die je in de pianokamer gevonden hebt. Je klikt op het lichtknopje en ziet nu hoe de tunnel er van binnen uitziet. Overal hangen spinnenwebben en je wil eigenlijk niet te lang in de tunnel blijven. Je ziet geen andere weg dan verder door de tunnel",
        "beschrijving2": "Je staat in de tunnel",
        "richtingen": "N: Terug naar de kelder Z: Verder door de tunnel",
        A: "Kelder",
        B: "Tunnel",
        C: "Grot",
        D: "Tunnel",
        E: "Kelder",
        "items": [""],
        "benodigdheden": "zaklamp",
        "acties":
        "d (drop item) \nu (use) \nh (health) \ni (inventory) \n? (help) \nq (quit) \n/ (opties)",
        "dood": "no",
        "win": "no"
    },
    "Grot": {
        "titel": "De grot",
        "beschrijving":
        "Je wil toch wat verder verkennen. Je loopt een grot in die je door het in het rondte bewegen van je zaklamp kon zien. Je ziet overal plantengroei. Je denkt bij jezelf: 'Hoe kunnen hier benenden zonder zonlicht allemaal planten groeien?' Als je nog verder kijkt zie je in het westen een soort ondergronds meer en in het zuiden...",
        "beschrijving2": "Je staat in de grot.",
        "richtingen": "N: De tunnel \nW: Ondergronds meer \nZ:",
        A: "Tunnel",
        B: "Grot",
        C: "",
        D: "OndergrondsMeer",
        "items": [""],
        "benodigdheden": "",
        "acties": "d (drop item) \nu (use) \nh (health) \ni (inventory) \n? (help) \nq (quit) \n/ (opties)",
        "dood": "no",
        "win": "no"
    },
    "OndergrondsMeer": {
        "titel": "Het ondergrondse meer",
        "beschrijving": "Je loopt naar het ondergrondse meer. Zodra je in het water kijkt lijkt het alsof er een andere wereld is onder het oppervlak. Zodra je het water aanraakt word je erin getrokken. Daarna word je wakker. Het was allemaal een droom... \nNadat je je kleding hebt aangedaan kom je uit je tent, maar als je om je heen kijkt zie je niet de tenten van je vrienden...",
        "beschrijving2": "",
        "richtingen": "",
        A: "OndergrondsMeer",
        B: "OndergrondsMeer",
        C: "OndergrondsMeer",
        D: "OndergrondsMeer",
        "items": [""],
        "benodigdheden": "",
        "acties": "d (drop item) \nu (use) \nh (health) \ni (inventory) \n? (help) \nq (quit) \n/ (opties)",
        "dood": "no",
        "win": "yes"
    },
    #alles vanaf dat je langs het huisje gaat
    "PadLangsHuisje": {
        "titel": "Je bent op het pad naast het huisje",
        "beschrijving":
        "Je bent nu in de achtertuin van het schimmige oude huisje. Er is hier niet veel te vinden, maar er ligt wel een lang stevig touw. Dat zou vast handig kunnen zijn. Opeens hoor je een soort gezang. Het lijkt vanuit zuidelijke richting te komen. Ook is de rotsmuur in oostelijke richting nu laag genoeg om er overheen te klimmen.",
        "beschrijving2": "",
        "richtingen":
        "O: Terug naar de voortuin van het huisje \nZ: Het pad volgen naar het zuiden",
        A: "PadLangsHuisje",
        B: "PadLangsRotsmuur",
        C: "Achtertuin",
        D: "PadLangsHuisje",
        E: "PadLangsRotsmuur",
        "items": ["touw"],
        "benodigdheden": "machete",
        "acties":
        "d (drop item) \nu (use) \nh (health) \ni (inventory) \n? (help) \nq (quit) \n/ (opties)",
        "dood": "no",
        "win": "no"
    },
    "Achtertuin": {
        "titel": "Achtertuin",
        "beschrijving":
        "Je komt op een open veld en het gezang is hier veel duidelijker te horen. Zonder het zelf door te hebben word je gelokt door een sirene. De sirene krijgt het zover je naar haar toe te lokken, zodat je op 1 meter afstand van haar staat. De sirene kijkt met haar witte zielloze ogen naar je. Dan opeens voelt het alsof je moe wordt. En als het eigenlijk al te laat is kom je erachter dat de sirene je ziel aan het opzuigen is.",
        "beschrijving2": "",
        "richtingen": "N: Het pad langs het huisje",
        A: "PadLangsHuisje",
        B: "Achtertuin",
        C: "Achtertuin",
        D: "Achtertuin",
        "items": [""],
        "benodigdheden": "",
        "acties": "",
        "dood": "yes",
        "win": "no"
    },
    "": {
        "titel": "",
        "beschrijving": "",
        "beschrijving2": "",
        "richtingen": "",
        A: "",
        B: "",
        C: "",
        D: "",
        "items": [""],
        "benodigdheden": "",
        "acties": "",
        "dood": "",
        "win": ""
    }
}
