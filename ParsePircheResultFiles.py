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
                    pircheData[patientId]['drb11PresentsUniqueCores']= parsePircheCoresString(pircheCoresString=drb11Presents)
                    drb12Presents = pircheTokens[38]
                    pircheData[patientId]['drb12PresentsUniqueCores'] = parsePircheCoresString(pircheCoresString=drb12Presents)

                    a1Originated = pircheTokens[57]
                    pircheData[patientId]['a1Originated'] = parsePircheCoresString(pircheCoresString=a1Originated)
                    a2Originated = pircheTokens[58]
                    pircheData[patientId]['a2Originated'] = parsePircheCoresString(pircheCoresString=a2Originated)
                    b1Originated = pircheTokens[59]
                    pircheData[patientId]['b1Originated'] = parsePircheCoresString(pircheCoresString=b1Originated)
                    b2Originated = pircheTokens[60]
                    pircheData[patientId]['b2Originated'] = parsePircheCoresString(pircheCoresString=b2Originated)
                    c1Originated = pircheTokens[61]
                    pircheData[patientId]['c1Originated'] = parsePircheCoresString(pircheCoresString=c1Originated)
                    c2Originated = pircheTokens[62]
                    pircheData[patientId]['c2Originated'] = parsePircheCoresString(pircheCoresString=c2Originated)

                    drb11Originated = pircheTokens[63]
                    pircheData[patientId]['drb11Originated'] = parsePircheCoresString(pircheCoresString=drb11Originated)
                    drb12Originated = pircheTokens[64]
                    pircheData[patientId]['drb12Originated'] = parsePircheCoresString(pircheCoresString=drb12Originated)

                    dqb11Originated = pircheTokens[73]
                    pircheData[patientId]['dqb11Originated'] = parsePircheCoresString(pircheCoresString=dqb11Originated)
                    dqb12Originated = pircheTokens[74]
                    pircheData[patientId]['dqb12Originated'] = parsePircheCoresString(pircheCoresString=dqb12Originated)

                    # TODO: Add DQA1, DPB1, DPA1, DRB3,4,5

                    drb1PresentsA = pircheTokens[126]
                    pircheData[patientId]['drb1PresentsAUniqueCores'] = parsePircheCoresString(pircheCoresString=drb1PresentsA)
                    drb1PresentsB = pircheTokens[167]
                    pircheData[patientId]['drb1PresentsBUniqueCores'] = parsePircheCoresString(pircheCoresString=drb1PresentsB)
                    drb1PresentsC = pircheTokens[148]
                    pircheData[patientId]['drb1PresentsCUniqueCores'] = parsePircheCoresString(pircheCoresString=drb1PresentsC)
                    drb1PresentsDrb1 = pircheTokens[159]
                    pircheData[patientId]['drb1PresentsDrb1UniqueCores'] = parsePircheCoresString(pircheCoresString=drb1PresentsDrb1)
                    drb1PresentsDqb1 = pircheTokens[214]
                    pircheData[patientId]['drb1PresentsDqb1UniqueCores'] = parsePircheCoresString(pircheCoresString=drb1PresentsDqb1)

                    #print('drb1PresentsDrb1:' + str(drb1PresentsDrb1))
                    #print('pircheData[patientId][drb1PresentsDrb1UniqueCores]:' + str(pircheData[patientId]['drb1PresentsDrb1UniqueCores']))

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
            print('Could not read pirche file:' + str(fileName) + ':' + str(e))
            #raise(e)

    return combinedPircheData


