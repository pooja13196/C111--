import plotly.figure_factory as pf
import plotly.graph_objects as pg
import statistics as st
import pandas as pd
import random 

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()
graph = pf.create_distplot([data], ['reading_time'], show_hist=False)
#graph.show()

mean = st.mean(data)
print('PopulationMean: ', mean)
sd = st.stdev(data)
print('PopulationStandardDeviation: ', sd)

def setOfMeans(counter):
    dataset = []
    for i in range(0,counter):
        randomEntries = random.randint(0,len(data)-1)
        value = data[randomEntries]
        dataset.append(value)

    mean = st.mean(dataset)
    return mean

meanList = []
for i in range(0,100):
    randomMean = setOfMeans(30)
    meanList.append(randomMean)

sampleMean = st.mean(meanList)
print('SampleMean: ', sampleMean)
sampleSD = st.stdev(meanList)
print('SampleStandardDeviation: ', sampleSD)
graph = pf.create_distplot([meanList], ['medium_data'], show_hist=False)
#graph.show()

firstsdStart, firstsdEnd = sampleMean - sampleSD, sampleMean + sampleSD
secondsdStart, secondsdEnd = sampleMean - (2*sampleSD), sampleMean + (2*sampleSD)
thirdsdStart, thirdsdEnd = sampleMean - (3*sampleSD), sampleMean + (3*sampleSD)
graph = pf.create_distplot([meanList], ['medium_data'], show_hist=False)
graph.add_trace(pg.Scatter(x=[mean, mean], y=[0,0.7], mode = 'lines', name = 'mean'))
graph.add_trace(pg.Scatter(x=[firstsdStart, firstsdStart], y=[0,0.7], mode='lines', name='sd1Start'))
graph.add_trace(pg.Scatter(x=[firstsdEnd, firstsdEnd], y=[0,0.7], mode='lines', name='sd1End'))
graph.add_trace(pg.Scatter(x=[secondsdStart, secondsdStart], y=[0,0.7], mode='lines', name='sd2Start'))
graph.add_trace(pg.Scatter(x=[secondsdEnd, secondsdEnd], y=[0,0.7], mode='lines', name='sd2End'))
graph.add_trace(pg.Scatter(x=[thirdsdStart, thirdsdStart], y=[0,0.7], mode='lines', name='sd3Start'))
graph.add_trace(pg.Scatter(x=[thirdsdEnd, thirdsdEnd], y=[0,0.7], mode='lines', name='sd3End'))
#graph.show()

df = pd.read_csv('medium_data.csv')
data = df['reading_time'].tolist()
meanSample = st.mean(data)
print('meanSample: ', meanSample)
graph = pf.create_distplot([meanList], ['medium_data'], show_hist=False)
graph.add_trace(pg.Scatter(x=[mean, mean], y=[0,0.7], mode = 'lines', name = 'mean'))
graph.add_trace(pg.Scatter(x=[meanSample, meanSample], y=[0,0.7], mode='lines', name='Mean Sample'))
graph.add_trace(pg.Scatter(x=[firstsdEnd, firstsdEnd], y=[0,0.7], mode='lines', name='sd1End'))
graph.show()

zscore = (meanSample - sampleMean)/sampleSD
print('Z-Score is: ', zscore)



