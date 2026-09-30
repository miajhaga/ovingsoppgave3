brus = 24.90
smørbrød = 45
banan = 8.50

totalsum = brus + smørbrød + banan
print("Totalsum", totalsum)

print ("totalsum pluss mva er", totalsum*1.25)
print ("pris per person =", totalsum/4)
print ("Prisforskjell mellom det dyreste og billigste er", smørbrød-banan)

#Siden smørbrød er et heltall, men brus er et desimaltall, vil svaret bli et desimaltall. Derfor blir datatypen gjort om til en float.
#Datatypen delt på fire blir en float, fordi det er desimaltall inkludert. 
#Det er fordel å bruke variabler fordi det effektiviserer prosessen. Det tar mye lengere tid å skrive tallene flere ganger på rad, i tillegg til at det er lettere å holde styr på variablene enn å måtte ha versikt over ulike tall og prosesser når man har flere ting å fokusere på. I tillegg vil variabler være nyttig i tilfelle tallene endrer seg. Vsriabler vi gjøre at totalsummen endres basert på tallene, og at variablene er konstante gjør at man kan effektivt redigere resultatene uten å gå over hele likningen.