def calculateFullEpitopes(recipientData=None, donorData=None):
    presentedPeptides={}
    recipientDrb11 = recipientData['drb11']
    recipientDrb12 = recipientData['drb12']
    if(recipientDrb12.strip()==''):
        recipientDrb12=recipientDrb11

    # TODO: probably clean this up and make a submethod
    drb11PresentsA1Cores = sorted(list(donorData['a1Originated'].intersection(donorData['drb11PresentsUniqueCores'])))
    presentedPeptides['drb11_presents_a1'] = set([recipientDrb11 + "~" + pep + '(' + donorData['a1'] + ')' for pep in drb11PresentsA1Cores])
    drb12PresentsA1Cores = sorted(list(donorData['a1Originated'].intersection(donorData['drb12PresentsUniqueCores'])))
    presentedPeptides['drb12_presents_a1'] = set([recipientDrb12 + "~" + pep + '(' + donorData['a1'] + ')' for pep in drb12PresentsA1Cores])
    drb11PresentsB1Cores = sorted(list(donorData['b1Originated'].intersection(donorData['drb11PresentsUniqueCores'])))
    presentedPeptides['drb11_presents_b1'] = set([recipientDrb11 + "~" + pep + '(' + donorData['b1'] + ')' for pep in drb11PresentsB1Cores])
    drb12PresentsB1Cores = sorted(list(donorData['b1Originated'].intersection(donorData['drb12PresentsUniqueCores'])))
    presentedPeptides['drb12_presents_b1'] = set([recipientDrb12 + "~" + pep + '(' + donorData['b1'] + ')' for pep in drb12PresentsB1Cores])
    drb11PresentsC1Cores = sorted(list(donorData['c1Originated'].intersection(donorData['drb11PresentsUniqueCores'])))
    presentedPeptides['drb11_presents_c1'] = set([recipientDrb11 + "~" + pep + '(' + donorData['c1'] + ')' for pep in drb11PresentsC1Cores])
    drb12PresentsC1Cores = sorted(list(donorData['c1Originated'].intersection(donorData['drb12PresentsUniqueCores'])))
    presentedPeptides['drb12_presents_c1'] = set([recipientDrb12 + "~" + pep + '(' + donorData['c1'] + ')' for pep in drb12PresentsC1Cores])

    drb11PresentsA2Cores = sorted(list(donorData['a2Originated'].intersection(donorData['drb11PresentsUniqueCores'])))
    presentedPeptides['drb11_presents_a2'] = set([recipientDrb11 + "~" + pep + '(' + donorData['a2'] + ')' for pep in drb11PresentsA2Cores])
    drb12PresentsA2Cores = sorted(list(donorData['a2Originated'].intersection(donorData['drb12PresentsUniqueCores'])))
    presentedPeptides['drb12_presents_a2'] = set([recipientDrb12 + "~" + pep + '(' + donorData['a2'] + ')' for pep in drb12PresentsA2Cores])
    drb11PresentsB2Cores = sorted(list(donorData['b2Originated'].intersection(donorData['drb11PresentsUniqueCores'])))
    presentedPeptides['drb11_presents_b2'] = set([recipientDrb11 + "~" + pep + '(' + donorData['b2'] + ')' for pep in drb11PresentsB2Cores])
    drb12PresentsB2Cores = sorted(list(donorData['b2Originated'].intersection(donorData['drb12PresentsUniqueCores'])))
    presentedPeptides['drb12_presents_b2'] = set([recipientDrb12 + "~" + pep + '(' + donorData['b2'] + ')' for pep in drb12PresentsB2Cores])
    drb11PresentsC2Cores = sorted(list(donorData['c2Originated'].intersection(donorData['drb11PresentsUniqueCores'])))
    presentedPeptides['drb11_presents_c2'] = set([recipientDrb11 + "~" + pep + '(' + donorData['c2'] + ')' for pep in drb11PresentsC2Cores])
    drb12PresentsC2Cores = sorted(list(donorData['c2Originated'].intersection(donorData['drb12PresentsUniqueCores'])))
    presentedPeptides['drb12_presents_c2'] = set([recipientDrb12 + "~" + pep + '(' + donorData['c2'] + ')' for pep in drb12PresentsC2Cores])


    drb11PresentsDrb11Cores = sorted(list(donorData['drb11Originated'].intersection(donorData['drb11PresentsUniqueCores'])))
    presentedPeptides['drb11_presents_drb11'] = set([recipientDrb11 + "~" + pep + '(' + donorData['drb11'] + ')' for pep in drb11PresentsDrb11Cores])
    drb12PresentsDrb11Cores = sorted(list(donorData['drb11Originated'].intersection(donorData['drb12PresentsUniqueCores'])))
    presentedPeptides['drb12_presents_drb11'] = set([recipientDrb12 + "~" + pep + '(' + donorData['drb11'] + ')' for pep in drb12PresentsDrb11Cores])

    drb11PresentsDrb12Cores = sorted(list(donorData['drb12Originated'].intersection(donorData['drb11PresentsUniqueCores'])))
    presentedPeptides['drb11_presents_drb12'] = set([recipientDrb11 + "~" + pep + '(' + donorData['drb12'] + ')' for pep in drb11PresentsDrb12Cores])
    drb12PresentsDrb12Cores = sorted(list(donorData['drb12Originated'].intersection(donorData['drb12PresentsUniqueCores'])))
    presentedPeptides['drb12_presents_drb12'] = set([recipientDrb12 + "~" + pep + '(' + donorData['drb12'] + ')' for pep in drb12PresentsDrb12Cores])

    drb11PresentsDqb11Cores = sorted(list(donorData['dqb11Originated'].intersection(donorData['drb11PresentsUniqueCores'])))
    presentedPeptides['drb11_presents_dqb11'] = set([recipientDrb11 + "~" + pep + '(' + donorData['dqb11'] + ')' for pep in drb11PresentsDqb11Cores])
    drb12PresentsDqb11Cores = sorted(list(donorData['dqb11Originated'].intersection(donorData['drb12PresentsUniqueCores'])))
    presentedPeptides['drb12_presents_dqb11'] = set([recipientDrb12 + "~" + pep + '(' + donorData['dqb11'] + ')' for pep in drb12PresentsDqb11Cores])

    drb11PresentsDqb12Cores = sorted(list(donorData['dqb12Originated'].intersection(donorData['drb11PresentsUniqueCores'])))
    presentedPeptides['drb11_presents_dqb12'] = set([recipientDrb11 + "~" + pep + '(' + donorData['dqb12'] + ')' for pep in drb11PresentsDqb12Cores])
    drb12PresentsDqb12Cores = sorted(list(donorData['dqb12Originated'].intersection(donorData['drb12PresentsUniqueCores'])))
    presentedPeptides['drb12_presents_dqb12'] = set([recipientDrb12 + "~" + pep + '(' + donorData['dqb12'] + ')' for pep in drb12PresentsDqb12Cores])


    # TODO: Add DQA1, DPB1,DPA1, DRB345
    '''
    drb11PresentsDqa1Cores = sorted(list(donorData['drb1PresentsDqa1UniqueCores'].intersection(donorData['drb11PresentsUniqueCores'])))
    presentedPeptides['drb11_presents_dqa1'] = set([recipientDrb11 + "~" + pep for pep in drb11PresentsDqa1Cores])
    drb12PresentsDqa1Cores = sorted(list(donorData['drb1PresentsDqa1UniqueCores'].intersection(donorData['drb12PresentsUniqueCores'])))
    presentedPeptides['drb12_presents_dqa1'] = set([recipientDrb12 + "~" + pep for pep in drb12PresentsDqa1Cores])
    '''
    return presentedPeptides


