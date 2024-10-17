# import necessary tools from the selenium library
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import finder

service = Service()
options = webdriver.ChromeOptions()
options.add_argument("--headless=new")
driver = webdriver.Chrome(service=service, options=options)
name =  input("Enter the Name: ")
episodeNumber = input("Enter the Episode Number : ")
name = finder.GetLastLink(name)
episodeStr = "-episode-" + str(episodeNumber) 
episode = "https://gogoanime.org.es/streaming.php?slug=" + name + episodeStr
driver.get(episode)

element = driver.find_element(By.TAG_NAME,"script")
x = driver.page_source
i =  x.find("https://www")
link = ""
while True:
    if str(x[i:i+4]) in ".m3u8":
        break
    link += x[i]
    i+=1
link += ".m3u8"
print(link)
os.system("vlc " + link)
driver.quit()
