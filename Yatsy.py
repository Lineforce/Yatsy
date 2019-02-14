# -*- coding: UTF-8 -*-

import random
import pygame
import os
from sys import exit
_image_library = {}


#värit
musta = (0,0,0)
valk = (255,255,255)
pink = (255, 0, 240)
reb = (255,0,0)




def loppu():
    global klik
    global summa1
    global summa2
    global valittu

    ruutu.blit(get_image('nainen.png'), (100,0))

    if 250 <= hiiri[0] <= 350 and 500 <= hiiri[1] <= 550:   #jeeeeeee
        ruutu.blit(get_image('jeeH.png'), (250,500))
    else:
        ruutu.blit(get_image('jeeE.png'), (250,500))

    if klik==True:
        if 250 <= hiiri[0] <= 350 and 500 <= hiiri[1] <= 550:
            return 1
    


    if summa2>0:
        summaEka= fontti.render((str(summa1)), 800,(pink))
        ruutu.blit(summaEka, (200,400))
        
        summaToka= fontti.render((str(summa2)), 50,(pink))
        ruutu.blit(summaToka, (380,400))
    else:
        summaEka= fontti.render((str(summa1)), 400,(pink))
        ruutu.blit(summaEka, (280,400))




def ykkoset():

    global nopat

    return nopat.count(1) * 1
            
    
def kakkoset():
    
    global nopat

    return nopat.count(2) * 2


    
def kolmoset():
    
    global nopat

    return nopat.count(3) * 3


def neloset():
    
    global nopat

    return nopat.count(4) * 4


def vitoset():
    
    global nopat

    return nopat.count(5) * 5

    
def kutoset():

    global nopat

    return nopat.count(6) * 6



    
def pari():
    
    global nopat
    i = 6

    while i > 0:
        if nopat.count(i) >= 2:
            return i*2
        else:
            i -= 1

    return 0



def kaksi_paria():

    global nopat
    i = 1
    summa = 0
    k = 0

    while i < 7:
        if nopat.count(i) == 2:
            summa += i*2
            k += 1

        if k == 2:
            return summa
        else:
            i += 1

    return 0



 

def kolme_samaa():
    
    global nopat
    i = 1

    while i < 7:
        if nopat.count(i) >= 3:
            return i*3
        else:
            i += 1

    return 0

    
def nelja_samaa():
    
    global nopat
    i = 1

    while i < 7:
        if nopat.count(i) >= 4:
            return i*4
        else:
            i += 1

    return 0


    
def tayskasi():
    
    global nopat
    i = 1
    summa = 0
    x = 0
    y = 0

    while i <= 7:
        if x + y == 2:
            return summa
        if x == 0 and nopat.count(i) == 2:
            summa += i*2
            x = 1
        elif nopat.count(i) == 3:
            summa += i*3
            y = 1
        i += 1
    
    return 0
    
    
def s_suora():
    
    global nopat
    tempNopat = nopat
    tempNopat.sort()
    
    k = 0
    
    while k<5:
        if tempNopat[k] == k+1:
            k += 1
        else:
            return 0
    
    return 15
    
    
def l_suora():
    
    global nopat
    tempNopat = nopat
    tempNopat.sort()
    
    k = 0
    
    while k<5:
        if tempNopat[k] == k+2:
            k += 1
        else:
            return 0
    
    return 20


    
def yatzy():

    global nopat
    i = 1

    while i < 7:
        if nopat.count(i) == 5:
            return 50
        else:
            i += 1

    return 0



def sattuma():
    global nopat
    i=0
    summa = 0
    while i < 5:
        summa += nopat[i]
        i+=1
    
    return summa


def num_tekstiksi():
    return


