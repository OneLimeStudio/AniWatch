import bs4
import requests

def GetLastLink(keyword):
    url ="https://gogoanime.org.es/search.html?keyword="
    url = url + keyword
    r = requests.get(url=url)
    soup = bs4.BeautifulSoup(r.content,"html.parser")
    x = soup.find_all("p",{"class": "name"})
    results= []
    i = 0
    for c in x:
        for name in c.findAll('a'):
            link = name.get('href')
            
            link = link.replace("/category/" , "")
            print( str(i) + "> " + link)
            results.append(link)
            i+=1
            
    choice = input("Enter Choice: ")
    return results[int(choice)]

