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
                    print('patientID:' + str(patientId))

                    pircheData[patientId] = {}

                    pircheData[patientId]['a1']=pircheTokens[1]
                    pircheData[patientId]['a2']=pircheTokens[2]
                    pircheData[patientId]['b1']=pircheTokens[3]
                    pircheData[patientId]['b2']=pircheTokens[4]
                    pircheData[patientId]['c1']=pircheTokens[5]
                    pircheData[patientId]['c2']=pircheTokens[6]
                    pircheData[patientId]['drb11']=pircheTokens[7]
                    pircheData[patientId]['drb12']=pircheTokens[8]
                    pircheData[patientId]['drb31']=pircheTokens[9]
                    pircheData[patientId]['drb32']=pircheTokens[10]
                    pircheData[patientId]['drb41']=pircheTokens[11]
                    pircheData[patientId]['drb42']=pircheTokens[12]
                    pircheData[patientId]['drb51']=pircheTokens[13]
                    pircheData[patientId]['drb52']=pircheTokens[14]
                    pircheData[patientId]['dqa11']=pircheTokens[15]
                    pircheData[patientId]['dqa12']=pircheTokens[16]
                    pircheData[patientId]['dqb11']=pircheTokens[17]
                    pircheData[patientId]['dqb12']=pircheTokens[18]
                    pircheData[patientId]['dpa11']=pircheTokens[19]
                    pircheData[patientId]['dpa12']=pircheTokens[20]
                    pircheData[patientId]['dpb11']=pircheTokens[21]
                    pircheData[patientId]['dpb12']=pircheTokens[22]


                    drb11Presents = pircheTokens[37]
                    pircheData[patientId]['drb11PresentsUniqueCores ']= parsePircheCoresString(pircheCoresString=drb11Presents)
                    drb12Presents = pircheTokens[38]
                    pircheData[patientId]['drb12PresentsUniqueCores'] = parsePircheCoresString(pircheCoresString=drb12Presents)

                    drb1PresentsA = pircheTokens[126]
                    pircheData[patientId]['drb1PresentsAUniqueCores'] = parsePircheCoresString(pircheCoresString=drb1PresentsA)
                    drb1PresentsB = pircheTokens[167]
                    pircheData[patientId]['drb1PresentsBUniqueCores'] = parsePircheCoresString(pircheCoresString=drb1PresentsB)
                    drb1PresentsC = pircheTokens[148]
                    pircheData[patientId]['drb1PresentsCUniqueCores'] = parsePircheCoresString(pircheCoresString=drb1PresentsC)
                    drb1PresentsDrb1 = pircheTokens[159]
                    pircheData[patientId]['drb1PresentsDrb1UniqueCores'] = parsePircheCoresString(pircheCoresString=drb1PresentsDrb1)

                    print('drb1PresentsDrb1:' + str(drb1PresentsDrb1))
                    print('pircheData[patientId][drb1PresentsDrb1UniqueCores]:' + str(pircheData[patientId]['drb1PresentsDrb1UniqueCores']))



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
    raise Exception ('Continue the script here, it is not done yet')

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