def pairPircheResults(combinedPircheData=None):
    print('Pairing together PIRCHE data...')

    transplantationIds = set()
    presentedPeptides = {}
    # Get unique transplantation IDs
    for sampleId in combinedPircheData.keys():
        #print('sampleId:' + str(sampleId))
        sampleIdTokens = sampleId.split('_')
        transplantationId = int(sampleIdTokens[1])
        transplantationIds.add(transplantationId)
    transplantationIds = list(transplantationIds)

    # Loop transplant ids
    for transplantationId in transplantationIds:
        try:
            presentedPeptides[transplantationId] = {}
            presentedPeptides[transplantationId]['all'] = calculateFullEpitopes(recipientData=combinedPircheData['Recipient_' + str(transplantationId)]
                , donorData= combinedPircheData['Donor_' + str(transplantationId)+ '_All'])
            presentedPeptides[transplantationId]['positive'] = calculateFullEpitopes(recipientData=combinedPircheData['Recipient_' + str(transplantationId)]
                , donorData= combinedPircheData['Donor_' + str(transplantationId)+ '_Positive'])
            presentedPeptides[transplantationId]['negative'] = calculateFullEpitopes(recipientData=combinedPircheData['Recipient_' + str(transplantationId)]
                , donorData= combinedPircheData['Donor_' + str(transplantationId)+ '_Negative'])
        except Exception as e:
            print('Failed analysing trans id because Pirche data is missing I think, look into this' + str(transplantationId) + ':' + str(e))

    return presentedPeptides


