import HourParser as parser
import Constants as c
def estimateDemand(hour):
    currDemand = parser.getTotalDemand(hour)
    lastWeekNow = parser.getLastWeek(hour)[0]
    diff = currDemand - lastWeekNow # how much higher current demand is than projected
    projectedHours = parser.getLastWeek(hour)[1:6]
    for hour in projectedHours:
        hour += diff #correct for weekly difference
    return projectedHours

def estimateTrend(hour):
    proj = estimateDemand(hour)
    return (proj[4] - proj[0]) /5 #returns the hourly change we have to make over the next 5 hours to stay with demand

def estimateSolarProduction(hour):
    return (c.SOLARAVG * parser.getSolarCoeff(hour))

def estimateWindProduction(hour):
    return (c.WINDAVG * parser.getWindCoeff(hour))

def estimateHydroProduction(hour):
    return (c.HYDROAVG * parser.getHydroCoeff(hour))

def getScaling(hour, power):
    currDemand = parser.getTotalDemand(hour)
    currGreen = parser.getAvailableSolar(hour) + parser.getAvailableWind(hour) + parser.getAvailableHydro(hour)
    trend = estimateTrend(hour)
    nextGreen = estimateSolarProduction(hour) + estimateHydroProduction(hour) + estimateWindProduction(hour)
    deltaGreen = nextGreen - currGreen
    trend -= deltaGreen #green energy will fluctuate on its own
    scalingValue = (trend / power)
    if abs(scalingValue) > 0.01: #can only scale production by +/-1%
        scalingValue = 0.01 * (abs(scalingValue) / scalingValue) #sets it to +/-1% if it is larger
    scalingValue += 1
    return scalingValue

