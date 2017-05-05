import csv

dataFolder='./data'
def createIndividualFiles():
    folder=dataFolder+'/ind'
    mainFile=dataFolder+'/eventFrequency.csv'
    curID=''
    curFile=None
    monitor= open(dataFolder+'/summary.csv','w')
    #read csv and create individual file
    count=0
    with open(mainFile,'r') as csvFile:
        handler=csv.reader(csvFile,delimiter=',')
        for row in handler:
            id=row[1]
            if(id!=curID):
                if(curFile != None):
                    curFile.close()
                    monitor.write(curID+','+str(count)+'\n')
                    count=0
                curFile= open(dataFolder+'/'+id+'.csv','w')
                curID=id

            curFile.write(','.join(row)+'\n')
            count+=1
    curFile.close()
    monitor.write(curID+','+str(count)+'\n')
    csvFile.close()
    monitor.close()




createIndividualFiles()
