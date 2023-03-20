import personummer

persnr = input("\nMata personnummer 10 siffror: ")

if (len(persnr) == 10):
    pnr = personummer.Personnummer(persnr)
    slutsiffra = pnr.getKontrollSiffra()
    print("\nBeräknad slutsiffra: " + str(slutsiffra))

    inputkontrollsiffra = persnr[+9 : ]
    
    if (inputkontrollsiffra == str(slutsiffra)):
        print("Kontrollsiffran stämmer!\n")
    else:
        print("Ogiltigt personnummer!\n")

else:
    print("\n 10 st Siffror!")
    


