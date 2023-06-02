# Color DNA with respect to their bases
def ColorDNA(mySequence, myColors, myDefaultColor):
	import numpy as np
	if type(mySequence) is np.ndarray:
		mySequence = ''.join(str(i) for i in mySequence)
		mySequence = mySequence.upper()
	s  = ""
	for ii in range(0,len(mySequence)):
		if mySequence[ii] == "A":
			s = s + f"{myColors[0]}" + mySequence[ii] + f"{myDefaultColor}"
		elif mySequence[ii] == "C":
			s = s + f"{myColors[1]}" + mySequence[ii] + f"{myDefaultColor}"
		elif mySequence[ii] == "G":
			s = s + f"{myColors[2]}" + mySequence[ii] + f"{myDefaultColor}"
		elif mySequence[ii] == "T":
			s = s + f"{myColors[3]}" + mySequence[ii] + f"{myDefaultColor}"
	return s


# Color a sequence with respect to the SOI Positions
def ColorTheSeq(mySequence, mySOIPositions, myColor, myDefaultColor):

	import numpy as np
	s=""
	if type(mySequence) is np.ndarray:
		mySequence=''.join(str(i) for i in mySequence)
		mySequence = mySequence.upper()
	for ii in range(0,len(mySequence)):
		if mySOIPositions[ii] > 0:
			s = s + f"{myColor}"+mySequence[ii] + f"{myDefaultColor}"
		else:
			s = s + f"{myDefaultColor}" + mySequence[ii] + f"{myDefaultColor}"
	return s


# Color a sequence array with respect to multiple SOIs stored in an array. The return is the position counts as well as colored "mySequence" and "mySOIPositions" as strings
def ColorTheSeqMerge(mySequence, mySOIPositions, myColors, myDefaultColor, myColorWarning):
	import numpy as np
	mySequence = mySequence.upper()
	if type(mySequence) is np.ndarray:
		mySequence = ''.join(str(i) for i in mySequence)
	s  = ""
	s2 = ""
	mySOIPositionsTotal = [0] * len(mySequence)
	for jj in range(len(mySOIPositions)):
		mySOIPositionsTotal    = mySOIPositionsTotal + mySOIPositions[jj]
	mySOIPositionsTotalColored = ''.join(str(i) for i in mySOIPositionsTotal)
	for ii in range(len(mySequence)):
		for jj in range(len(mySOIPositions)):
			if mySOIPositionsTotal[ii] == 0:
				s  = s + f"{myDefaultColor}" + mySequence[ii] + f"{myDefaultColor}"
				s2 = s2 + f"{myDefaultColor}" + mySOIPositionsTotalColored[ii] + f"{myDefaultColor}"
				break
			elif mySOIPositionsTotal[ii] == 1 and mySOIPositions[jj][ii] == 1:
				s  = s + f"{myColors[jj]}" + mySequence[ii]+f"{myDefaultColor}"
				s2 = s2 + f"{myColors[jj]}" + mySOIPositionsTotalColored[ii]+f"{myDefaultColor}"
			elif mySOIPositionsTotal[ii] > 1:
				s  = s + f"{myColorWarning}" + mySequence[ii]+f"{myDefaultColor}"	
				s2 = s2 + f"{myColorWarning}" + mySOIPositionsTotalColored[ii]+f"{myDefaultColor}"
				break
	return s, s2, mySOIPositionsTotal


def ColorTheSeqMergeGUI(myText, mySequence, mySOIPositions, myColorsTextBox, myDefaultColorTextBox, myColorWarningTextBox, myBackgroundColor, root, myColumnCount):
	from tkinter import Text, INSERT, END, DISABLED
	import tkinter as tk
	import numpy as np
	mySequence = mySequence.upper()
	if type(mySequence) is np.ndarray:
		mySequence = ''.join(str(i) for i in mySequence)
	mySOIPositionsTotal = [0] * len(mySequence)
	for jj in range(0, len(mySOIPositions)):
		mySOIPositionsTotal = mySOIPositionsTotal + mySOIPositions[jj]
	# print("func: " + mySequence)
	# myText.config(state=ENABLED)
	# myText.delete(0, END)
	myText.insert(INSERT, mySequence)
	myText.config(state = DISABLED)
	mySOIPositionsTotalColored = ''.join(str(i) for i in mySOIPositionsTotal)
	for ii in range(0, len(mySequence)):
		if ii < len(mySequence):
			for jj in range(0, len(mySOIPositions)):
				if mySOIPositionsTotal[ii] == 0:
					myText.tag_add(str(ii), "1." + str(ii), "1." + str(ii + 1))
					myText.tag_config(str(ii), foreground = myDefaultColorTextBox)
					break

				elif mySOIPositionsTotal[ii] == 1 and mySOIPositions[jj][ii] == 1:
					myText.tag_add(str(ii), "1." + str(ii), "1." + str(ii + 1))
					myText.tag_config(str(ii), foreground = myColorsTextBox[jj])
					
				elif mySOIPositionsTotal[ii] > 1:
					myText.tag_add(str(ii), "1."+str(ii), "1." + str(ii + 1))
					myText.tag_config(str(ii), foreground = myColorWarningTextBox)
					break
	return myText


