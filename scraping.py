from bs4 import BeautifulSoup
import csv
from urllib.request import urlopen as uReq
import pandas as pd
from matplotlib import pyplot as plt
from collections import Counter
import numpy as np



Urls=['http://dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=3&RegionName=Mumbai' , 'http://www.dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=6&RegionName=Pune' , 'http://www.dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=2&RegionName=Aurangabad','http://dtemaharashtra.gov.in/frmInstituteList.aspx?RegionID=1&RegionName=Amravati' ]



print("***********************WELCOME***********************")
print("WRITING ALL THE DETAILS INTO A CSV FILE.THIS MAY TAKE TIME........")
with open("Engineering_Colleges.csv" , mode="w" , newline="") as csv_file:

        writer=csv.writer(csv_file)

        headers=["COLLEGE-ID" , "COLLEGE" , "ADDRESS" , "DISTRICT" , "EMAIL ADDRESS" , "COLLEGE WEBSITE" , "PRINCIPAL NAME" , "PHONE NO." , "REGISTRAR NAME" , "AUTONOMY STATUS"]

        writer.writerow(headers)



        
        for url in Urls:
        
            client=uReq(url)
            raw_html=client.read()
            client.close()


            soup=BeautifulSoup(raw_html,'lxml')

            table=soup.findAll("table",{"class" : "DataGrid"})



            clg_table=table[0]
            the_list=[]
            for cells in clg_table.findAll("td" , {"class" : "Item"}):
                for links in cells.findAll("a"):
                        hrefs=links.get("href")
                        the_list.append(hrefs)
                        
            while(the_list.count(None)):
                the_list.remove(None)
                       


            
            str1='http://www.dtemaharashtra.gov.in/'
            for i in range(len(the_list)):
                rows=[]


                
                the_list[i]=str1+the_list[i]
                clgUrl=the_list[i]
                client=uReq(clgUrl)
                clgHtml=client.read()
                client.close()

                soup2=BeautifulSoup(clgHtml,'lxml')

                allTable=soup2.findAll("table" , {"class" : "AppFormTable"})

                clgTable=allTable[0]



               
                clg_name=clgTable.findAll("span",{"id":"ctl00_ContentPlaceHolder1_lblInstituteNameEnglish"})[0].text

                clg_id=clgTable.findAll("span",{"id":"ctl00_ContentPlaceHolder1_lblInstituteCode"})[0].text
                    
                if("Engineering" in clg_name or "Technology" in clg_name):

                    if ("Management" not in clg_name and "Pharmacy" not in clg_name and "Polytechnic" not in clg_name):


                        
                        rows.append(clg_id)
                        print(clg_id)


                        rows.append(clg_name)
                        print(clg_name)

                            
                        clg_address=clgTable.findAll("span",{"id":"ctl00_ContentPlaceHolder1_lblAddressEnglish"})[0].text
                        rows.append(clg_address)
                        print(clg_address)


                        clg_district=clgTable.findAll("span",{"id":"ctl00_ContentPlaceHolder1_lblDistrict"})[0].text
                        rows.append(clg_district)
                        print(clg_district)


                        clg_email=clgTable.findAll("span",{"id":"ctl00_ContentPlaceHolder1_lblEMailAddress"})[0].text
                        rows.append(clg_email)
                        print(clg_email)


                        clg_web=clgTable.findAll("span",{"id":"ctl00_ContentPlaceHolder1_lblWebAddress"})[0].text
                        rows.append(clg_web)
                        print(clg_web)


                        clg_principal=clgTable.findAll("span",{"id":"ctl00_ContentPlaceHolder1_lblPrincipalNameEnglish"})[0].text
                        rows.append(clg_principal)
                        print(clg_principal)




                        clg_phone=clgTable.findAll("span",{"id":"ctl00_ContentPlaceHolder1_lblOfficePhoneNo"})[0].text
                        rows.append(clg_phone.split("Ext.-")[0])
                        print(clg_phone.split("Ext.-")[0])


                           

                        clg_reg=clgTable.findAll("span",{"id":"ctl00_ContentPlaceHolder1_lblRegistrarNameEnglish"})[0].text
                        rows.append(clg_reg)
                        print(clg_reg+"\n")


                        clg_autonomy=clgTable.findAll("span",{"id":"ctl00_ContentPlaceHolder1_lblStatus2"})[0].text
                        rows.append(clg_autonomy)

                            

                        
                        writer.writerow(rows)


