from matplotlib import pyplot as plt
import pandas as pd
from collections import Counter
import numpy as np

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
