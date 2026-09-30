alder = 31
aldersgrense = 18
navn = "Michael"
antall_studenter = 30

#Jeg tror svaret blir at  det er true at alder er større en aldersgrense
print (alder > aldersgrense)

#Jeg tror svaret blir True
print (alder == 31)

#Jeg tror svaret blir True
print (alder != aldersgrense)

#Jeg tror svaret blir False
print (alder <= aldersgrense)

#Jeg tror svaret blir true
print (navn == "Michael")

#Jeg tror svaret blir false
print (navn == "michael")

#Jeg tror svaret blir false
print (antall_studenter >= 30)

#Jeg tror svaret blir true
print (alder + 5 > antall_studenter)

#Svar 5 og 6 gir forsjellig svar selv omd e er ganske like, fordi forbokstaven i 5 er stor, og liten i 6. Når man da skriver inn at navnet er noe annet enn måten man har opprinnelig skrevet det på, blir det sett på som false av programmet.
#Forskjellen på = og == er at = viser til en verdi, altså at en variabel får en verdi. == Sammenlikner to verdier, og setter det opp mot true eller false. 
#Jeg tror python følger linjen fra høyre til venstre, og leser ettersom det står i rekkefølge. Derfor tror jeg python tar for seg plusstegnet som er det aritmetiske først, og så sammenligningsoperatøren etterpå.
#True eller false verdier vil være nyttige i et program for at programmet kan ta avgjørelser basert på verdier.