def bonus():
    global pelaaja1
    global pelaaja2
    global p_no
    global valittu
    summa = 0
    i=0

  
    if p_no == 0:
        summa += pelaaja1['ykkoset']
        summa += pelaaja1['kakkoset']
        summa += pelaaja1['kolmoset']
        summa += pelaaja1['neloset']
        summa += pelaaja1['vitoset']
        summa += pelaaja1['kutoset']
        if summa >= 63:
            pelaaja1['bonus'] = 50 
            return 50
        else:
            pelaaja1['bonus'] = 0
            return 0
    else:
        summa += pelaaja2['ykkoset']
        summa += pelaaja2['kakkoset']
        summa += pelaaja2['kolmoset']
        summa += pelaaja2['neloset']
        summa += pelaaja2['vitoset']
        summa += pelaaja2['kutoset']
            
        if summa >= 63:
            pelaaja2['bonus'] = 50
            return 50
        else:
            pelaaja2['bonus'] = 0
            return 0
    


    
  


def summa():  #etsii myös bonuksen 
    global p_no
    global valinta
    global pelaaja1
    global pelaaja2
    global summa1
    global summa2
    global valittu
    bonus_lista = ['ykkoset', 'kakkoset', 'kolmoset', 'neloset', 'vitoset', 'kutoset']
    global bonus_found_for1 
    global bonus_found_for2 
    bon = 0

            
    if set(bonus_lista).issubset(pelaaja1) and bonus_found_for1==0:
        bon = bonus()
        summa1 += bon
        bonus_found_for1 = 1

        

    if set(bonus_lista).issubset(pelaaja2) and bonus_found_for2==0:
        bon = bonus()
        summa2 += bon
        bonus_found_for2 = 1

    if p_no ==0:
        summa1 += valinta
    else:
        summa2 += valinta
    

            

def piirtaa_tuloksia():
    global pelaaja1
    global pelaaja2
    global p_no
    global summa1
    global summa2
    global valittu

    
    if 'ykkoset' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['ykkoset'])), 20,(valk)), (155, 95))
    if 'kakkoset' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['kakkoset'])), 20,(valk)), (155, 125))
    if 'kolmoset' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['kolmoset'])), 20,(valk)), (155, 155))
    if 'neloset' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['neloset'])), 20,(valk)), (155, 185))
    if 'vitoset' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['vitoset'])), 20,(valk)), (155, 215))
    if 'kutoset' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['kutoset'])), 20,(valk)), (155, 245))
    if 'bonus' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['bonus'])), 20,(pink)), (155, 275))
    if 'pari' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['pari'])), 20,(valk)), (155, 305))
    if 'kaksi paria' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['kaksi paria'])), 20,(valk)), (155, 335))
    if 'kolme samaa' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['kolme samaa'])), 20,(valk)), (155, 365))
    if 'nelja samaa' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['nelja samaa'])), 20,(valk)), (155, 395))
    if 'tayskasi' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['tayskasi'])), 20,(valk)), (155, 425))
    if 's_suora' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['s_suora'])), 20,(valk)), (155, 455))
    if 'l_suora' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['l_suora'])), 20,(valk)), (155, 485))
    if 'yatzy' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['yatzy'])), 20,(reb)), (155, 515))
    if 'sattuma' in pelaaja1:
        ruutu.blit(fontti.render((str(pelaaja1['sattuma'])), 20,(valk)), (155, 545))
    if valittu ==2:
        if 'ykkoset' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['ykkoset'])), 20,(valk)), (390, 95))
        if 'kakkoset' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['kakkoset'])), 20,(valk)), (390, 125))
        if 'kolmoset' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['kolmoset'])), 20,(valk)), (390, 155))
        if 'neloset' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['neloset'])), 20,(valk)), (390, 185))
        if 'vitoset' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['vitoset'])), 20,(valk)), (390, 215))
        if 'kutoset' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['kutoset'])), 20,(valk)), (390, 245))
        if 'bonus' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['bonus'])), 20,(pink)), (390, 275))
        if 'pari' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['pari'])), 20,(valk)), (390, 305))
        if 'kaksi paria' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['kaksi paria'])), 20,(valk)), (390, 335))
        if 'kolme samaa' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['kolme samaa'])), 20,(valk)), (390, 365))
        if 'nelja samaa' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['nelja samaa'])), 20,(valk)), (390, 395))
        if 'tayskasi' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['tayskasi'])), 20,(valk)), (390, 425))
        if 's_suora' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['s_suora'])), 20,(valk)), (390, 455))
        if 'l_suora' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['l_suora'])), 20,(valk)), (390, 485))
        if 'yatzy' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['yatzy'])), 20,(reb)), (390, 515))
        if 'sattuma' in pelaaja2:
            ruutu.blit(fontti.render((str(pelaaja2['sattuma'])), 20,(valk)), (390, 545))

    
    ruutu.blit(fontti.render((str(summa1)), 20,(pink)), (155, 575))

    if valittu == 2:
               
        ruutu.blit(fontti.render((str(summa2)), 20,(pink)), (390, 575))
            
            



