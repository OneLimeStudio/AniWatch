#!/usr/bin/python3
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import finder
import subprocess
#Initialization

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service, options=options)


linkToSite = "https://gogoanime.org.es/streaming.php?slug="
class Anime():
    def __init__(self):
        self.name = ""
        self.episodeNumber = 1
        self.episodeStr = "-episode-" + str(self.episodeNumber)
        self.episode = linkToSite + self.name + self.episodeStr
        self.running = True
        
    def getAnimeName(self):
        self.name = finder.GetLastLink(self.name)
        self.episodeNumber = int(input("Enter the Episode Number : "))
        self.episodeStr = "-episode-" + str(self.episodeNumber)
        self.episode = linkToSite + self.name + self.episodeStr
    
    def changeEpisode(self,isNext):
        if isNext == True:
   
            self.episodeNumber += 1
           
            self.episodeStr = "-episode-" + str(self.episodeNumber)
           
            self.episode = linkToSite + self.name + self.episodeStr
       
            #print(self.episodeNumber)
            #self.episode = self.episode.replace("episode-" + str(self.episodeNumber),"episode-" + str(self.episodeNumber+1) )
            #print(self.episode)
            
        else:
            self.episodeNumber -= 1
            if (self.episodeNumber <= 0 ):
                self.episodeNumber = 1
            self.episodeStr = "-episode-" + str(self.episodeNumber)
            self.episode = linkToSite + self.name + self.episodeStr
    def RunIt(self,driver):
        print(self.episode)
        
        driver.get(self.episode)
        element = driver.find_element(By.TAG_NAME,"script")
        x = driver.page_source
        #i =  x.find("https://www")
        end = x.find(".m3u8")
        while True:
            if str(x[end-4:end]) in "http":
                i = end - 4
                break
            end -=1
        link = ""
        while True:
            if str(x[i:i+4]) in ".m3u8":
                break
            link += x[i]
            i+=1
        link += ".m3u8"  
        #print("link" + link)
        #
        #os.system("vlc " + link)
        subprocess.run("clear")
        subprocess.run(["vlc", str(link)])
        
anime = Anime()
start = True
while anime.running == True:
    if start:
        anime.name = input("Enter the Name: ") 
         
        anime.getAnimeName()
        start = False
    else:
        print("0> Next Episode")
        print("1> Prev Episode")
        print("2> Change Anime")
        print("3> Quit")
        choice = int(input("Enter The Choice : "))
        if choice == 0:
            anime.changeEpisode(True)
        elif choice == 1:
            anime.changeEpisode(False)
        elif choice == 2:
            anime.name = input("Enter the Name: ")
            anime.getAnimeName()
        elif choice == 3:
            break
    
    anime.RunIt(driver)
    
driver.quit()