import csv
import Constants as c

filename = 'inputFile1.csv'

currentHour = 3 #first hour

def setFileName(name):
    global filename
    filename = name

def getStarters():
    global filename
    totalData = list((csv.reader(open(filename, mode='r', encoding='utf-8-sig'))))
    endData = []
    endData.append(totalData[0])
    endData.append(totalData[1])
    endData.append(totalData[2])
    return endData
     


def getNextHour():
    global currentHour
    totalData = list((csv.reader(open(filename))))
    if currentHour < len(totalData) - 1:
        nextHour = totalData[currentHour]
        currentHour += 1
        return nextHour
    else:
        return [-1]

def writeOutput(arr, time, diff, demand):
    global filename
    with open("Trillium - Output" + filename[9] + ".csv" ,  mode='a') as csvfile:
        output = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
        green = arr[1] + arr[2] + arr[3]
        
        #output array order = [nuclear, solar, wind, hydroelectric, gas, biofuel, neighbour, total emissions, total cost]
        output.writerow([str(2) + ",", str(time)+ ",", str(arr[1])+ ",", str(arr[0])+ ",", str(arr[2])+ ",", str(arr[3])+ ",", str(arr[4])+ ",", str(arr[5])+ ",", str(arr[6])+ ",", str(diff)+ ",", str(green)+ ",", str(arr[6])+ ",", "0,", str(arr[7])+ ",", str(0.08)+ ",", str(arr[8]/demand)+ ",", str(0.08 - arr[8]/demand)+ ",", "-1"])

#test values

setFileName('inputFile1.csv')

"""print(getStarters())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())
print(getNextHour())"""







                