# Compute complement, reverse and reverse complement of a DNA
def ComplRev(mySequence, returnSeq):
    mySequence = mySequence.upper()
    probingBoolean                  = 0
    mySequenceComplement            = [""] * len(mySequence)
    mySequenceReverse               = [""] * len(mySequence)
    mySequenceReverseComplement     = [""] * len(mySequence)
    pairAT                          = ["A", "T"]
    pairCG                          = ["C", "G"]
    for ii in range(len(mySequence)):
        if returnSeq == "Sequence":
            pass
        elif returnSeq == "SequenceComplement":
            if mySequence[ii] == pairAT[probingBoolean]:
                mySequenceComplement[ii] = pairAT[not probingBoolean]
            elif mySequence[ii] == pairAT[not probingBoolean]:
                mySequenceComplement[ii] = pairAT[probingBoolean]
            elif mySequence[ii] == pairCG[probingBoolean]:
                mySequenceComplement[ii] = pairCG[not probingBoolean]
            elif mySequence[ii] == pairCG[not probingBoolean]:
                mySequenceComplement[ii] = pairCG[probingBoolean]
        elif returnSeq == "SequenceReverse":
            if mySequence[ii] == pairAT[probingBoolean]:
                mySequenceReverse[len(mySequence) - ii - 1] = pairAT[probingBoolean]
            elif mySequence[ii] == pairAT[not probingBoolean]:
                mySequenceReverse[len(mySequence) - ii - 1] = pairAT[not probingBoolean]
            elif mySequence[ii] == pairCG[probingBoolean]:
                mySequenceReverse[len(mySequence) - ii - 1] = pairCG[probingBoolean]
            elif mySequence[ii] == pairCG[not probingBoolean]:
                mySequenceReverse[len(mySequence) - ii - 1] = pairCG[not probingBoolean]
        elif returnSeq == "SequenceReverseComplement":
            if mySequence[ii] == pairAT[probingBoolean]:
                mySequenceReverseComplement[len(mySequence) - ii - 1] = pairAT[not probingBoolean]
            elif mySequence[ii] == pairAT[not probingBoolean]:
                mySequenceReverseComplement[len(mySequence) - ii - 1] = pairAT[probingBoolean]
            elif mySequence[ii] == pairCG[probingBoolean]:
                mySequenceReverseComplement[len(mySequence) - ii - 1] = pairCG[not probingBoolean]
            elif mySequence[ii] == pairCG[not probingBoolean]:
                mySequenceReverseComplement[len(mySequence) - ii - 1] = pairCG[probingBoolean]
    mySequenceComplementReturn        = List2String(mySequenceComplement)
    mySequenceReverseReturn           = List2String(mySequenceReverse)
    mySequenceReverseComplementReturn = List2String(mySequenceReverseComplement)
    if returnSeq == "Sequence":
        return mySequence
    elif returnSeq == "SequenceComplement":
        return mySequenceComplementReturn
    elif returnSeq == "SequenceReverse":
        return mySequenceReverseReturn
    elif returnSeq == "SequenceReverseComplement":
        return mySequenceReverseComplementReturn


def DarkTitleBar(window):
    import ctypes as ct
    window.update()
    set_window_attribute = ct.windll.dwmapi.DwmSetWindowAttribute
    get_parent = ct.windll.user32.GetParent
    hwnd = get_parent(window.winfo_id())
    value = 2
    value = ct.c_int(value)
    set_window_attribute(hwnd, 20, ct.byref(value),4)


# convert a list to a string
def List2String(myList):
	myList = ''.join(str(i) for i in myList)
	return myList


def SeqNumberGen(mySequence, distance):
	labelX = []
	labelNum = []
	for ii in range(1,len(mySequence)+1):
		if (ii % (distance * 10)) == 0:
			labelX.append("x")
		elif (ii % distance) == 0:
			labelX.append("|")
		else:
			labelX.append("-")
		labelNum.append((ii % 10))
	labelX = List2String(labelX)
	labelNum = List2String(labelNum)
	return labelNum, labelX


# find SOI positions and return each position as a digit representing, how many SOIs are "involved"
def SOIPositions(mySequence, mySOI, mode):
	
	import numpy as np
	mySOIPositions = np.array([0] * len(mySequence))
	mySOIPositionsIndices = []
	myCount = 0
	for ii in range(0, len(mySequence)-len(mySOI)+1):
		if mySequence[ii:ii + len(mySOI)] == mySOI:
			myCount = myCount + 1
			mySOIPositions[ii:ii + len(mySOI)] = mySOIPositions[ii:ii + len(mySOI)] + 1
			mySOIPositionsIndices.append(ii)
	if mode == "countchain":
		return myCount, mySOIPositions
	elif mode == "indices":
		return myCount, mySOIPositionsIndices