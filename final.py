import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure

#BAR
df = pd.read_csv(r'C:\Users\SONY\Desktop\ProjektiDAV\heart.csv')

labels = ['0-angina tipike', '1-angina atipike', '3-dhimbje jo anginale', '4-asimptomatike']

male_cp = df.cp[df.sex == 1].value_counts()
female_cp = df.cp[df.sex == 0].value_counts()

#lokacioni i labelave
x = np.arange(len(labels))  
width = 0.35  

#funksion per vendsojen e vlerave numerike mbi cdo bar
def vlera_bar(rects):
    for rect in rects:
        gjatesia = rect.get_height()
        ax.annotate('{}'.format(gjatesia),
                    xy=(rect.get_x() + rect.get_width() / 2, gjatesia),
                    xytext=(0, 3),
                    textcoords="offset points",
                    ha='center', va='bottom')


fig, ax = plt.subplots(figsize=(10,8))
rects1 = ax.bar(x - width/2, male_cp, width, label='Meshkuj')
rects2 = ax.bar(x + width/2, female_cp, width, label='Femra')

ax.set_ylabel('Numri i pacientëve')
ax.set_title('Raporti ne mes te gjinise dhe llojit te dhimbjes se gjoksit')
ax.set_xticks(x)
ax.set_xticklabels(labels)
ax.legend()

vlera_bar(rects1)
vlera_bar(rects2)

fig.tight_layout()

plt.show()
#----------------------------------------------------------------------------
#HBAR
thal_value = df['thal'].value_counts()

labels = ['defekt fiks', 'defekt i kthyeshem', 'normal', 'panjohur']

#lokacioni i labelave
x = np.arange(len(labels))  
width = 0.35  

fig, ax = plt.subplots(figsize=(10,8))
rects1 = ax.barh(x, thal_value, width, color='orange')

ax.set_yticks(x)
ax.set_yticklabels(labels)
ax.invert_yaxis()
ax.set_xlabel('Numri i pacienteve')
ax.set_title('Rezultatet e testit te stresit me Talium te rastet me semundje te zemres')

fig.tight_layout()

plt.show()
#--------------------------------------------------------------------------------
# PIE
labels = 'angina tipike', ' angina jotipike', ' angina jo anginale', 'asimptomatike'
sizes = [20, 15, 20, 45]
colors = ("cyan", "brown", "indigo", "beige")

fig1, ax1 = plt.subplots()
ax1.pie(sizes, labels=labels,colors=colors,wedgeprops={'edgecolor':'black'} ,autopct='%1.1f%%',
        shadow=True, startangle=90)

ax1.axis('equal') 
ax1.set_title("Shpërndarja e dhimbjes në gjoks dhe sëmundja e zemrës",fontsize=15) 

plt.legend(title="Permbajtja", loc="lower right",fontsize=15)
plt.subplots_adjust(left=0.1, bottom=0, right=1.75)
plt.show()

#---------------------------------------------------
# PIE 2
restecg = df['restecg']
labels='Normal','Çrregullim i valës ST-T','Hipertrofi ventrikulare e majtë'
sizes=(147,152,4)
colors=('red','yellow','brown')
normal,abnormal,hypertrophy = 0,0,0
for i in restecg:
  if i == 0:
    normal += 1
  elif i == 1:
    abnormal += 1
  else:
    hypertrophy += 1
    
my_circle = plt.Circle((0, 0), 0.7, color='white')

d = plt.pie(sizes,colors=colors, labels=labels, autopct='%0.1f%%',
            wedgeprops={'edgecolor':'black'},shadow=True ,
            startangle=90, labeldistance=1.05)
fig = plt.gcf()
fig.gca().add_artist(my_circle)
plt.axis('equal')
plt.title("Rezultatet elektrokardiografike të pushimit") 

plt.gca().add_artist(my_circle)

