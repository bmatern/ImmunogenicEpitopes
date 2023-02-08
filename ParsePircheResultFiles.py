import argparse
from os import makedirs, listdir
from os.path import isfile,join, isdir

def parsePircheCoresString(pircheCoresString=None):
    uniqueCores = set()
    for peptideToken in  pircheCoresString.split(' | '):
        core = str(peptideToken.split(' ')[0]).strip()
        if(len(core)>1):
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

                    dqa11Originated = pircheTokens[71]
                    pircheData[patientId]['dqa11Originated'] = parsePircheCoresString(pircheCoresString=dqa11Originated)
                    dqa12Originated = pircheTokens[72]
                    pircheData[patientId]['dqa12Originated'] = parsePircheCoresString(pircheCoresString=dqa12Originated)




                    dpb11Originated = pircheTokens[77]
                    pircheData[patientId]['dpb11Originated'] = parsePircheCoresString(pircheCoresString=dpb11Originated)
                    dpb12Originated = pircheTokens[78]
                    pircheData[patientId]['dpb12Originated'] = parsePircheCoresString(pircheCoresString=dpb12Originated)

                    dpa11Originated = pircheTokens[75]
                    pircheData[patientId]['dpa11Originated'] = parsePircheCoresString(pircheCoresString=dpa11Originated)
                    dpa12Originated = pircheTokens[76]
                    pircheData[patientId]['dpa12Originated'] = parsePircheCoresString(pircheCoresString=dpa12Originated)



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

                    drb1PresentsDqa1 = pircheTokens[203]
                    pircheData[patientId]['drb1PresentsDqa1UniqueCores'] = parsePircheCoresString(pircheCoresString=drb1PresentsDqa1)


                    drb1PresentsDpb1 = pircheTokens[236]
                    pircheData[patientId]['drb1PresentsDpb1UniqueCores'] = parsePircheCoresString(pircheCoresString=drb1PresentsDpb1)

                    drb1PresentsDpa1 = pircheTokens[225]
                    pircheData[patientId]['drb1PresentsDpa1UniqueCores'] = parsePircheCoresString(pircheCoresString=drb1PresentsDpa1)

                    #print('drb1PresentsDrb1:' + str(drb1PresentsDrb1))
                    #print('pircheData[patientId][drb1PresentsDrb1UniqueCores]:' + str(pircheData[patientId]['drb1PresentsDrb1UniqueCores']))
                    pass

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


def combinePresenterAndEpitopes(originatedEpitopes=None, presenterEpitopes=None, recipientPresenter=None, donorOriginatedAllele=None):
    presentedCores = sorted(list(originatedEpitopes.intersection(presenterEpitopes)))
    if(len(presentedCores)==0):
        return set()
    else:
        combinedPresenterWithEpitopes = set([recipientPresenter + "~" + pep + '(' + donorOriginatedAllele + ')' for pep in presentedCores])
        return combinedPresenterWithEpitopes


