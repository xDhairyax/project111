import csv
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics as st 
import random 
import pandas as pd 
import plotly.graph_objects as go 

df=pd.read_csv("data.csv")
data=df["reading_time"].tolist()

def randomsetofmean(counter):
    dataset=[]
    for i in range(0,counter):
        randomindex=random.randint(0,len(data)-1)
        value=data[randomindex]
        dataset.append(value)
        mean=st.mean(dataset)
        return mean

#def showfig(meanlist):
    #df=meanlist
    #mean=st.mean(df)
    #fig=ff.create_distplot([df],["ReadingTime"],show_hist=False)
    #fig.show()


meanlist=[]
for i in range(0,100):
    setofmean=randomsetofmean(30)
    meanlist.append(setofmean)
#showfig(meanlist)

mean=st.mean(meanlist)
print("Sample mean",mean)

mean1=st.mean(data)
print("Population mean",mean1)


standarddeviation=st.stdev(meanlist)
print("standard deviation",standarddeviation)

z_score=mean1-mean/standarddeviation
print("z score is",z_score)

standarddeviationstart,standarddeviationend=mean-standarddeviation,mean+standarddeviation
standarddeviationstart2,standarddeviationend2=mean-(2*standarddeviation),mean+(2*standarddeviation)
standarddeviationstart3,standarddeviationend3=mean-(2+standarddeviation),mean+(3*standarddeviation)
print("sd1",standarddeviationstart,standarddeviationend)
print("sd2",standarddeviationstart2,standarddeviationend2)
print("sd3",standarddeviationstart3,standarddeviationend3)

#fig=ff.create_distplot([meanlist],["ReadingTime"],show_hist=False)
#fig.add_trace(go.Scatter(x=[mean1,mean1],y=[0.06,0.2],mode="lines",name="data"))
#fig.show()

fig=ff.create_distplot([meanlist],["Reading Time"],show_hist=False)
fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="MEAN"))
fig.add_trace(go.Scatter(x=[standarddeviationstart,standarddeviationstart],y=[0,0.17],mode="lines",name="data1"))
fig.add_trace(go.Scatter(x=[standarddeviationend,standarddeviationend],y=[0,0.17],mode="lines",name="data2"))
fig.add_trace(go.Scatter(x=[standarddeviationstart2,standarddeviationstart2],y=[0,0.17],mode="lines",name="data3"))
fig.add_trace(go.Scatter(x=[standarddeviationend2,standarddeviationend2],y=[0,0.17],mode="lines",name="data4"))
fig.add_trace(go.Scatter(x=[standarddeviationstart3,standarddeviationstart3],y=[0,0.17],mode="lines",name="data5"))
fig.add_trace(go.Scatter(x=[standarddeviationend3,standarddeviationend3],y=[0,0.17],mode="lines",name="data6"))
fig.show()