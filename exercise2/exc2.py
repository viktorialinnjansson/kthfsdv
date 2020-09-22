#author: Viktoria Jansson
#email: viktoria.linn.jansson@gmail.com
#last revised: 2020-09-21

import math
import time
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

class Graph():  # a class that that contain information that can be plotted, and methods to plot the information.
    def __init__(self):
        #sets start values for graph
        self.START_TIME = time.time()  
        self.t = 0
        self.function = 0
        self.reCalculates()
        #How the information should be plotted
        self.plot_full_graph = False   #if true only the last n data points will be kept and plotted. 
        self.interval = 1000 #how often the graph should be updated with new data, in milliseconds)
        self.datashown = 20   #How many periods that will be plotted in graph, if not plotting full graph.
        #adds start values to list that will be plotted
        self.functionvalues = [self.function]
        self.timeaxis = [self.t]
        #configures plot
        self.fig = plt.figure() 
        
    
    def letTimePass(self):  #increases the value for the instance variable t
        self.t = time.time() - self.START_TIME

    def reCalculates(self): #calculates the function value for the given time
        self.h = 5 * math.sin((2*math.pi)*self.t)
        self.function = 3 * math.pi * math.exp(-self.h)

    def addNewData(self): #creates new data and appends to the list of current data.
        #new data point
        self.letTimePass()
        self.reCalculates()
        #adds new data point to lists
        self.timeaxis.append(self.t)
        self.functionvalues.append(self.function)
        #if the program is adjusted to not show data from start, removes first data from lists
        if not self.plot_full_graph:  
            if len(self.functionvalues) > self.datashown:
                self.functionvalues.pop(0)
            if len(self.timeaxis) > self.datashown:
                self.timeaxis.pop(0)

    def plotTheFunction(self, i): #creates new data points, clears the plots and re-plots the data.
        self.addNewData()
        plt.cla()
        plt.ylabel("Value of function")
        plt.xlabel('Time (seconds)')
        plt.plot(self.timeaxis, self.functionvalues)

    def updateGraph(self): #updates the plot continuosly which lets the graph be updates in real-time
        self.ani = FuncAnimation(self.fig, self.plotTheFunction, interval=self.interval)        
           

def main():  #creates an instance of Graph and runs it
    littleGraph = Graph()
    littleGraph.updateGraph()
    
    plt.show()


if __name__ == "__main__": 
    main() #runs main function