def calculateFullEpitopes(recipientData=None, donorData=None):
    presentedPeptides={}
    recipientDrb11 = recipientData['drb11']
    recipientDrb12 = recipientData['drb12']
    if(recipientDrb12.strip()==''):
        recipientDrb12=recipientDrb11

    # DRB1~A
    presentedPeptides['drb11_presents_a1'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['a1Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['a1'])
    presentedPeptides['drb12_presents_a1'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['a1Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['a1'])
    presentedPeptides['drb11_presents_a2'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['a2Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['a2'])
    presentedPeptides['drb12_presents_a2'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['a2Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['a2'])

    # DRB1~B
    presentedPeptides['drb11_presents_b1'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['b1Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['b1'])
    presentedPeptides['drb12_presents_b1'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['b1Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['b1'])
    presentedPeptides['drb11_presents_b2'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['b2Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['b2'])
    presentedPeptides['drb12_presents_b2'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['b2Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['b2'])

    # DRB1~C
    presentedPeptides['drb11_presents_c1'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['c1Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['c1'])
    presentedPeptides['drb12_presents_c1'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['c1Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['c1'])
    presentedPeptides['drb11_presents_c2'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['c2Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['c2'])
    presentedPeptides['drb12_presents_c2'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['c2Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['c2'])

    # DRB1~DRB1
    presentedPeptides['drb11_presents_drb11'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['drb11Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['drb11'])
    presentedPeptides['drb12_presents_drb11'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['drb11Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['drb11'])
    presentedPeptides['drb11_presents_drb12'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['drb12Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['drb12'])
    presentedPeptides['drb12_presents_drb12'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['drb12Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['drb12'])

    # DRB1~DQB1
    presentedPeptides['drb11_presents_dqb11'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dqb11Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['dqb11'])
    presentedPeptides['drb12_presents_dqb11'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dqb11Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['dqb11'])
    presentedPeptides['drb11_presents_dqb12'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dqb12Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['dqb12'])
    presentedPeptides['drb12_presents_dqb12'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dqb12Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['dqb12'])

    # DRB1~DQA1
    presentedPeptides['drb11_presents_dqa11'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dqa11Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['dqa11'])
    presentedPeptides['drb12_presents_dqa11'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dqa11Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['dqa11'])
    presentedPeptides['drb11_presents_dqa12'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dqa12Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['dqa12'])
    presentedPeptides['drb12_presents_dqa12'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dqa12Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['dqa12'])

    # DRB1~DPB1
    presentedPeptides['drb11_presents_dpb11'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dpb11Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['dpb11'])
    presentedPeptides['drb12_presents_dpb11'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dpb11Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['dpb11'])
    presentedPeptides['drb11_presents_dpb12'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dpb12Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['dpb12'])
    presentedPeptides['drb12_presents_dpb12'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dpb12Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['dpb12'])

    # DRB1~DPA1
    presentedPeptides['drb11_presents_dpa11'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dpa11Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['dpa11'])
    presentedPeptides['drb12_presents_dpa11'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dpa11Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['dpa11'])
    presentedPeptides['drb11_presents_dpa12'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dpa12Originated']
        , presenterEpitopes=donorData['drb11PresentsUniqueCores'], recipientPresenter=recipientDrb11, donorOriginatedAllele=donorData['dpa12'])
    presentedPeptides['drb12_presents_dpa12'] = combinePresenterAndEpitopes(originatedEpitopes=donorData['dpa12Originated']
        , presenterEpitopes=donorData['drb12PresentsUniqueCores'], recipientPresenter=recipientDrb12, donorOriginatedAllele=donorData['dpa12'])


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
            pass
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
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_dqa11'].union(epitopes['drb12_presents_dqa11']))))) + "\""
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_dqa12'].union(epitopes['drb12_presents_dqa12']))))) + "\""
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_dpb11'].union(epitopes['drb12_presents_dpb11']))))) + "\""
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_dpb12'].union(epitopes['drb12_presents_dpb12']))))) + "\""
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_dpa11'].union(epitopes['drb12_presents_dpa11']))))) + "\""
        ,"\"" + str('\n'.join(sorted(list(epitopes['drb11_presents_dpa12'].union(epitopes['drb12_presents_dpa12']))))) + "\""
    ])
    return outputLine


def writePIRCHEEpitopeSummary(outputDirectory=None, epitopes=None, combinedPircheData=None, delimiter=',', newline='\n'):
    print('Writing Epitope File:' + str(outputDirectory))

    outputFileName = join(outputDirectory,'TcellEpitopes.csv')

    # TODO: I should somehow find a way to highlight the positive alleles
    #  or just list it as a column in here somewhere.
    with open(outputFileName,'w') as outputFile:
        headerLine = delimiter.join(['Transplantation_ID','R_A1','R_A2','R_B1','R_B2','R_C1','R_C2','R_DRB1_1','R_DRB1_2','R_DQB1_1','R_DQB1_2'
            ,'D_A1','D_A2','D_B1','D_B2','D_C1','D_C2','D_DRB1_1','D_DRB1_2','D_DQB1_1','D_DQB1_2'
            ,'PIRCHE_A1_Score','PIRCHE_A2_Score','PIRCHE_B1_Score','PIRCHE_B2_Score','PIRCHE_C1_Score','PIRCHE_C2_Score'
            ,'PIRCHE_DRB11_Score','PIRCHE_DRB12_Score','PIRCHE_DQB11_Score','PIRCHE_DQB12_Score'
            ,'PIRCHE_A1','PIRCHE_A2','PIRCHE_B1','PIRCHE_B2','PIRCHE_C1','PIRCHE_C2','PIRCHE_DRB11','PIRCHE_DRB12','PIRCHE_DQB11','PIRCHE_DQB12'
            ,'PIRCHE_DQA11','PIRCHE_DQA12','PIRCHE_DPB11','PIRCHE_DPB12','PIRCHE_DPA11','PIRCHE_DPA12'])
        outputFile.write(headerLine + newline)
        for transplantationID in epitopes.keys():
            currentEpitopes= epitopes[transplantationID]

            try:
                outputFile.write(str(transplantationID) + '_All' + delimiter
                    + constructOutputLine(epitopes=currentEpitopes['all']
                        , recipTyping=combinedPircheData['Recipient_' + str(transplantationID)]
                        , donorTyping=combinedPircheData['Donor_' + str(transplantationID) + '_All'])
                    + newline)
                outputFile.write(str(transplantationID) + '_Positive' + delimiter
                    + constructOutputLine(epitopes=currentEpitopes['positive']
                        , recipTyping=combinedPircheData['Recipient_' + str(transplantationID)]
                        , donorTyping=combinedPircheData['Donor_' + str(transplantationID) + '_Positive'])
                    + newline)
                outputFile.write(str(transplantationID) + '_Negative' + delimiter
                    + constructOutputLine(epitopes=currentEpitopes['negative']
                        , recipTyping=combinedPircheData['Recipient_' + str(transplantationID)]
                        , donorTyping=combinedPircheData['Donor_' + str(transplantationID) + '_Negative'])
                    + newline)
            except Exception as e:
                print('Trouble writing output file for transplant ID ' + str(transplantationID) + ':' + str(e))


def countEpitopes(epitopes=None):
    epitopeCountsAll = {}
    epitopeCountsPositive = {}
    epitopeCountsNegative = {}
    for transplantationId in epitopes.keys():
        try:
            allPeptides = epitopes[transplantationId]['all']
            positivePeptides = epitopes[transplantationId]['positive']
            negativePeptides = epitopes[transplantationId]['negative']
            for presenterPeptidePair in allPeptides.keys():
                for epitope in list(allPeptides[presenterPeptidePair]):
                    epitopeMinusOriginAllele = epitope.split('(')[0]
                    if epitopeMinusOriginAllele not in epitopeCountsAll.keys():
                        epitopeCountsAll[epitopeMinusOriginAllele] = 0
                    epitopeCountsAll[epitopeMinusOriginAllele] += 1
                for epitope in list(positivePeptides[presenterPeptidePair]):
                    epitopeMinusOriginAllele = epitope.split('(')[0]
                    if epitopeMinusOriginAllele not in epitopeCountsPositive.keys():
                        epitopeCountsPositive[epitopeMinusOriginAllele] = 0
                    epitopeCountsPositive[epitopeMinusOriginAllele] += 1
                for epitope in list(negativePeptides[presenterPeptidePair]):
                    epitopeMinusOriginAllele = epitope.split('(')[0]
                    if epitopeMinusOriginAllele not in epitopeCountsNegative.keys():
                        epitopeCountsNegative[epitopeMinusOriginAllele] = 0
                    epitopeCountsNegative[epitopeMinusOriginAllele] += 1
        except KeyError as e:
            print('could not count epitopes for transplantation id ' + str(transplantationId) + ':' + str(e))

    return epitopeCountsAll, epitopeCountsPositive, epitopeCountsNegative


def collectAndStratefyEpitopes(outputDirectory=None, epitopes=None, combinedPircheData=None, delimiter=',', newline='\n'):
    print('Writing some summary data:' + str(outputDirectory))

    # THis is counting how many times epitopes appear.
    # The counts are against the "positive" alleles in a sample
    # They're also against the "negative" alleles in sample.
    epitopeCountFileName = join(outputDirectory, 'epitopeCounts.csv')

    epitopeCountsAll, epitopeCountsPositive, epitopeCountsNegative = countEpitopes(epitopes=epitopes)

    with open(epitopeCountFileName, 'w') as epitopeCountFile:
        headerLine = delimiter.join(['Epitope','CountTotal','CountPositiveAlleles','PositiveProportion','CountNegativeAlleles','NegativeProportion'])
        epitopeCountFile.write(headerLine + newline)
        allEpitopes = sorted(list(set(epitopeCountsAll.keys())))

        for epitope in allEpitopes:
            epitopeCountAll = epitopeCountsAll[epitope]
            try:
                epitopeCountPositive = epitopeCountsPositive[epitope]
            except Exception as e:
                epitopeCountPositive = 0
            try:
                epitopeCountNegative = epitopeCountsNegative[epitope]
            except Exception as e:
                epitopeCountNegative = 0

            positiveProportion = 1.0 * epitopeCountPositive / epitopeCountAll
            negativeProportion = 1.0 * epitopeCountNegative / epitopeCountAll

            dataline = delimiter.join([str(epitope), str(epitopeCountAll), str(epitopeCountPositive), str(positiveProportion), str(epitopeCountNegative), str(negativeProportion)])
            epitopeCountFile.write(dataline + newline)


def countEpitopesPerAllele(donorGenotype=None, recipientGenotype=None, donorPeptides=None):
    currentEpitopesPerAllele = []

    for alleleIndex in donorGenotype.keys():
        if (len(str(donorGenotype[alleleIndex]))>1
            and alleleIndex in ['a1','a2','c1','c2','drb11','drb12','dqb11','dqb12']):

            currentAllele = str(donorGenotype[alleleIndex])

            # exclude recipient alleles. No antibodies in this case.
            alleleExistsInRecipient=False
            for recipAlleleIndex in recipientGenotype.keys():
                if str(recipientGenotype[recipAlleleIndex]) == currentAllele:
                    alleleExistsInRecipient=True

            if not alleleExistsInRecipient:
                epitopes = donorPeptides['drb11_presents_' + str(alleleIndex)].union(donorPeptides['drb12_presents_' + str(alleleIndex)])
                currentEpitopesPerAllele.append((currentAllele,str(len(list(epitopes)))))

    return currentEpitopesPerAllele



def countAllEpitopesPerAllele(outputDirectory=None, epitopes=None, combinedPircheData=None, delimiter=',', newline='\n'):
    # Count up how many epitopes exist per allele, split by "positive" and "negative" alleles.

    epitopesPerAlleleAll = []
    epitopesPerAllelePositive = []
    epitopesPerAlleleNegative = []
    for transplantationId in epitopes.keys():
        try:
            epitopesPerAlleleAll.extend(countEpitopesPerAllele(donorGenotype=combinedPircheData['Donor_' + str(transplantationId) + '_All'], recipientGenotype=combinedPircheData['Recipient_' + str(transplantationId)], donorPeptides=epitopes[transplantationId]['all']))
            epitopesPerAllelePositive.extend(countEpitopesPerAllele(donorGenotype=combinedPircheData['Donor_' + str(transplantationId) + '_Positive'], recipientGenotype=combinedPircheData['Recipient_' + str(transplantationId)], donorPeptides=epitopes[transplantationId]['positive']))
            epitopesPerAlleleNegative.extend(countEpitopesPerAllele(donorGenotype=combinedPircheData['Donor_' + str(transplantationId) + '_Negative'], recipientGenotype=combinedPircheData['Recipient_' + str(transplantationId)], donorPeptides=epitopes[transplantationId]['negative']))
        except KeyError as e:
            print('could not count epitopes per allele for transplantation id ' + str(transplantationId) + ':' + str(e))

    outputFileName = join(outputDirectory,'EpitopesPerAlleleAll.csv')
    with open(outputFileName, 'w') as outputFile:
        for epitopePerAlleleAll in epitopesPerAlleleAll:
            outputFile.write(str(epitopePerAlleleAll[0]) + delimiter + str(epitopePerAlleleAll[1]) + newline)

    outputFileName = join(outputDirectory,'EpitopesPerAllelePositive.csv')
    with open(outputFileName, 'w') as outputFile:
        for epitopePerAllelePositive in epitopesPerAllelePositive:
            outputFile.write(str(epitopePerAllelePositive[0]) + delimiter + str(epitopePerAllelePositive[1]) + newline)

    outputFileName = join(outputDirectory,'EpitopesPerAlleleNegative.csv')
    with open(outputFileName, 'w') as outputFile:
        for epitopePerAlleleNegative in epitopesPerAlleleNegative:
            outputFile.write(str(epitopePerAlleleNegative[0]) + delimiter + str(epitopePerAlleleNegative[1]) + newline)


def summarizeOriginatingAlleles(outputDirectory=None, epitopes=None, combinedPircheData=None, delimiter=',', newline='\n'):
    print('Summarizing originating alleles:' + str(outputDirectory))

    outputFileName = join(outputDirectory, 'OriginatingAllelesSummary.csv')

    with open(outputFileName, 'w') as outputFile:
        headerLine = delimiter.join(['Locus,AveragePircheAll,AveragePirchePositive,AveragePircheNegative'])
        outputFile.write(headerLine + newline)

        for transplantationId in epitopes.keys():
            pass

        # for each allele in all alleles
            # Add # of pirche to all alleles list

            # If it's in the positi


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

    writePIRCHEEpitopeSummary(outputDirectory=args.output, epitopes=epitopes, combinedPircheData=combinedPircheData)

    collectAndStratefyEpitopes(outputDirectory=args.output, epitopes=epitopes, combinedPircheData=combinedPircheData)

    countAllEpitopesPerAllele(outputDirectory=args.output, epitopes=epitopes, combinedPircheData=combinedPircheData)

    summarizeOriginatingAlleles(outputDirectory=args.output, epitopes=epitopes, combinedPircheData=combinedPircheData)


