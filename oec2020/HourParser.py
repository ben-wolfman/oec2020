def getTime(hour):
    end = ""
    for ch in hour[1]:
        if ch == ':':
            break
        else:
            end += ch
    end = int(end)
    return end

        
def getTemperatures(hour): #gets array of temperatures for this hour
    intermediate = hour[10:15]
    end = []
    for i in intermediate:
        end.append(float(i))
    return end
def getTotalDemand(hour):
    return float(hour[2])
def getAvailableSolar(hour):
    return float(hour[3])
def getAvailableWind(hour):
    return float(hour[5])
def getAvailableHydro(hour):
    return float(hour[6])
def getAvailableGas(hour):
    return float(hour[7])
def getAvailableBio(hour):
    return float(hour[8])
def getAvailableNeighbour(hour):
    return float(hour[9])
def getSolarCoeff(hour):
    return float(hour[15])
def getWindCoeff(hour):
    return float(hour[16])
def getHydroCoeff(hour):
    return float(hour[17])
def getNeighbourNeed(hour): #max we can sell to the neighbour
    return float(hour[18])
def getSellingPrice(hour): #selling price to neighbour
    return float(hour[19])
def getLastWeek(hour): #list of last weeks demand
    intermediate = hour[20:26]
    end = []
    for i in intermediate:
        end.append(float(i))
    return end
def getSeason(temps):
    season = "W" #base value
    for temperature in temps:
        if temperature < -1.5:
            season = "W"
        elif temperature > 21.8:
            season = "S"
    return season
def getCostType(time, season):
    if season == "W":
        if time >= 7 and time <= 10:
            return 13.4
        elif time >= 11 and time <= 4:
            return 9.4
        elif time == 5 or time == 6:
            return 13.4
        else:
            return 6.5
    else:
        if time >= 7 and time <= 10:
            return 9.4
        elif time >= 11 and time <= 4:
            return 13.4
        elif time == 5 or time == 6:
            return 9.4
        else:
            return 6.5