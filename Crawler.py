import urllib.request
import funktionen


# with open("complete_data.txt", "a") as myfile:
#     myfile.write("Sustainalytics"+"\n")
#
#
# def sustainalytics(int):
#
#     txt_analytics = funktionen.geturl("https://www.sustainalytics.com/esg-ratings?currentpage=1")
#     funktionen.speichern("save_file.html", txt_analytics)
#     i = 1
#     while i < 2:
#         link = "https://www.sustainalytics.com/esg-ratings?industry=&currentpage="+str(i)
#         print(link)
#         txt_analytics = funktionen.geturl(link)
#         print(txt_analytics)
#     # Bearbeiten einer page:
#
#         link = "https://www.sustainalytics.com/"
#         sublinks = funktionen.extrahieren(txt_analytics, 'esg-rating/', '"')
#
#         #aus = open("complete_data.txt","w",encoding = "utf-8")
#
#         for s in sublinks:
#             print(link + "esg-rating/" + s)
#
#             txt_analytics = funktionen.geturl(link + "esg-rating/" + s)
#             funktionen.speichern("subdomains.html", txt_analytics)
#
#
#             data = funktionen.extrahieren(txt_analytics, '<h2 class="">', '</h2>')[0] +  ";" + \
#                    funktionen.extrahieren(txt_analytics, '"col-xs-6 risk-rating-score"><span class="">', '</span></div>')[0] + ";" + \
#                    funktionen.extrahieren(txt_analytics, '<p><strong class="industry-group">', '</strong> <span')[0] + "\n"
#
#             # aus.write(data)
#             with open("complete_data.txt", "a") as myfile:
#                 myfile.write(data)
#
#         i = i+1
#
# #print(sustainalytics(2))


# with open("complete_data.txt", "a") as myfile:
#     myfile.write("\n"+"\n"+"Corporate Human Rights Benchmark"+"\n")


def chrb(int):
    txt_chrb = funktionen.geturl("https://www.worldbenchmarkingalliance.org/publication/chrb/companies/")
    funktionen.speichern("save_chrb.html", txt_chrb)

    link = "https://www.worldbenchmarkingalliance.org/publication/chrb/companies/"
    sublinks = funktionen.extrahieren(txt_chrb, 'https://www.worldbenchmarkingalliance.org/publication/chrb/companies/', '"')

    # aus = open("complete_data.txt","w",encoding = "utf-8")

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



print(chrb(2))