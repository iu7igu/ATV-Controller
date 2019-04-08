import pygame
import time
import os
import configparser
import datetime
from sys import platform

config = configparser.ConfigParser()
config.read("atv-raspy.conf")

x, y = (640,480) #Risoluzione della schermata
                

    
if config.get("ATV-Raspy", "Tipo") and config.get("ATV-Raspy", "TestoAbilitato") and config.get("ATV-Raspy", "Reverse") and config.get("ATV-Raspy", "Nominativo") and config.get("ATV-Raspy", "QTH"):

    if config.get("ATV-Raspy", "Tipo").lower() == "barre" :
        pygame.init()
        pygame.font.init()
        pygame.mouse.set_visible(False)  #Nascondo il mouse all'avvio del monoscopio

        z = x

        qrz = pygame.font.SysFont('Liberation Sans', int(z*0.1))   #Imposto il font del QRZ
        testo = pygame.font.SysFont('Liberation Sans', int(z*0.03))  #Imposto il font del testo scorrevole
        orapx = pygame.font.SysFont('Liberation Sans', int(z*0.03))  #Imposto il font del testo scorrevole

        screen =  pygame.display.set_mode((x, y), pygame.FULLSCREEN)  # creo la finestra con le dimensioni x, y in FULLSCREEN
        nominativo = qrz.render(config.get("ATV-Raspy", "Nominativo"), False, (255,255,255)) # creo il testo per il nominativo
        locatore =  qrz.render(config.get("ATV-Raspy", "QTH"), False, (255,255,255)) # creo il testo per il nominativo
        if int(config.get("ATV-Raspy", "TestoAbilitato")):
            testoscorre = testo.render(config.get("ATV-Raspy", "Testo"), False, (0,0,0)) #creo il testo scorrevole
        reverse = int(config.get("ATV-Raspy", "Reverse"))     #Verifico se il reverse è abilitato

        pygame.display.set_caption("Hello World")  #titolo della finestra

        clock = pygame.time.Clock()
        background_image = pygame.image.load(config.get("ATV-Raspy", "sfondobarre")).convert()  # carico l'immagine del monoscopio
        background_image = pygame.transform.scale(background_image,(x, y))    #Scalo l'immagine alle dimensioni della schermata x,y
        
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_q):    # Gestione del comando di chiusura del monoscopio tasto Q
                    pygame.quit()
            screen.blit(background_image, [0,0])  # carico l'immagine del monoscopio come sfondo
            screen.blit(nominativo, (z/2 - z*0.15 - len(config.get("ATV-Raspy", "Nominativo")),y*0.3)) # carico il nominativo
            screen.blit(locatore, (z/2 - z*0.17 - len(config.get("ATV-Raspy", "QTH")),y*0.5)) # carico il nominativo
            if int(config.get("ATV-Raspy", "Orologio")):
                ora = qrz.render(datetime.datetime.utcnow().strftime('%H:%M:%S'), False, (255, 0, 0))
                screen.blit(ora, (z*0.05555 - len(datetime.datetime.utcnow().strftime('%H:%M:%S')),y*0.08333333))
            if reverse: # settaggi per il reverse
                x = x
            else:
                x = 0
            if int(config.get("ATV-Raspy", "TestoAbilitato")):
                screen.blit(testoscorre,(x,y*0.93)) #posiziono il testo scorrevole
                screen.blit(testoscorre,(x-len(config.get("ATV-Raspy", "Testo"))-z*0.7,y*0.93)) # ripeto il testo spostato di tot pixel
            
            pygame.display.update() #stampo a schermo tutti i passaggi precedenti
        
            if reverse:
                x-=float(config.get("ATV-Raspy", "Velocita"))
                if x <= -len(config.get("ATV-Raspy", "Testo"))*2 - z:
                    x=+len(config.get("ATV-Raspy", "Testo")) + z *2
            else:
                x+=float(config.get("ATV-Raspy", "Velocita"))
                if x >= len(config.get("ATV-Raspy", "Testo"))*2 + z*2:
                    x=-len(config.get("ATV-Raspy", "Testo"))-z
      
    if config.get("ATV-Raspy", "Tipo").lower() == "monoscopio" :
        pygame.init()
        pygame.font.init()
        pygame.mouse.set_visible(False)  #Nascondo il mouse all'avvio del monoscopio

        z = x

        qrz = pygame.font.SysFont('Liberation Sans', int(z*0.04200))   #Imposto il font del QRZ
        testo = pygame.font.SysFont('Liberation Sans', int(z*0.03000))  #Imposto il font del testo scorrevole

# Open a window
        screen =  pygame.display.set_mode((x, y), pygame.FULLSCREEN)  # creo la finestra con le dimensioni x, y in FULLSCREEN
        nominativo = qrz.render(config.get("ATV-Raspy", "Nominativo"), False, (255,255,255)) # creo il testo per il nominativo
        locatore =  qrz.render(config.get("ATV-Raspy", "QTH"), False, (255,255,255)) # creo il testo per il nominativo
        if int(config.get("ATV-Raspy", "TestoAbilitato")):
            testoscorre = testo.render(config.get("ATV-Raspy", "Testo"), False, (0,0,0)) #creo il testo scorrevole
        reverse = int(config.get("ATV-Raspy", "Reverse"))     #Verifico se il reverse è abilitato

        pygame.display.set_caption("Hello World")  #titolo della finestra

        clock = pygame.time.Clock()
        background_image = pygame.image.load(config.get("ATV-Raspy", "sfondomono")).convert()  # carico l'immagine del monoscopio
        background_image = pygame.transform.scale(background_image,(x, y))    #Scalo l'immagine alle dimensioni della schermata x,y
        
        while True:
            for event in pygame.event.get():
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_q):    # Gestione del comando di chiusura del monoscopio tasto Q
                    pygame.quit()
            screen.blit(background_image, [0,0])  # carico l'immagine del monoscopio come sfondo
            screen.blit(nominativo, (z/2 - z*0.05555 - len(config.get("ATV-Raspy", "Nominativo")),y*0.08333333)) # carico il nominativo
            screen.blit(locatore, (z/2 - z*0.05555 - len(config.get("ATV-Raspy", "QTH")),y*0.77)) # carico il nominativo
            if int(config.get("ATV-Raspy", "Orologio")):
                ora = qrz.render(datetime.datetime.utcnow().strftime('%H:%M:%S'), False, (255, 0, 0))
                screen.blit(ora, (z*0.05555 - len(datetime.datetime.utcnow().strftime('%H:%M:%S')),y*0.08333333))
            if reverse: # settaggi per il reverse
                x = x
            else:
                x = 0
            if int(config.get("ATV-Raspy", "TestoAbilitato")):
                screen.blit(testoscorre,(x,y*0.93)) #posiziono il testo scorrevole
                screen.blit(testoscorre,(x-len(config.get("ATV-Raspy", "Testo"))-z*0.7,y*0.93)) # ripeto il testo spostato di tot pixel
            
            pygame.display.update() #stampo a schermo tutti i passaggi precedenti
        
            if reverse:
                x-=float(config.get("ATV-Raspy", "Velocita"))
                if x <= -len(config.get("ATV-Raspy", "Testo"))*2 - z:
                    x=+len(config.get("ATV-Raspy", "Testo")) + z *2
            else:
                x+=float(config.get("ATV-Raspy", "Velocita"))
                if x >= len(config.get("ATV-Raspy", "Testo"))*2 + z*2:
                    x=-len(config.get("ATV-Raspy", "Testo"))-z
else:
    print("Verifica il file di configurazione")
    
    
