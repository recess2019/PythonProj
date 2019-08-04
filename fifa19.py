#libraries used
import pandas as pd #data manipulation
import seaborn as sns #data visualisation
import numpy as np #data
import matplotlib.pyplot as plt #data visualisation

df = pd.read_csv("data.csv")
df.shape
df.head(20)
df.tail(20)
df.nunique()
#Dropping Columns
del df["Photo"]

del df['Flag']
del df['Club Logo']
del df['Body Type']
del df['Real Face']
del df['Contract Valid Until']
del df['Special']
del df['International Reputation']
del df['Skill Moves']
del df['Work Rate']
del df['Jersey Number']
del df['Joined']
del df['Loaned From']
del df['ID']
print(df)

#PLAYER CLUSTERING
#by Nationality
plt.figure(figsize=(10,30))
sns.countplot(y = df.Nationality)
#by Age
plt.figure(figsize=(10,5))
sns.countplot(x="Age", data=df)
#by Positon
plt.figure(figsize=(12,6))
sns.countplot(x = df.Position)

#DREAM TEAM
#weights
a=0.5
b=1
c=2
d=3

#GoalKepping X-tics
df['gk_Shot_Stopper'] = (b*df.Reactions + b*df.Composure+ a*df.SprintSpeed+ a*df.Strength + c*df.Jumping + b*df.GKPositioning + c*df.GKDiving + d*df.GKReflexes + b*df.GKHandling)/(2*a + 4*b + 2*c + 1*d)
df['gk_Sweeper'] = (b*df.Reactions + b*df.Composure + b*df.SprintSpeed + a*df.ShortPassing + a*df.LongPassing + b*df.Jumping + b*df.GKPositioning + b*df.GKDiving + d*df.GKReflexes + b*df.GKHandling + d*df.GKKicking + c*df.Vision)/(2*a + 4*b + 2*c + 1*d)

plt.figure(figsize=(8,5))
#Generate sequential daata and plot
sd1 =df.sort_values('gk_Shot_Stopper', ascending=False)[:5]
x1 = np.array(list(sd1['Name']))
y1 = np.array(list(sd1['gk_Shot_Stopper']))

sns.barplot(x1, y1)
plt.ylabel("Shot Stopping Score")
#Plotting for a Sweeper
plt.figure(figsize=(8,5))
sd = df.sort_values('gk_Sweeper', ascending=False)[:5]
x2 = np.array(list(sd['Name']))
y2 = np.array(list(sd['gk_Sweeper']))
sns.barplot(x2, y2, palette= "colorblind")
plt.ylabel("Sweeping Score")

#Choosing Defenders
df['df_centre_backs'] = ( d*df.Reactions + c*df.Interceptions + d*df.SlidingTackle + d*df.StandingTackle + b*df.Vision+ b*df.Composure + b*df.Crossing +a*df.ShortPassing + b*df.LongPassing+ c*df.Acceleration + b*df.SprintSpeed
+ d*df.Stamina + d*df.Jumping + d*df.HeadingAccuracy + b*df.LongShots + d*df.Marking + c*df.Aggression)/(6*b + 3*c + 7*d)
df['df_wb_Wing_Backs'] = (b*df.BallControl + a*df.Dribbling + a*df.Marking + d*df.SlidingTackle + d*df.StandingTackle + a*df.Positioning + c*df.Vision + c*df.Crossing + b*df.ShortPassing + c*df.LongPassing + d*df.Acceleration +d*df.SprintSpeed + c*df.Stamina + a*df.Finishing)/(4*a + 2*b + 4*c + 4*d)
#CentreBacks
plt.figure(figsize=(8,5))
sd = df[(df['Position'] == 'LCB') | (df['Position'] == 'CB') | (df['Position'] == 'RCB') ].sort_values('df_centre_backs', ascending=False)[:5]
x2 = np.array(list(sd['Name']))
y2 = np.array(list(sd['df_centre_backs']))
sns.barplot(x2, y2, palette=sns.color_palette("Blues_d"))
plt.ylabel("CentreBack Score")
#Left WingBack
plt.figure(figsize=(8,5))
sd = df[(df['Position'] == 'LWB') | (df['Position'] == 'LB')].sort_values('df_wb_Wing_Backs', ascending=False)[:5]
x4 = np.array(list(sd['Name']))
y4 = np.array(list(sd['df_wb_Wing_Backs']))
sns.barplot(x4, y4, palette=sns.color_palette("Blues_d"))
plt.ylabel("Left Back Score")
#Right WingBack
plt.figure(figsize=(8,5))
sd = df[(df['Position'] == 'RWB') | (df['Position'] == 'RB')].sort_values('df_wb_Wing_Backs', ascending=False)[:5]
x5 = np.array(list(sd['Name']))
y5 = np.array(list(sd['df_wb_Wing_Backs']))
sns.barplot(x5, y5, palette=sns.color_palette("Blues_d"))
plt.ylabel("Right Back Score")

