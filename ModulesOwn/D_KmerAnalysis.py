def FindPalindroms(dictSeqGroup, klength):
    from Bio.Seq import Seq
    count = 1
    # walk along the target sequence
    for ii in range(len(dictSeqGroup["targetSeq"]["mySequence"]) - klength):
        mySOIProbeIndices = []
        mySOIProbeRCIndices = []
        mySOI = dictSeqGroup["targetSeq"]["mySequence"][ii:ii + klength]
        seq = Seq(mySOI)
        mySOIRevCompl = str(seq.reverse_complement_rna())
        palindrom = False
        for jj in range(ii, len(dictSeqGroup["targetSeq"]["mySequence"]) - klength):
            mySOIProbe = dictSeqGroup["targetSeq"]["mySequence"][jj:jj + klength]
            if mySOIProbe == mySOI:
                mySOIProbeIndices.append(jj)
            elif mySOIProbe == mySOIRevCompl:
                mySOIProbeRCIndices.append(jj)
                palindrom = True
        if palindrom == True:
            dictSeqGroup["palindrom"+"{:02d}".format(count)] = {}
            dictSeqGroup["palindrom"+"{:02d}".format(count)]["mySOI"] = mySOI
            dictSeqGroup["palindrom"+"{:02d}".format(count)]["mySOIRC"] = mySOIRevCompl
            dictSeqGroup["palindrom"+"{:02d}".format(count)]["mySOIIndices"] = mySOIProbeIndices
            dictSeqGroup["palindrom"+"{:02d}".format(count)]["mySOIRCIndices"] = mySOIProbeRCIndices
            dictSeqGroup["palindrom"+"{:02d}".format(count)]["myColor"] = "Green"
            count += 1
    return dictSeqGroup


def PrintPalindroms(dictSeqGroup, klength, myColors, myDefaultColor):
    stemp=""
    s=""
    stringlist=[]
    for kk in range(len(dictSeqGroup) - 1):
        joindedList=[]
        joindedListColor=[]
        joindedList = dictSeqGroup["palindrom"+"{:02d}".format(kk+1)]["mySOIIndices"] + dictSeqGroup["palindrom"+"{:02d}".format(kk+1)]["mySOIRCIndices"]
        joindedListColor = [0]*len(dictSeqGroup["palindrom"+"{:02d}".format(kk+1)]["mySOIIndices"])+[1]*len(dictSeqGroup["palindrom"+"{:02d}".format(kk+1)]["mySOIRCIndices"])
        for kfor in range(len(joindedList)):
            if kfor == 0 and joindedList[kfor] == 0:
                s = f"{myColors[joindedListColor[kfor]]}" + dictSeqGroup["targetSeq"]["mySequence"][0:joindedList[kfor]+klength]
            elif kfor == 0 and joindedList[kfor] != 0:
                s = f"{myDefaultColor}" + dictSeqGroup["targetSeq"]["mySequence"][0:joindedList[kfor]]+ f"{myColors[joindedListColor[kfor]]}" + dictSeqGroup["targetSeq"]["mySequence"][joindedList[kfor]:joindedList[kfor]+klength]
            elif joindedList[kfor-1]+klength>joindedList[kfor]:
                delta = -(joindedList[kfor - 1] + klength) + joindedList[kfor]
                stemp=s[:len(stemp)-3]
                s = s[:len(s)+delta] + f"{myColors[2]}" + dictSeqGroup["targetSeq"]["mySequence"][joindedList[kfor]:joindedList[kfor-1]+klength] + f"{myColors[1]}" + dictSeqGroup["targetSeq"]["mySequence"][joindedList[kfor-1]+klength:joindedList[kfor]+klength] + f"{myDefaultColor}" + dictSeqGroup["targetSeq"]["mySequence"][joindedList[kfor]+klength:len(dictSeqGroup["targetSeq"]["mySequence"])]
            elif kfor < len(joindedList)-1:
                s = s + f"{myDefaultColor}" + dictSeqGroup["targetSeq"]["mySequence"][joindedList[kfor-1]+klength:joindedList[kfor]]+ f"{myColors[joindedListColor[kfor]]}" + dictSeqGroup["targetSeq"]["mySequence"][joindedList[kfor]:joindedList[kfor]+klength]
            else:
                s = s + f"{myDefaultColor}" + dictSeqGroup["targetSeq"]["mySequence"][joindedList[kfor-1]+klength:joindedList[kfor]]+ f"{myColors[joindedListColor[kfor]]}" + dictSeqGroup["targetSeq"]["mySequence"][joindedList[kfor]:joindedList[kfor]+klength]# + f"{myDefaultColor}" + dictSeqGroup["targetSeq"]["mySequence"][joindedList[kfor]+klength:len(dictSeqGroup["targetSeq"]["mySequence"])]
                s = s + f"{myDefaultColor}" + dictSeqGroup["targetSeq"]["mySequence"][joindedList[kfor]+klength:len(dictSeqGroup["targetSeq"]["mySequence"])]
        stringlist.append(s)
        # print("Palindroms "+"{:02d}".format(kk+1) + ": \t\t" +s)
    return stringlist