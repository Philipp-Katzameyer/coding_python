import urllib.request

## Relevant functions 
def extrahieren(txt,von,bis):
    erg=[]
    ps=txt.split(von)
    ps.pop(0)
    for p in ps:
        erg1=p.split(bis)[0]
        erg.append(erg1)
    return erg

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


## Crawler
def chrb(int):
    txt_chrb = funktionen.geturl("https://www.worldbenchmarkingalliance.org/publication/chrb/companies/")
    funktionen.speichern("save_chrb.html", txt_chrb)

    link = "https://www.worldbenchmarkingalliance.org/publication/chrb/companies/"
    sublinks = funktionen.extrahieren(txt_chrb, 'https://www.worldbenchmarkingalliance.org/publication/chrb/companies/', '"')

    for s in sublinks:
        print(link + s)

        txt_chrb = funktionen.geturl(link + s)
        txt_chrb = funktionen.sauberleer(txt_chrb)
        funktionen.speichern("subdomains.html", txt_chrb)
        print(txt_chrb)

        txt_summary = funktionen.extrahieren(txt_chrb,'<h2>Summary</h2>','.</p>')
        print(txt_summary)
        txt_summary = txt_summary[0]        #Umwandlung list in string


        if "agricultural products" in txt_summary:
            a1 = "Agricultural Product"
        else: a1 = ""

        if "apparel" in txt_summary:
            a2 = "Apparel"
        else: a2 = ""

        if "automotive manufacturing" in txt_summary:
            a3 = "Automotive Manufacturing"
        else: a3 = ""

        if "extractive " in txt_summary:
            a4 = "Extractive"
        else: a4 = ""

        if " ICT manufacturing" in txt_summary:
            a5 = " ICT Manufacturing"
        else: a5 = ""

        industry= (a1+"|"+a2+"|"+a3+"|"+a4+"|"+a5)

        data = funktionen.extrahieren(txt_chrb, '<h1>', '<')[0] + "|" + \
               funktionen.extrahieren(txt_chrb, '<span class="gauge gauge--small text-color--500"> ', '<span>/26</span> </span> </dd> </span>')[0]
        print(data)


        # aus.write(data)
        with open("complete_data.csv", "a") as myfile:
            myfile.write(data+"|"+industry+"\n")


print(chrb(0)