plt.show()     
#--------------------------------------------------------------------------------
#LINE  
plt.plot(df['age'].sort_values(), df['trestbps'], alpha = 0.75, color = 'r', linestyle = '-',
     linewidth = 2) 
plt.title('Shtypja sistolike e gjakut në krahasim me moshën', fontsize=12)
plt.xlabel('Mosha', fontsize=12)
plt.ylabel('Shtypja sistolike e gjakut', fontsize=12)
plt.autoscale(tight='x')
plt.tight_layout()
plt.show()

#--------------------------------------------------------------------------------
#LINE 2
plt.plot(df['age'].sort_values(), df['thalach'], alpha = 0.75, color = 'r', linestyle = '-',
     linewidth = 2) 
plt.title('Maksimumi i rrahjeve të zemrës të arritura në krahasim me moshën', fontsize=12)
plt.xlabel('Mosha', fontsize=12)
plt.ylabel('Rrahjet e zemrës', fontsize=12)
plt.show()
#--------------------------------------------------------------------------------
#SCATTER
x1=df[["age","fbs","trestbps","chol"]]
x2=x1.loc[x1['fbs'] == 1]
x3=x2[["age"]].values
x4=x2[["trestbps"]].values
x5=x1.loc[x1['chol'] > 200]
x6=x5[["age"]].values
x7=x5[["trestbps"]].values

fig = figure(figsize=(10,5))
ax = fig.add_subplot(1, 1, 1)
x8=ax.scatter(x3,x4,40, color = 'b', label="Pacientët me \n nivel glukoze abnormal", marker='X', alpha =.5)
x9=ax.scatter(x6,x7,20, color = 'r', label="Pacientët me \n nivel kolesteroli abnormal", marker='s', alpha = .5)

ticks = ax.set_yticks([100, 120, 140, 160, 180, 200])
labels = ax.set_yticklabels(['100 mmHg', '120 mmHg', '140 mmHg', '160 mmHg', '180 mmHg', '200 mmHg' ]
                             )
figure_title = "Ndyshimi i vlerave të presionit të gjakut sipas moshës te pacientëve me vlera jo-normale të kolesterolit dhe glukozës"

plt.text(0.6, 1.18, figure_title,
         horizontalalignment='center',
         fontsize=15, transform = ax.transAxes, c="#8B0000")
ax.set_xlabel('Mosha', fontsize=14)
ax.set_ylabel('Presioni i gjakut në qetësi', fontsize=14)
ax.legend(bbox_to_anchor=(1.0, 1.02), title='Përmbajtja', fontsize=13)
plt.show()
#----------------------------------------------------------------------------
#SCATTER 1

x1=df[["age","sex","chol"]]
x2=x1.loc[x1['sex'] == 1]
x3=x2[["age"]].values
x4=x2[["chol"]].values
x5=x1.loc[x1['sex'] == 0]
x6=x5[["age"]].values
x7=x5[["chol"]].values

fig = figure(figsize=(10,5))
ax = fig.add_subplot(1, 1, 1)
x8=ax.scatter(x3,x4,30, color = 'g', label="Femra", marker='*', alpha =.5)
x9=ax.scatter(x6,x7,50, color = 'm', label="Meshkuj", marker='+', alpha = .5)

ticks = ax.set_yticks([0,100,200, 300, 400, 500,600])
labels = ax.set_yticklabels(['0', '100 mg/dl', '200 mg/dl', '300 mg/dl', '400 mg/dl', '500 mg/dl', '600 mg/dl' ]
                            )

ax.set_xlabel('Mosha', fontsize=13)
ax.set_ylabel('Niveli i kolesterolit në gjak', fontsize=13)
ax.legend(bbox_to_anchor=(1.2, 1.025), title='Përmbajtja', fontsize=13)

figure_title = "Ndryshimi i vlerave të kolesterolit sipas gjinisë dhe moshës"

plt.text(0.5, 1.18, figure_title,
         horizontalalignment='center',
         fontsize=20, transform = ax.transAxes, c="#0000A0")
plt.show()