def mika_valinta():
    
    global valinta
    global pelaaja1
    global pelaaja2
    global p_no 
    global klik
    
    

    
        
    if 0 <= hiiri[0] <= 600 and 85 <= hiiri[1] <= 115 :
        valinta = ykkoset()
        if p_no ==0 and 'ykkoset' not in pelaaja1:
            pelaaja1['ykkoset'] = valinta
            summa()
            return 1
        elif p_no == 1 and 'ykkoset' not in pelaaja2:
            pelaaja2['ykkoset'] = valinta
            summa()
            return 1
        
    elif 0 <= hiiri[0] <= 600 and 115 <= hiiri[1] <= 145:
        valinta = kakkoset()
        if p_no ==0 and 'kakkoset' not in pelaaja1:
            pelaaja1['kakkoset'] = valinta
            summa()
            return 1
        elif p_no == 1 and 'kakkoset' not in pelaaja2:
            pelaaja2['kakkoset'] = valinta
            summa()
            return 1
        
    elif 0 <= hiiri[0] <= 600 and 145 <= hiiri[1] <= 175:
        valinta = kolmoset()
        if p_no ==0  and 'kolmoset' not in pelaaja1:
            pelaaja1['kolmoset'] = valinta
            summa()
            return 1
        elif p_no == 1 and 'kolmoset' not in pelaaja2:
            pelaaja2['kolmoset'] = valinta
            summa()
            return 1
        
    elif 0 <= hiiri[0] <= 600 and 175 <= hiiri[1] <= 205:
        valinta = neloset()
        if p_no ==0  and 'neloset' not in pelaaja1:
            pelaaja1['neloset'] = valinta
            summa()
            return 1
        elif p_no == 1 and 'neloset' not in pelaaja2:
            pelaaja2['neloset'] = valinta
            summa()
            return 1
        
    elif 0 <= hiiri[0] <= 600 and 205 <= hiiri[1] <= 235:
        valinta = vitoset()
        if p_no ==0 and 'vitoset' not in pelaaja1:
            pelaaja1['vitoset'] = valinta
            summa()
            return 1
        elif p_no == 1 and 'vitoset' not in pelaaja2:
            pelaaja2['vitoset'] = valinta
            summa()
            return 1
        
    elif 0 <= hiiri[0] <= 600 and 235 <= hiiri[1] <= 265:
        valinta = kutoset()
        if p_no ==0 and 'kutoset' not in pelaaja1:
            pelaaja1['kutoset'] = valinta
            summa()
            return 1
        elif p_no == 1 and 'kutoset' not in pelaaja2:
            pelaaja2['kutoset'] = valinta
            summa()
            return 1
        
    elif 0 <= hiiri[0] <= 600 and 295 <= hiiri[1] <= 325:  
        valinta = pari()
        if p_no ==0 and 'pari' not in pelaaja1:
            pelaaja1['pari'] = valinta
            summa()
            return 1
        elif p_no == 1 and 'pari' not in pelaaja2:
            pelaaja2['pari'] = valinta
            summa()
            return 1
        
    elif 0 <= hiiri[0] <= 600 and 325 <= hiiri[1] <= 355:
        valinta = kaksi_paria()
        if p_no ==0 and 'kaksi paria' not in pelaaja1:
            pelaaja1['kaksi paria'] = valinta
            summa()
            return 1
        elif p_no == 1 and 'kaksi paria' not in pelaaja2:
            pelaaja2['kaksi paria'] = valinta
            summa()
            return 1
        
    elif 0 <= hiiri[0] <= 600 and 355 <= hiiri[1] <= 385:
        valinta = kolme_samaa()
        if p_no ==0 and 'kolme samaa' not in pelaaja1:
            pelaaja1['kolme samaa'] = valinta
            summa()
            return 1
        elif p_no == 1 and 'kolme samaa' not in pelaaja2:
            pelaaja2['kolme samaa'] = valinta
            summa()
            return 1
        
    elif 0 <= hiiri[0] <= 600 and 385 <= hiiri[1] <= 415:
        valinta = nelja_samaa()
        if p_no ==0 and 'nelja samaa' not in pelaaja1:
            pelaaja1['nelja samaa'] = valinta
            summa()
            return 1
        elif p_no == 1 and 'nelja samaa' not in pelaaja2:
            pelaaja2['nelja samaa'] = valinta
            summa()
            return 1
        
    elif 0 <= hiiri[0] <= 600 and 415 <= hiiri[1] <= 445:
        valinta = tayskasi()
        if p_no ==0 and 'tayskasi' not in pelaaja1:
            pelaaja1['tayskasi'] = valinta
            summa()
            return 1
        elif p_no == 1 and 'tayskasi' not in pelaaja2:
            pelaaja2['tayskasi'] = valinta
            summa()
            return 1
        
    elif 0 <= hiiri[0] <= 600 and 445 <= hiiri[1] <= 475:
        valinta = s_suora()
        if p_no ==0 and 's_suora' not in pelaaja1:
            pelaaja1['s_suora'] = valinta
            summa()
            return 1
        elif p_no == 1 and 's_suora' not in pelaaja2:
            pelaaja2['s_suora'] = valinta
            summa()
            return 1
        
    elif 0 <= hiiri[0] <= 600 and 475 <= hiiri[1] <= 505:
        valinta = l_suora()
        if p_no ==0 and 'l_suora' not in pelaaja1:
            pelaaja1['l_suora'] = valinta
            summa()
            return 1
        elif p_no == 1 and 'l_suora' not in pelaaja2:
            pelaaja2['l_suora'] = valinta
            summa()
        
            return 1
        
    elif 0 <= hiiri[0] <= 600 and 505 <= hiiri[1] <= 535:
        valinta = yatzy()
        if p_no ==0 and 'yatzy' not in pelaaja1:
            pelaaja1['yatzy'] = valinta
            summa()
            return 1
        elif p_no == 1 and 'yatzy' not in pelaaja2:
            pelaaja2['yatzy'] = valinta
            summa()
        
            return 1
        
    elif 0 <= hiiri[0] <= 600 and 535 <= hiiri[1] <= 565:
        valinta = sattuma()
        if p_no ==0 and 'sattuma' not in pelaaja1:
            pelaaja1['sattuma'] = valinta
            summa()
            return 1
        elif p_no == 1 and 'sattuma' not in pelaaja2:
            pelaaja2['sattuma'] = valinta
            summa()
        
            return 1
        
    return 0
        
    
    