def constructOutputLine(epitopes=None, recipTyping=None, donorTyping=None, delimiter=','):
    outputLine = delimiter.join([
        recipTyping['a1']
        ,recipTyping['a2']
        ,recipTyping['b1']
        ,recipTyping['b2']
        ,recipTyping['c1']
        ,recipTyping['c2']
        ,recipTyping['drb11']
        ,recipTyping['drb12']
        ,recipTyping['dqb11']
        ,recipTyping['dqb12']
        ,donorTyping['a1']
        ,donorTyping['a2']
        ,donorTyping['b1']
        ,donorTyping['b2']
        ,donorTyping['c1']
        ,donorTyping['c2']
        ,donorTyping['drb11']
        ,donorTyping['drb12']
        ,donorTyping['dqb11']
        ,donorTyping['dqb12']
        ,str(len(list(epitopes['drb11_presents_a1'].union(epitopes['drb12_presents_a1']))))
        ,str(len(list(epitopes['drb11_presents_a2'].union(epitopes['drb12_presents_a2']))))
        ,str(len(list(epitopes['drb11_presents_b1'].union(epitopes['drb12_presents_b1']))))
        ,str(len(list(epitopes['drb11_presents_b2'].union(epitopes['drb12_presents_b2']))))
        ,str(len(list(epitopes['drb11_presents_c1'].union(epitopes['drb12_presents_c1']))))
        ,str(len(list(epitopes['drb11_presents_c2'].union(epitopes['drb12_presents_c2']))))
        ,str(len(list(epitopes['drb11_presents_drb11'].union(epitopes['drb12_presents_drb11']))))
        ,str(len(list(epitopes['drb11_presents_drb12'].union(epitopes['drb12_presents_drb12']))))
        ,str(len(list(epitopes['drb11_presents_dqb11'].union(epitopes['drb12_presents_dqb11']))))
        ,str(len(list(epitopes['drb11_presents_dqb12'].union(epitopes['drb12_presents_dqb12']))))
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_a1'].union(epitopes['drb12_presents_a1']))))) + "\""
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_a2'].union(epitopes['drb12_presents_a2']))))) + "\""
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_b1'].union(epitopes['drb12_presents_b1']))))) + "\""
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_b2'].union(epitopes['drb12_presents_b2']))))) + "\""
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_c1'].union(epitopes['drb12_presents_c1']))))) + "\""
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_c2'].union(epitopes['drb12_presents_c2']))))) + "\""
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_drb11'].union(epitopes['drb12_presents_drb11']))))) + "\""
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_drb12'].union(epitopes['drb12_presents_drb12']))))) + "\""
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_dqb11'].union(epitopes['drb12_presents_dqb11']))))) + "\""
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_dqb12'].union(epitopes['drb12_presents_dqb12']))))) + "\""
    ])
    return outputLine


def writeOutputFile(outputDirectory=None, epitopes=None, combinedPircheData=None, delimiter=',',newline='\n'):
    print('Writing Epitope File:' + str(outputDirectory))

    outputFileName = join(outputDirectory,'TcellEpitopes.csv')

    # TODO: I should somehow find a way to highlight the positive alleles
    #  or just list it as a column in here somewhere.
    with open(outputFileName,'w') as outputFile:
        headerLine = delimiter.join(['Transplantation_ID','R_A1','R_A2','R_B1','R_B2','R_C1','R_C2','R_DRB1_1','R_DRB1_2','R_DQB1_1','R_DQB1_2'
            ,'D_A1','D_A2','D_B1','D_B2','D_C1','D_C2','D_DRB1_1','D_DRB1_2','D_DQB1_1','D_DQB1_2'
            ,'PIRCHE_A1_Score','PIRCHE_A2_Score','PIRCHE_B1_Score','PIRCHE_B2_Score','PIRCHE_C1_Score','PIRCHE_C2_Score'
            ,'PIRCHE_DRB11_Score','PIRCHE_DRB12_Score','PIRCHE_DQB11_Score','PIRCHE_DQB12_Score'
            ,'PIRCHE_A1','PIRCHE_A2','PIRCHE_B1','PIRCHE_B2','PIRCHE_C1','PIRCHE_C2','PIRCHE_DRB11','PIRCHE_DRB12','PIRCHE_DQB11','PIRCHE_DQB12'])
        outputFile.write(headerLine + newline)
        for transplantationID in epitopes.keys():
            currentEpitopes= epitopes[transplantationID]

            try:
                outputFile.write(str(transplantationID) + '_Positive' + delimiter
                    + constructOutputLine(epitopes=currentEpitopes['positive']
                        , recipTyping=combinedPircheData['Recipient_' + str(transplantationID)]
                        , donorTyping=combinedPircheData['Donor_' + str(transplantationID) + '_All'])
                    + newline)
            except Exception as e:
                print('Trouble writing output file for transplant ID ' + str(transplantationID) + ':' + str(e))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("-v", "--verbose", help="verbose operation", action="store_true")
    parser.add_argument("-pd", "--pirchedirectory", help="Directory with Pirche Results CSV from pirche portal", required=True)
    parser.add_argument("-o", "--output", help="output dir", required=True)

    args = parser.parse_args()
    verbose = args.verbose

    if not isdir(args.output):
        makedirs(args.output)

    spacer = '-'*40

    combinedPircheData = readPircheDirectory(pircheDirectory=args.pirchedirectory)

    epitopes = pairPircheResults(combinedPircheData=combinedPircheData)

    writeOutputFile(outputDirectory=args.output, epitopes=epitopes, combinedPircheData=combinedPircheData)



