import math

class Personnummer:

    #constructor körs först när klass objektet initieras
    def __init__(self, persnr):
        self.persnr = persnr
        self.slutsiffra = 0

        multiplicerade = self.multipliceraMed2och1()
        separerade_tal = self.separeraTal(multiplicerade)
        self.adderaTalenSetKontrollSiffra(separerade_tal)

    #funktioner som tillhör en klass kallas för metoder=Methods
    #multipliceraMed2och1() - multiplicerar alla siffror med 2 - 1 osv
    def multipliceraMed2och1(self):
        
        i=0
        listnumbers = []

        for tchar in self.persnr:

            siffra_tchar = int(tchar)

            if i % 2 == 0 :
                siffra_tchar = siffra_tchar * 2
                listnumbers.append(siffra_tchar)
                
            else:
                siffra_tchar = siffra_tchar * 1
                listnumbers.append(siffra_tchar) 
                 
            i+=1
   
        return listnumbers
    #separeraTal() separerar alla tal och lägger i lista
    def separeraTal(self, listnummren):

        i=0
        lista_ensiffriga_tal = []

        for nummer in listnummren:
            #talet är mindre än 10
            if nummer / 10 < 1:
                #tar reda på rest
                rest = nummer % 10
                lista_ensiffriga_tal.append(rest)
            else: #talet är större än 10 och 10talet ska separeras från rest
                #avrundar 10 talet neråt
                tiotal = math.floor(nummer / 10)
                lista_ensiffriga_tal.append(tiotal)

                ental_rest = nummer % 10
                lista_ensiffriga_tal.append(ental_rest)
            
            i += 1

        return lista_ensiffriga_tal
    #adderaTalenSetKontrollSiffra() Adderar alla talen i lista och subtraherar från högre 10tal
    def adderaTalenSetKontrollSiffra(self, list_ensifrigatal):
        
        summan = 0
        #Tar bort kontrollsifran på slutet
        list_ensifrigatal = list_ensifrigatal[ : -1]

        for num in list_ensifrigatal:            
            summan += num

        stortiotal = math.ceil(summan/10)*10
        self.slutsiffra = stortiotal - summan 
    
    #getKontrollSiffra - returnerar kontrollsiffra
    def getKontrollSiffra(self):
        return self.slutsiffra