def nopanHeitto():
    return random.randint(1, 6)
    

def noppaKuva(noppa):
    if noppa == 1:
        return 'nro1.png'
    if noppa == 2:
        return 'nro2.png'
    if noppa == 3:
        return 'nro3.png'
    if noppa == 4:
        return 'nro4.png'
    if noppa == 5:
        return 'nro5.png'
    if noppa == 6:
        return 'nro6.png'
    







def pelivuoro():


    global klik
    global nopat
    i = 0
    h = 0
    global kierros
    global vali
    global pidetaan
    
    if kierros < 3:
        if 400 <= hiiri[0] <= 500 and 18 <= hiiri[1] <= 68:   #heitä nappi
            ruutu.blit(get_image('HeitaH.png'), (400,18))
        else:
            ruutu.blit(get_image('HeitaE.png'), (400,18))


    
    if vali ==0 and kierros < 3:
    
        if klik == True:


            
            if 7 <= hiiri[0] <= (78) and 7 <= hiiri[1] <= 71:  #katotaan mitä pidetään
                if 1 not in pidetaan:
                    pidetaan.append(1)
                else:
                    pidetaan.remove(1)
                

                
            if 82 <= hiiri[0] <= (153) and 7 <= hiiri[1] <= 71:  
                if 2 not in pidetaan:
                    pidetaan.append(2)
                else:
                    pidetaan.remove(2)


                

            if 157 <= hiiri[0] <= (228) and 7 <= hiiri[1] <= 71:  
                if 3 not in pidetaan:
                    pidetaan.append(3)
                else:
                    pidetaan.remove(3)

                

            if 232 <= hiiri[0] <= (303) and 7 <= hiiri[1] <= 71:  
                if 4 not in pidetaan:
                    pidetaan.append(4)  
                else:
                    pidetaan.remove(4)

                

            if 307 <= hiiri[0] <= (378) and 7 <= hiiri[1] <= 71:  
                if 5 not in pidetaan:
                    pidetaan.append(5)
                else:
                    pidetaan.remove(5)
                    
            

            if 400 <= hiiri[0] <= 500 and 18 <= hiiri[1] <= 68:  #painaa heitä nappia
                
                i = 0
                tempNopat = []
                while i < 5:      #nopat
                    if (i + 1) not in pidetaan:
                        tempNopat.append(nopanHeitto())
                    else:
                        tempNopat.append(nopat[i])      
                    i+=1
                nopat = tempNopat
                kierros+=1
                


            if 0 <= hiiri[0] < 600 and 95 <= hiiri[1] <= 600 and kierros >0:  #valittee jonkun
                vali = mika_valinta()
                 

    
    
    i=0 
    h=7
    if len(nopat)>i:
        while i <5:
            ruutu.blit(get_image(noppaKuva(nopat[i])), (h, 7))
            h+=75
            i+=1

        n=1
        h=7
        while n<6:
            if n in pidetaan:
                ruutu.blit(get_image('hohto.png'), (h,7)) # hoksaa mitä on jo painettu
            else:
                ruutu.blit(get_image('hohto.png'), (600,600))
            h +=75
            n += 1
                
    
    if vali == 0 and kierros ==3:     #kierros loppuuu
        ruutu.blit(get_image('HeitaE.png'), (400,18))       

        if klik == True:
            if 0 <= hiiri[0] < 600 and 85 <= hiiri[1] <= 600:  #valittee jonkun
                vali = mika_valinta()
                
                
    
    





