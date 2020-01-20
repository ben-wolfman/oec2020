import HourParser as parser
import FileReader as reader
import estimator as estim
import solver as solv

filename = "inputFile3.csv" #change this

starters = reader.getStarters()


reader.setFileName(filename)
currHour = reader.getNextHour()
currPow = float(starters[2][4])
season = parser.getSeason(parser.getTemperatures(currHour))
while currHour != [-1]:
    powscalar = estim.getScaling(currHour, currPow)
    print("Currpow was ", currPow)
    print("Currpow scaling ", powscalar)
    currPow *= powscalar
    print("Trend is: ", estim.estimateTrend(currHour))
    print("Currpow is ", currPow)
    powDiff = currPow + parser.getAvailableSolar(currHour) + parser.getAvailableWind(currHour) + parser.getAvailableHydro(currHour) + parser.getAvailableBio(currHour) + parser.getAvailableGas(currHour) - parser.getTotalDemand(currHour)
    print("Power difference: ", powDiff)
    print("Demand is: ", parser.getTotalDemand(currHour))
    print("solar: ", parser.getAvailableSolar(currHour))
    print("hydro: ", parser.getAvailableHydro(currHour))
    print("wind: ", parser.getAvailableWind(currHour))
    print("other: ", parser.getAvailableBio(currHour) + parser.getAvailableGas(currHour))
    print("Hour is: ", parser.getTime(currHour))
    #priority order: hydro, nuke, wind, solar, bio, neighbour, gas

    arr = solv.energyOptimization(nuclear = currPow, solar = parser.getAvailableSolar(currHour), wind = parser.getAvailableWind(currHour), hydroelectric = parser.getAvailableHydro(currHour), gas = parser.getAvailableGas(currHour), biofuel = parser.getAvailableBio(currHour), neighbour = parser.getAvailableNeighbour(currHour), dem = parser.getTotalDemand(currHour))

    reader.writeOutput(arr = arr, time = parser.getTime(currHour), diff = 0, demand = parser.getTotalDemand(currHour))

    currHour = reader.getNextHour()    



#while currHour != [-1]:
    