#Choosing Midfielders
df['mf_playmaker'] = (d*df.BallControl + d*df.Dribbling + a*df.Marking + d*df.Reactions + d*df.Vision + c*df.Positioning + c*df.Crossing + d*df.ShortPassing + c*df.LongPassing + c*df.Curve + b*df.LongShots + c*df.FKAccuracy)/(1*a + 1*b + 4*c + 4*d)
df['mf_beast'] = (d*df.Agility + c*df.Balance + b*df.Jumping + c*df.Strength + d*df.Stamina + a*df.SprintSpeed + c*df.Acceleration + d*df.ShortPassing + c*df.Aggression + d*df.Reactions + b*df.Marking + b*df.StandingTackle + b*df.SlidingTackle + b*df.Interceptions)/(1*a + 5*b + 4*c + 4*d)
df['mf_controller'] = ( d*df.BallControl + a*df.Dribbling + a*df.Marking + a*df.Reactions + c*df.Vision + c*df.Composure + d*df.ShortPassing + d*df.LongPassing)/(2*c + 3*d + 4*a)
#PlayMaker(RCM)
plt.figure(figsize=(8,5))
ss = df[(df['Position'] == 'CAM') | (df['Position'] == 'RM') | (df['Position'] == 'RAM') | (df['Position'] == 'RCM')].sort_values('mf_playmaker', ascending=False)[:5]
x3 = np.array(list(ss['Name']))
y3 = np.array(list(ss['mf_playmaker']))
sns.barplot(x3, y3, palette=sns.diverging_palette(145, 280, s=85, l=25, n=5))
plt.ylabel("PlayMaker Score")
#Beast(DM)
plt.figure(figsize=(8,5))
ss = df[(df['Position'] == 'RDM') | (df['Position'] == 'CDM') | (df['Position'] == 'LDM')].sort_values('mf_beast', ascending=False)[:5]
x2 = np.array(list(ss['Name']))
y2 = np.array(list(ss['mf_beast']))
sns.barplot(x2, y2, palette=sns.diverging_palette(145, 280, s=85, l=25, n=5))
plt.ylabel("Beast Score")
#Controller(LCM)
plt.figure(figsize=(8,5))
ss = df[(df['Position'] == 'CAM') | (df['Position'] == 'LM')| (df['Position'] == 'LAM') | (df['Position'] == 'LCM')].sort_values('mf_controller', ascending=False)[:5]
x1 = np.array(list(ss['Name']))
y1 = np.array(list(ss['mf_controller']))
sns.barplot(x1, y1, palette=sns.diverging_palette(145, 280, s=85, l=25, n=5))
plt.ylabel("Controller Score")

#Choosing Attackers
#Attacking Attributes
df['att_left_wing'] = (c*df.BallControl + c*df.Dribbling + c*df.SprintSpeed + d*df.Acceleration + b*df.Vision + c*df.Crossing + b*df.ShortPassing + b*df.LongPassing + b*df.Aggression + b*df.Agility + a*df.Curve + c*df.LongShots + b*df.FKAccuracy + d*df.Finishing)/(a + 6*b + 6*c + 2*d)
df['att_right_wing'] = (c*df.BallControl + c*df.Dribbling + c*df.SprintSpeed + d*df.Acceleration + b*df.Vision + c*df.Crossing + b*df.ShortPassing + b*df.LongPassing + b*df.Aggression + b*df.Agility + a*df.Curve + c*df.LongShots + b*df.FKAccuracy + d*df.Finishing)/(a + 6*b + 6*c + 2*d)
df['att_striker'] = (b*df.BallControl + a*df.Vision + b*df.Aggression + b*df.Agility + a*df.Curve + a*df.LongShots + d*df.Balance + d*df.Finishing + d*df.HeadingAccuracy + c*df.Jumping + c*df.Dribbling)/(3*a + 4*b + 2*c + 3*d)
#LEFT WINGER
plt.figure(figsize=(8,5))
ss = df[(df['Position'] == 'LW') | (df['Position'] == 'LS') | (df['Position'] == 'LF')].sort_values('att_left_wing', ascending=False)[:5]
x1 = np.array(list(ss['Name']))
y1 = np.array(list(ss['att_left_wing']))
sns.barplot(x1, y1, palette=sns.diverging_palette(255, 133, l=60, n=5, center="dark"))
plt.ylabel("Left Wing")
#RIGHT WINGER
plt.figure(figsize=(8,5))
ss = df[(df['Position'] == 'RW') | (df['Position'] == 'RS') | (df['Position'] == 'RF')].sort_values('att_right_wing', ascending=False)[:5]
x2 = np.array(list(ss['Name']))
y2 = np.array(list(ss['att_right_wing']))
sns.barplot(x2, y2, palette=sns.diverging_palette(255, 133, l=60, n=5, center="dark"))
plt.ylabel("Right Wing")
#STRIKER
plt.figure(figsize=(8,5))
ss = df[(df['Position'] == 'ST') | (df['Position'] == 'LS') | (df['Position'] == 'RS') | (df['Position'] == 'CF')].sort_values('att_striker', ascending=False)[:5]
x3 = np.array(list(ss['Name']))
y3 = np.array(list(ss['att_striker']))
sns.barplot(x3, y3, palette=sns.diverging_palette(255, 133, l=60, n=5, center="dark"))
plt.ylabel("Striker")

#ATTRIBUTE CORRELATION
df.corr()
f,ax = plt.subplots(figsize=(15,15))
sns.heatmap(df[['Age','Overall', 'Potential', 'Value',
                'Acceleration', 'Aggression', 'Agility', 'Balance', 'BallControl','Composure', 'Crossing','Dribbling', 'FKAccuracy', 'Finishing', 
                'HeadingAccuracy', 'Interceptions','Jumping', 'LongPassing', 'LongShots',
                'Marking', 'Penalties', 'Position', 'Positioning',
                'ShortPassing', 'ShotPower','SlidingTackle',
                'SprintSpeed', 'Stamina', 'StandingTackle', 'Strength', 'Vision',
                'Volleys']].corr(), annot=True, linewidths=0.5, fmt= '.1f',ax=ax, cmap='Blues')
plt.show()