def peli():
    global valittu
    global tulos
    global p_no
    global vali
    global kierros
    global nopat
    global pidetaan
    global vuosi
    
    txt_lista = ['ykkoset', 'kakkoset', 'kolmoset', 'neloset', 'vitoset', 'kutoset', 'Bonus', 'Pari', 'kaksi paria', 'kolme samaa', 'nelja samaa', 'Tayskasi', 'Pieni suora', 'Iso suora', 'Yatzy', 'Sattuma', 'Summa']
    k = 95
    h = 0
    
    while k < 600: #luo taulukon
        
        pygame.draw.line(ruutu, valk, (0, (k-10)), (600, (k-10)), 1)
        ruutu.blit(fontti.render(txt_lista[h], 20,(valk)), (10, k))
        k+=30
        h+=1
        
    pygame.draw.line(ruutu, valk, (150, 85), (150, (600)), 1)
    
    
    if valittu == 2:
        pygame.draw.line(ruutu, valk, (385, 85), (385, (600)), 1)
        
    
        
    pelivuoro()
    if valittu == 2:
        if p_no == 0:
            if vali ==1:
                vali = 0
                kierros = 0
                p_no = 1
                nopat[:]=[]
                pidetaan[:]=[]


        else:
            if vali ==1:
                vali = 0
                kierros = 0
                p_no = 0
                nopat[:]=[]
                pidetaan[:]=[]
                vuosi+=1
                
    else:
        p_no =0
        if vali ==1:
                vali = 0
                kierros = 0
                nopat[:]=[]
                pidetaan[:]=[]
                vuosi+=1
               
    
    piirtaa_tuloksia()
    print vuosi
    if vuosi ==15:
        return 1




