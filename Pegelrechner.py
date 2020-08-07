import math as m
# -*- coding: utf-8 -*-
"""
Created on Mon Aug  3 14:12:29 2020

@author: Alexander
"""


print ("Wilkommen zum Pegelrechner V 1.0.0!")

p_0 = pow(10,-5)*2
ende=False

while ende == False:
    pegelwerte=[]
    gesamtpegel = 0
    druckwerte = []
    wichtungen = []
    gesamtwichtung = 0

    pegelwerte_ = input("Geben Sie die Pegelwerte in der Form L1,L2,...Ln ein. Nichts eingeben zum beenden\n").split(",")
    if pegelwerte_ == ['']:
        ende = True 
    else:
        wichtungen_ = input("Geben Sie die Wichtungsfaktoren(unnormiert) ein. Z.B: t1,t2,t3.Nichts eingeben zur Berechnung ohne Wichtungen\n").split(",")
    
        for a in pegelwerte_: pegelwerte.append(float(a))
    

        if wichtungen_ !=['']:
            
            for a in wichtungen_: wichtungen.append(float(a))
            for a in wichtungen: gesamtwichtung += a 
            for a in range (0,len(wichtungen),1): wichtungen[a]=wichtungen[a]/gesamtwichtung
            
            for a in range(0,len(pegelwerte),1):
                i=pegelwerte[a]
                j=wichtungen[a]
                gesamtpegel += pow(10,i/10)*j
                
            print ("Pegelmittelwert:      ",format(10*m.log10(gesamtpegel),'3f'),"dB")
        
        else:         
            for a in pegelwerte:
                druckwerte.append(round(p_0*pow(10,a/20),3))
                gesamtpegel +=pow(10,a/10)
                
            schallmittelwert = gesamtpegel/len(pegelwerte)
            gesamtpegel = 10* m.log10(gesamtpegel)
            schallmittelwert = 10* m.log10(schallmittelwert)
                
            print ("Pegelmittelwert:  ",format(schallmittelwert,'.3f'),"dB")
            print ("Gesamtpegel:      ",format(gesamtpegel,'3f'),"dB")
            print ("Schalldruckwerte: ",druckwerte, "Pa")
            
print("=====Programm beendet====")            