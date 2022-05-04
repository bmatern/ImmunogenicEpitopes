import argparse
from os import makedirs, listdir
from os.path import isfile,join, isdir

def parsePircheCoresString(pircheCoresString=None):
    uniqueCores = set()
    for peptideToken in  pircheCoresString.split(' | '):
        core = peptideToken.split(' ')[0]
        uniqueCores.add(core)
    return uniqueCores

def readPircheFile(pircheResultsFile=None, delimiter=','):
    if verbose:
        print('Reading Pirche Results File:' +str(pircheResultsFile))
        print(spacer)

    pircheData = {}
    patientId=''
    with open(pircheResultsFile, "r") as input:
        for rowIndex, row in enumerate(input):

            if(rowIndex>=3):
                pircheTokens = row.strip().split(delimiter)
                patientId = pircheTokens[0]
                if len(pircheTokens) > 3 and len(str(patientId).strip())>0:
                    #print('row:' + str(row.strip()))
                    #print('patientID:' + str(patientId))

                    pircheData[patientId] = {}

                    pircheData[patientId]['a1']=pircheTokens[1]
                    pircheData[patientId]['a2']=pircheTokens[2]
                    pircheData[patientId]['b1']=pircheTokens[3]
                    pircheData[patientId]['b2']=pircheTokens[4]
                    pircheData[patientId]['c1']=pircheTokens[5]
                    pircheData[patientId]['c2']=pircheTokens[6]
                    pircheData[patientId]['drb11']=pircheTokens[7]
                    pircheData[patientId]['drb12']=pircheTokens[8]


                    drb11Presents = pircheTokens[37]
                    pircheData[patientId]['drb11PresentsUniqueCores ']= parsePircheCoresString(pircheCoresString=drb11Presents)
                    drb12Presents = pircheTokens[38]
                    pircheData[patientId]['drb12PresentsUniqueCores'] = parsePircheCoresString(pircheCoresString=drb12Presents)

                    #print('drb11Presents:' + str(drb11Presents))
                    #print('drb12Presents:' + str(drb12Presents))



            else:
                pass # Header Row
    return pircheData


def readPircheDirectory(pircheDirectory=None):
    print('Looking for files in Pirche Directory:' + str(pircheDirectory))

    fileNames = sorted([f for f in listdir(pircheDirectory) if isfile(join(pircheDirectory, f))])


    print('Filenames:' + str(fileNames))
    combinedPircheData = {}

    for fileName in fileNames:
        try:
            currentPircheResults = readPircheFile(pircheResultsFile=join(pircheDirectory, fileName))
            combinedPircheData.update(currentPircheResults)
        except Exception as e:
            print('Could not read pirche file:' + str(fileName))

    return combinedPircheData


def pairPircheResults(combinedPircheData=None):
    print('Pairing together PIRCHE data...')

    transplantationIds = set()
    # Get unique transplantation IDs
    for sampleId in combinedPircheData.keys():
        #print('sampleId:' + str(sampleId))
        sampleIdTokens = sampleId.split('_')
        transplantationId = int(sampleIdTokens[1])
        transplantationIds.add(transplantationId)
    transplantationIds = sorted(list(transplantationIds))

    # Loop transplant ids

    # Get Patient and Donor results from dictionary

    # Pair DRB1 and Epitopes

    # Write a result....


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--verbose", help="verbose operation", action="store_true")
    parser.add_argument("-pd", "--pirchedirectory", help="Directory with Pirche Results CSV from pirche portal", required=True)
    #parser.add_argument("-o", "--output", help="output dir", required=True)

    args = parser.parse_args()
    verbose = args.verbose

    #if not isdir(args.output):
    #    makedirs(args.output)

    spacer = '-'*40

    combinedPircheData = readPircheDirectory(pircheDirectory=args.pirchedirectory)

    pairPircheResults(combinedPircheData=combinedPircheData)