def pelaaja_lkm():
    global valittu
    global klik
    
    ruutu.blit(get_image('yatzy.png'), (10,0))
    
    if 200 >= hiiri[0] >= 100 and 450 >= hiiri[1] >= 400:
        ruutu.blit(get_image('PelaaH.png'), (100,400))
    else:
        ruutu.blit(get_image('PelaaE.png'), (100,400))

    if 500 >= hiiri[0] >= 400 and 450 >= hiiri[1] >= 400:
        ruutu.blit(get_image('LopetaH.png'), (400,400))
    else:
        ruutu.blit(get_image('LopetaE.png'), (400,400))

    



    if valittu == 0:
        

        if 412 <= hiiri[0] <= 492 and 200 <= hiiri[1] <= 280:
            pelaaja2 = ruutu.blit(get_image('pelaaja2VAL.png'), (412,200))
        else:
            pelaaja2 = ruutu.blit(get_image('pelaaja2EI.png'), (412, 200))
        if 112 <= hiiri[0] <= 192 and 200 <= hiiri[1]<= 280:
            pelaaja1 = ruutu.blit(get_image('pelaaja1VAL.png'), (112,200))
        else:
            pelaaja1 = ruutu.blit(get_image('pelaaja1EI.png'), (112,200))

                                  
        if klik == True:
            if 412 <= hiiri[0] <= 492 and 200 <= hiiri[1] <= 280:
                pelaaja2 = ruutu.blit(get_image('pelaaja2VAL.png'), (412,200))
                valittu = 2
            if 112 <= hiiri[0] <= 192 and 200 <= hiiri[1]<= 280:
                pelaaja1 = ruutu.blit(get_image('pelaaja1VAL.png'), (112,200))
                valittu = 1
            
            
            
    elif valittu == 1:

        pelaaja1 = ruutu.blit(get_image('pelaaja1VAL.png'), (112,200))                            
        if 412 <= hiiri[0] <= 492 and 200 <= hiiri[1] <= 280:
            pelaaja2 = ruutu.blit(get_image('pelaaja2VAL.png'), (412,200))
        else:
            pelaaja2 = ruutu.blit(get_image('pelaaja2EI.png'), (412, 200))
    
                                  
        if klik == True:
            if 412 <= hiiri[0] <= 492 and 200 <= hiiri[1] <= 280:
                pelaaja2 = ruutu.blit(get_image('pelaaja2VAL.png'), (412,200))
                valittu = 2
            if 112 <= hiiri[0] <= 192 and 200 <= hiiri[1]<= 280:
                pelaaja1 = ruutu.blit(get_image('pelaaja1VAL.png'), (112,200))
                valittu = 0



    elif valittu == 2:

        pelaaja2 = ruutu.blit(get_image('pelaaja2VAL.png'), (412, 200))
        
        if 112 <= hiiri[0] <= 192 and 200 <= hiiri[1]<= 280:
            pelaaja1 = ruutu.blit(get_image('pelaaja1VAL.png'), (112,200))
        else:
            pelaaja1 = ruutu.blit(get_image('pelaaja1EI.png'), (112,200))

                                  
        if klik == True:
            if 112 <= hiiri[0] <= 192 and 200 <= hiiri[1]<= 280:
                pelaaja1 = ruutu.blit(get_image('pelaaja1VAL.png'), (112,200))
                valittu = 1

            if 412 <= hiiri[0] <= 492 and 200 <= hiiri[1] <= 280:
                pelaaja2 = ruutu.blit(get_image('pelaaja2VAL.png'), (412,200))
                valittu = 0

    if klik == True and valittu > 0:
        if 200 >= hiiri[0] >= 100 and 450 >= hiiri[1] >= 400:
            return valittu   #pelaa napin painallus
    if klik == True:
        if 500 >= hiiri[0] >= 400 and 450 >= hiiri[1] >= 400:
            return 0   #lopeta napin painallus