plt.style.use("ggplot")


Allrecords=pd.read_csv("Engineering_Colleges.csv" , engine='python' )

district=Allrecords['DISTRICT']
distDict=Counter(district)

distList=[]
numberList=[]
for dists in distDict.most_common(10):
    distList.append(dists[0])
    numberList.append(dists[1])
numberList.reverse()
distList.reverse()


ax3,fig3=plt.subplots(figsize=(8,4))
plt.barh(distList,numberList , color='#51eaea')

plt.title("Number of Engineering colleges per district,Maharashtra" , fontsize=11 , fontweight='bold' , fontstyle='italic')
plt.yticks(np.arange(len(distList)), fontsize=9)
plt.xticks( fontsize=9)


plt.xlabel("Number of colleges" , fontsize=11 , fontweight='bold' , labelpad=15)
plt.ylabel("Districts" , fontsize=11 , fontweight='bold' , labelpad=15)

records_mum=Allrecords.iloc[1:68]
records_pune=Allrecords.iloc[68:208]
records_aur=Allrecords.iloc[207:251]
records_ama=Allrecords.iloc[249:278]



autonomous= records_mum.loc[records_mum['AUTONOMY STATUS'] == 'Autonomous'].count()[0]
autonomous1= records_pune.loc[records_pune['AUTONOMY STATUS'] == 'Autonomous'].count()[0]
autonomous2= records_aur.loc[records_aur['AUTONOMY STATUS'] == 'Autonomous'].count()[0]
autonomous3= records_ama.loc[records_ama['AUTONOMY STATUS'] == 'Autonomous'].count()[0]


Nautonomous= records_mum.loc[records_mum['AUTONOMY STATUS'] == 'Non-Autonomous'].count()[0]
Nautonomous1= records_pune.loc[records_pune['AUTONOMY STATUS'] == 'Non-Autonomous'].count()[0]
Nautonomous2= records_aur.loc[records_aur['AUTONOMY STATUS'] == 'Non-Autonomous'].count()[0]
Nautonomous3= records_ama.loc[records_ama['AUTONOMY STATUS'] == 'Non-Autonomous'].count()[0]


the_list=[autonomous , autonomous1, autonomous2 , autonomous3]
the_list2=[Nautonomous , Nautonomous1 , Nautonomous2 ,Nautonomous3 ]
explode=(0.05,0.05,0.03,0.3)
labels='MUMBAI' , 'PUNE' , 'AURANGABAD', 'AMARAVATI'
colors1=['#b0eacd' , '#e71414' , '#5fdde5' ,'#ede682']
colors2=['#8ef6e4','#9896f1','#d59bf6' ,'#ffb0cd']



fig1,ax1=plt.subplots()
plt.title('Autonomous Engineering Colleges in Maharashtra' , fontsize=10)
ax1.pie(the_list, explode=explode, labels=labels , colors=colors1,  autopct='%1.2f%%' , textprops={'fontsize':9} , center=(0,0) , pctdistance=0.85)
cir=plt.Circle((0,0) , 0.7, fc='white')
fig=plt.gcf()
fig.gca().add_artist(cir)

fig2,ax2=plt.subplots()
plt.title('Non-Autonomous Engineering Colleges in Maharashtra' , fontsize=10)
ax2.pie(the_list2, explode=explode, labels=labels , colors=colors2, autopct='%1.2f%%'  , textprops={'fontsize':9} , center=(0,0), pctdistance=0.85)
cir1=plt.Circle((0,0) , 0.7, fc='white')
fig=plt.gcf()
fig.gca().add_artist(cir1)

plt.tight_layout()
plt.show()



        


         
