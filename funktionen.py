import urllib.request

def extrahieren(txt,von,bis):
    erg=[]
    ps=txt.split(von)
    ps.pop(0)
    for p in ps:
        erg1=p.split(bis)[0]
        erg.append(erg1)
    return erg

def sauber(txt):
    repls = ".,;:_!\"'/()[]{}+<>*"
    for r in repls:
        txt = txt.replace(r, " ")
        txt = txt.replace("- "," ")
    while txt.count(" ") > 0:
        txt = txt.replace(" ", " ")
    return txt

def geturl(url):
    from urllib.request import Request, urlopen
    ws = Request(url,headers={'User-Agent': 'Mozilla/5.0'})
    txt = urlopen(ws).read().decode("utf-8") #ws.read().decode("utf-8")
    return txt

def speichern(datei,txt):
    aus = open(datei,"w",encoding="utf-8")
    aus.write(txt)
    aus.close

def sauberleer(txt):
    txt = txt.replace("\t"," ").replace("\n"," ")
    #txt = txt.replace(" ","")
    while txt.count("  "):
        txt = txt.replace("  "," ")
    return txt