def menu():
    global klik
    ruutu.blit(get_image('yatzy.png'), (10,0))
    
    
    
    
    if 200 >= hiiri[0] >= 100 and 450 >= hiiri[1] >= 400:
        ruutu.blit(get_image('PelaaH.png'), (100,400))
    else:
        ruutu.blit(get_image('PelaaE.png'), (100,400))

    if 500 >= hiiri[0] >= 400 and 450 >= hiiri[1] >= 400:
        ruutu.blit(get_image('LopetaH.png'), (400,400))
    else:
        ruutu.blit(get_image('LopetaE.png'), (400,400))

    




    
    if klik == True:
        if 200 >= hiiri[0] >= 100 and 450 >= hiiri[1] >= 400:
            return 1   #pelaa napin painallus
        
        if 500 >= hiiri[0] >= 400 and 450 >= hiiri[1] >= 400:
            return 0   #lopeta napin painallus
            
    
                
def get_image(path):
    global _image_library
    image = _image_library.get(path)
    if image == None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image
       





if __name__ == "__main__" :
    pygame.init()
    pygame.font.init()
    fontti = pygame.font.Font('ARCADECLASSIC.ttf',20)

    ruutu = pygame.display.set_mode((600, 600))
    aika = pygame.time.Clock()
    jatsi = True
    
    

    state = 0 # 0 = menu, 1 = pelaaja lkm, 2 = peli, 3 = loppuikkuna
    valittu = 0  #  \/nämä on tässä koska global muuttuja ei toiminut muussa paikkaa
    valinta = 0
    nopat = []
    p_no = 0
    bonus_lista = ['ykkoset', 'kakkoset', 'kolmoset', 'neloset', 'vitoset', 'kutoset']
    pelaaja1 = {}
    pelaaja2 = {}
    summa1 = 0
    summa2 = 0
    kierros = 0
    vali = 0
    pidetaan = []
    bonus_found_for1 = 0
    bonus_found_for2 = 0
    end=0
    vuosi=0
    
    
    
    while jatsi:


        klik = False
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                jatsi = False
            if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                klik = True

        hiiri = pygame.mouse.get_pos()
        

        ruutu.fill(musta)

        if state == 0:
            ekaIkkuna = menu()

            if ekaIkkuna == 0:
                jatsi = False
            elif ekaIkkuna == 1:
                state = 1

        elif state == 1:
            tokaIkkuna = pelaaja_lkm()

            if tokaIkkuna > 0:
                state = 2

            elif tokaIkkuna == 0:
                jatsi = False
            
        elif state == 2:
            tila = peli()
            
            if tila>0:
                state=3


        elif state ==3:
            end = loppu()
            if end==True:
                state =1
                valittu = 0 
                valinta = 0
                nopat = []
                p_no = 0
                pelaaja1 = {}
                pelaaja2 = {}
                summa1 = 0
                summa2 = 0
                kierros = 0
                vali = 0
                pidetaan = []
                bonus_found_for1 = 0
                bonus_found_for2 = 0
                end=0
                vuosi=0
                



        


        pygame.display.update()

    pygame.quit()
        
            
        
        
