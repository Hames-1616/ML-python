import matplotlib.pyplot as plot
import numpy
from scipy import stats
x = numpy.array([12,16,20,24,28,32,36])
y = numpy.array([6,9,12,15,18,21,24])

plot.scatter(x, y)
values = stats.linregress(x,y)
slope = values[0]
intercept = values[1]
Rvalue = values[2]
plot.plot(x,slope*x+intercept) #for displaying the regression line
if intercept>0 : intercept = "+"+str(intercept)
plot.title("R-value = "+str(Rvalue)+" , y = "+str(slope)+"x"+str(intercept))
plot.show()


