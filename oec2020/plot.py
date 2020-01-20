# libraries and data
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import HourParser as parser
import FileReader as fr



def makePlot():
    #Parsing the file to get the values
    times = []
    avWind = []
    avHydro = []
    avGas = []
    avBio = []
    avN = []
    avNuclear = []
    avSolar = []
    maxY = 0
    tickY = []

    for hours in range(23):
        current = fr.getNextHour()
        times.append(parser.getTime(current))
        avWind.append(parser.getAvailableWind(current))
        avHydro.append(parser.getAvailableHydro(current))
        avGas.append(parser.getAvailableGas(current))
        avBio.append(parser.getAvailableBio(current))
        avN.append(parser.getAvailableNeighbour(current))
        avSolar.append(parser.getAvailableSolar(current))
    
    maxY = max(avWind + avNuclear + avN + avHydro + avGas + avBio)



    #Plot all the different types of energy available
    plt.plot(times,avSolar,'o-',markersize=5,label="Solar")
    plt.plot(times,avWind,'o-',markersize=5,label="Wind")
    plt.plot(times,avHydro,'o-',markersize=5,label="Hydroelectric")
    plt.plot(times,avGas,'o-',markersize=5,label="Gas/oil")
    plt.plot(times,avBio,'o-',markersize=5,label="Biofuel")
    plt.plot(times,avN,'o-',markersize=5,label="Neighbour")

    #Add labels
    #plt.xlabel("Time")
    plt.ylabel("Available Energy")
    plt.title("Available Energy per Day")

    plt.legend(loc="best",shadow=True, fontsize="small")
    plt.grid()

    print(maxY)
    for i in range(int(maxY)):
        if(i%1000 == 0):
            tickY.append(i)


    plt.yticks(avWind + avNuclear + avN + avHydro + avGas + avBio)
    plt.show()

makePlot()