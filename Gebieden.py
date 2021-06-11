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
        "titel": "1. Een rivier met een brug.",
        "beschrijving":
        "Het is een gammele houten brug die naar het noorden over \nde rivier loopt. Je weet niet of je er eigenlijk \nwel overheen kunt lopen zonder dat hij doorbreekt. \nJe ziet ook nog een pad langs het water stroomopwaarts \nrichting het oosten lopen.",
        "beschrijving2": "Je staat bij de rivier met de brug.",
        "richtingen":
        "N: De brug naar het noorden \nO: Het rivierpad naar het oosten",
        A: "BrugNaarNoorden",
        B: "StenenPlein",
        C: "RivierMetBrug",
        D: "RivierMetBrug",
        "items": [""],
        "benodigdheden": "kompas",
        "acties": "d (drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "no",
        "win": "no"
    },
    "BrugNaarNoorden": {
        "titel": "2. De brug",
        "doodsbeschrijving":
        "Je loopt er overheen. De brug breekt door en je valt in het \nijskoude water. Je weet er uiteindelijk nog wel uit te \nklimmen, maar je gaat toch nog dood door onderkoeling.",
        "beschrijving":
        "Je loopt er overheen. De brug breekt door en je valt in het \nijskoude water. Je weet er uiteindelijk nog wel uit te \nklimmen en overleeft het maar net. Je gaat snel terug naar \nhet vorige kruispunt.",
        A: "RivierMetBrug",
        "benodigdheden": "kompas",
        "dood": "yes",
        "win": "no"
    },
    "StenenPlein": {
        "titel": "3. Stenen pleintje",
        "beschrijving":
        "Je loopt langs het pad en komt op een stenen pleintje. Je \nkomt een klein meisje tegen in witte gewaden. Het lijkt \nbijna alsof ze gloeit, zo licht zijn haar gewaden. Zodra het \nmeisje je ziet, loopt ze weg richting het zuiden. Je twijfelt\n of je haar zal volgen of dat je het rivier pad moet volgen. \nVerder zie je ook nog bij een stenen pilaar een EHBO-kit \nliggen.",
        "beschrijving2": "Je staat op het stenen plein.",
        "richtingen":
        "O: Verder naar het oosten \nZ: Meisje naar zuiden \nW: De rivier bij de brug",
        A: "StenenPlein",
        B: "RotsmuurInOosten",
        C: "MeisjeZuiden",
        D: "RivierMetBrug",
        "items": ["ehbo-kit"],
        "benodigdheden": "kompas",
        "acties": "g/d (get/drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "no",
        "win": "no"
    },
    "MeisjeZuiden": {
        "titel": "4. Het meisje",
        "doodsbeschrijving":
        "Je komt op een open plaats en ziet het meisje nog net \nverdwijnen tussen de bosjes. Opeens komt er uit diezelfde \nbosjes een groot gruwelijk monster (details nog uitwerken). \nHet monster verslindt je met huid en haar en je gaat dood.",
        "beschrijving":
        "Je komt op een open plaats en ziet het meisje nog net \nverdwijnen tussen de bosjes. Opeens komt er uit diezelfde \nbosjes een groot gruwelijk monster (details nog uitwerken). \nJe weet net op tijd weg te rennen en komt weer uit bij het \nrivierpad \n",
        A: "StenenPlein",
        "benodigdheden": "kompas",
        "dood": "yes",
        "win": "no"
    },
    "RotsmuurInOosten": {
        "titel": "5. Rotsmuur",
        "beschrijving":
        "Je komt bij een stenen helling van een berg die te steil is \nom te klimmen. Daar waar de rots overgaat in het gras zie je\n iets liggen. Als je goed kijkt blijkt het dat het een lijk \nis. Maar het is geen gewoon lijk. Het lijk is vastgegroeid \naan de rots door een of andere schimmel. Je ziet dat het \nlijk iets in zijn handen heeft. Het blijkt een machete te \nzijn. Daarmee kun je planten wegslaan. Je kan vanaf hier \nalleen naar het zuiden, want in het noorden loopt de rivier \nen in het oosten is de rotsmuur.",
        "beschrijving2": "Je staat bij de rotsmuur",
        "richtingen":
        "Z: Pad langs de rotsmuur naar het zuiden \nW: Rivierpad in het westen",
        A: "RotsmuurInOosten",
        B: "RotsmuurInOosten",
        C: "PadLangsRotsmuur",
        D: "StenenPlein",
        "items": ["machete"],
        "benodigdheden": "kompas",
        "acties": "d (drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "no",
        "win": "no",
    },
    "PadLangsRotsmuur": {
        "titel": "6. Het pad langs de rotsmuur",
        "beschrijving":
        "Je loopt op het pad en je ziet een verlaten huisje. Je loopt\n er naar toe en je betwijfelt of het wel een goede keuze is \nom naar binnen te gaan. Je denkt bij jezelf: “In horrorfilms\n zijn dit altijd de plekken waar het fout gaat.” De ingang \nvan het huisje is ten zuiden van jou. Je kan ook om het \nhuisje heen via een pad ten westen van jou.",
        "beschrijving2": "Je staat op het pad dat langs de rotsmuur loopt.",
        "richtingen":
        "N: De Rotsmuur \nO: Op de rotsmuur \nZ: Het huisje in het zuiden binnengaan \nW: Het pad om het huisje heen",
        A: "RotsmuurInOosten",
        B: "OpDeRotsmuur",
        C: "Huisje",
        D: "PadLangsHuisje",
        "items": [""],
        "benodigdheden": "kompas",
        "acties": "d (drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "no",
        "win": "no"
    },
    #alles vanaf dat je in het huisje komt
    "Huisje": {
        "titel": "7. In het huisje",
        "beschrijving": "Je besluit om naar binnen te gaan. Bij je eerste stap in het\n huis hoor je meteen de planken onder je voeten kraken. Je \nvraagt je af hoe oud dit huis eigenlijk is. Opeens hoor je \neen piano spelen in een kamer ten oosten van jou. Je weet \nniet of je daar heen moet gaan, maar misschien vind je dan \neindelijk iemand anders in dit vreselijke bos. Je kan ook naar \nhet zuiden de trap af naar de kelder.",
        "beschrijving2": "Je staat in het huisje. De planken kraken nog steeds.",
        "richtingen":
        "N: Het huisje uit \nO: De kamer met de pianomuziek \nZ: De keldertrap af",
        A: "PadLangsRotsmuur",
        B: "Pianokamer",
        C: "Kelder",
        D: "Huisje",
        "items": [""],
        "benodigdheden": "kompas",
        "acties": "d (drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "no",
        "win": "no"
    },
    "Pianokamer": {
        "titel": "8. De pianokamer",
        "beschrijving": "Je loopt de kamer voorzichtig in en je ziet een platenspeler\n muziek spelen. Daar kwam de pianomuziek dus vandaan! Maar wie \nheeft die plaat erop gelegd?? Er zijn geen andere uitgangen \nuit de kamer behalve de deuropening waar je doorheen bent \ngekomen. Verder zie je een tafel met een zaklamp erop \nliggen.",
        "beschrijving2": "Je staat in de pianokamer.",
        "richtingen": "W: De ingang van het huisje",
        A: "Pianokamer",
        B: "Pianokamer",
        C: "Pianokamer",
        D: "Huisje",
        "items": ["zaklamp"],
        "benodigdheden": "kompas",
        "acties": "g/d (get/drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "no",
        "win": "no"
    },
    "Kelder": {
        "titel": "9. De kelder",
        "beschrijving": "Je staat in de kelder. Je ziet hier wat botten liggen en wat\n tonnen waarvan je hoopt dat er gewoon wijn in zit en geen \nbloed. (Oh wat heb je toch een grote fantasie.) Verder zie je als \nje goed kijkt opeens een tunnel aan de andere kant \nvan de kelder. Het ziet er erg donker uit.",
        "beschrijving2": "Je staat in de kelder.",
        "richtingen": "N: Weer uit de kelder \nZ: De donkere tunnel in",
        A: "Huisje",
        B: "Kelder",
        C: "Tunnel",
        D: "Kelder",
        "items": [""],
        "benodigdheden": "kompas",
        "acties": "d (drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "no",
        "win": "no"
    },
    "Tunnel": {
        "titel": "10. De donkere tunnel",
        "beschrijving": "Het is erg donker en je ziet niet waar je heengaat. Gelukkig\n heb je die zaklamp die je in de pianokamer gevonden hebt. \nJe klikt op het lichtknopje en ziet nu hoe de tunnel er van \nbinnen uitziet. Overal hangen spinnenwebben en je wil \neigenlijk niet te lang in de tunnel blijven. Je ziet geen \nandere weg dan verder door de tunnel.",
        "beschrijving2": "Je staat in de tunnel",
        "richtingen": "N: Terug naar de kelder \nZ: Verder door de tunnel",
        A: "Kelder",
        B: "Tunnel",
        C: "Grot",
        D: "Tunnel",
        E: "Kelder",
        "items": [""],
        "benodigdheden": "zaklamp",
        "acties": "d (drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "no",
        "win": "no"
    },
    "Grot": {
        "titel": "11. De grot",
        "beschrijving": "Je wil toch wat verder verkennen. Je loopt een grot in die \nje door het in het rondte bewegen van je zaklamp kon zien. \nJe ziet overal plantengroei. Je denkt bij jezelf: 'Hoe \nkunnen hier beneden zonder zonlicht allemaal planten \ngroeien?' Als je nog verder kijkt zie je in het westen een \nsoort ondergronds meer en in het zuiden zie je nog een deel van de grot",
        "beschrijving2": "Je staat in de grot.",
        "richtingen": "N: De tunnel \nW: Ondergronds meer \nZ: Een ander deel van de grot",
        A: "Tunnel",
        B: "Grot",
        C: "SpinnenKamer",
        D: "OndergrondsMeer",
        "items": [""],
        "benodigdheden": "kompas",
        "acties": "d (drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "no",
        "win": "no"
    },
    "SpinnenKamer": {
        "titel": "12. Spinnenkamer",
        "beschrijving": "Je loopt de kamer in. Om je heen hoor je allemaal geluiden. Nadat je je zaklamp hebt aangezet zie je allemaal spinnen! Ze kruipen over je heen en ze bijten je. Ze kruipen zelfs in je mond. Je rent snel weg uit die kamer.",
        "doodsbeschrijving": "Je loopt de kamer in. Om je heen hoor je allemaal geluiden. Nadat je je zaklamp hebt aangezet zie je allemaal spinnen! Ze kruipen over je heen en ze bijten je. Ze kruipen zelfs in je mond. Je wordt langzaam verlamt door het gif totdat je niet meer helder kunt denken. Alles wordt zwart...",
        "richtingen": "",
        A: "Grot",
        "items": [""],
        "benodigdheden": "kompas",
        "acties": "d (drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "yes",
        "win": "no"
    },
    "OndergrondsMeer": {
        "titel": "13. Het ondergrondse meer",
        "beschrijving": "Je loopt naar het ondergrondse meer. Zodra je in het water \nkijkt lijkt het alsof er een andere wereld is onder het \noppervlak. Zodra je het water aanraakt word je erin \ngetrokken. Daarna word je wakker. Het was allemaal een \ndroom... Nadat je je kleding hebt aangedaan kom je uit je \ntent, maar als je om je heen kijkt zie je niet de tenten van\n je vrienden... \nDruk op [enter] om door te gaan.",
        "beschrijving2": "",
        "richtingen": "",
        A: "OndergrondsMeer",
        B: "OndergrondsMeer",
        C: "OndergrondsMeer",
        D: "OndergrondsMeer",
        "items": [""],
        "benodigdheden": "",
        "acties": "d (drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "no",
        "win": "yes"
    },
    #alles vanaf dat je langs het huisje gaat
    "PadLangsHuisje": {
        "titel": "14. De achtertuin van het huisje",
        "beschrijving": "Je bent nu in de achtertuin van het schimmige oude huisje. \nEr is hier niet veel te vinden, maar er ligt wel een lang \nstevig touw. Dat zou vast handig kunnen zijn. Opeens hoor je\n een soort gezang. Het lijkt vanuit zuidelijke richting te \nkomen.",
        "beschrijving2": "Je staat in de achtertuin van het huisje.",
        "richtingen":
        "O: Terug naar de voortuin van het huisje \nZ: Het pad volgen naar het zuiden",
        A: "PadLangsHuisje",
        B: "PadLangsRotsmuur",
        C: "Sirene",
        D: "PadLangsHuisje",
        E: "PadLangsRotsmuur",
        "items": ["touw"],
        "benodigdheden": "machete",
        "acties": "g/d (get/drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "no",
        "win": "no"
    },
    "Sirene": {
        "titel": "15. Sirene",
        "doodsbeschrijving": "Je komt op een open veld en het gezang is hier veel \nduidelijker te horen. Zonder het zelf door te hebben word je\n gelokt door een sirene. De sirene krijgt het zover je naar \nhaar toe te lokken, zodat je op 1 meter afstand van haar \nstaat. De sirene kijkt met haar witte zielloze ogen naar je.\n Dan opeens voelt het alsof je moe wordt. En als het \neigenlijk al te laat is kom je erachter dat de sirene je \nziel aan het opzuigen is.",
        "beschrijving": "Je komt op een open veld en het gezang is hier veel \nduidelijker te horen. Zonder het zelf door te hebben word je\n gelokt door een sirene. De sirene krijgt het zover je naar \nhaar toe te lokken, zodat je op 1 meter afstand van haar \nstaat. De sirene kijkt met haar witte zielloze ogen naar je.\n Dan opeens voelt het alsof je moe wordt. Je kunt \nnet op tijd wegrennen voordat ze je ziel helemaal heeft \nopgezogen.",
        "richtingen": "N: Het pad langs het huisje",
        A: "PadLangsHuisje",
        B: "Sirene",
        C: "Sirene",
        D: "Sirene",
        "items": [""],
        "benodigdheden": "",
        "acties": "",
        "dood": "yes",
        "win": "no"
    },
  "OpDeRotsmuur": {
        "titel": "16. Op de rotsmuur",
        "beschrijving": "Je loopt richting de rotsmuur. Je bent aan het denken over \nhoe je deze muur gaat beklimmen. Dan besef je dat je nog dat\n touw hebt wat je had gevonden achter het huisje. Je klimt \nover de rotsmuur en staat nu op een hoog stuk grond. In het \nNoorden zie je een bos waar je een machete voor nodig hebt \nen in het oosten zie je een vallei.",
        "beschrijving2": "Je staat boven op de rotsmuur. In het westen hangt nog steeds\n het touw dat je hebt opgehangen.",
        "richtingen": "N: Bos \nO: Vallei \nW: Pad langs de rotsmuur",
        A: "Bos",
        B: "Vallei",
        C: "OpDeRotsmuur",
        D: "PadLangsRotsmuur",
        E: "PadLangsRotsmuur",
        "items": [""],
        "benodigdheden": "touw",
        "acties": "d (drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "no",
        "win": "no"
    },
  "Bos": {
        "titel": "17. Het bos",
        "beschrijving": "Je loopt richting het bos. De doornen en uitstekende takken \ndoen je gedachtes niet veel goeds, totdat je bedenkt dat je \nnog die machete hebt die je gevonden hebt in de grot! “Deze \ntocht heeft wel lang genoeg geduurd..” denk je. Je gebruikt \nje laatste beetje kracht en slaat je weg door het bos heen \nmet de machete. Je ziet de de tent waar je vrienden in \nliggen. Je hebt het hele avontuur doorstaan.",
        "beschrijving2": "",
        "richtingen": "",
        A: "",
        B: "",
        C: "",
        D: "",
        E: "OpDeRotsmuur",
        "items": [""],
        "benodigdheden": "machete",
       "acties": "d (drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "no",
        "win": "yes"
    },
  "Vallei": {
        "titel": "18. De vallei",
        "beschrijving": "Je loopt de vallei binnen. Het is er prachtig!!! Je ziet \noveral eenhoorns en regenbogen. De bomen zijn gemaakt van \nsuikerspin en de meren zijn gevuld met limonade. Het liefst \nblijf je voor altijd hier. Helaas kan dat niet. Je kan \nalleen weer naar dezelfde kant als waar je vandaan kwam.",
        "beschrijving2": "Je staat in de vallei. Oh wat een zoete geuren!!!",
        "richtingen": "W: Boven op de rotsmuur",
        A: "Vallei",
        B: "Vallei",
        C: "Vallei",
        D: "OpDeRotsmuur",
        E: "OpDeRotsmuur",
        "items": ["suikerspin", "chocolade", "lolly's", "eenhoorn"],
        "benodigdheden": "kompas",
        "acties": "g/d (get/drop item), u (use), h (health), i (inventory), ? (help), q (quit), / (opties)",
        "dood": "no",
        "win": "no"
    },
}
