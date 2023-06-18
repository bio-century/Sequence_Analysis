def AnalyseSeq(myText, myNumberOfSOIs, mySequence, mySOIPositions, myColorsTextBox,
               myDefaultColorTextBox, myColorWarningTextBox, myBackgroundColor, tab1, myColumnCount, myInput):
    from tkinter import Text, END
    import tkinter as tk
    import json
    import ModulesOwn.A_Groundwork as Groundwork
    with open("./ModulesOwn/B_SimpleTabbedGUI_Data/02_Sequence.json", "r") as openfile:
        dictSequence = json.load(openfile)
    for ii in range(len(dictSequence["SOIs"]) + 1):
        if ii == 0:
            dictSequence["mySequence"] = myInput[ii].get()
        else:
            currentKey = "mySOI""{:02d}".format(ii)
            dictSequence["SOIs"][currentKey]["Seq"] = myInput[ii].get()
    myCount              = [0] * len(dictSequence["SOIs"])
    for ii in range(myNumberOfSOIs):
        currentKey = "mySOI""{:02d}".format(ii+1)
        currentValue = dictSequence["SOIs"][currentKey]["Seq"]
        myCount[ii], mySOIPositions[ii] = Groundwork.SOIPositions(dictSequence["mySequence"], currentValue, "countchain")
    myText.delete
    myTextnew= Text(tab1, height = 2, width = 35, background = myBackgroundColor, highlightthickness = 0,
                    borderwidth = 0, font = ('Courier New', 12, 'bold'))
    myTextnew = Groundwork.ColorTheSeqMergeGUI(myTextnew, dictSequence["mySequence"], mySOIPositions, myColorsTextBox,
                                               myDefaultColorTextBox, myColorWarningTextBox, myBackgroundColor, tab1,
                                               myColumnCount)
    myTextnew.grid(row = myColumnCount, column = 3, rowspan = 1, columnspan = 5, sticky = tk.W + tk.E)


def ClearInputFields(dictSequence, myInput):
    from tkinter import BOTH, END, LEFT
    for ii in range(len(dictSequence["SOIs"]) + 1):
        myInput[ii].delete(0,END)


def ClearText(dictSequence):
    import json
    dictSequence = {
        "SOIs": {
                "mySOI01": {
                "Seq": "",
                "myColor": "green"
                },
                "mySOI02": {
                "Seq": "",
                "myColor": "blue"
                },
                "mySOI03": {
                "Seq": "",
                "myColor": "yellow"
                }
        },
        "mySequence": ""
    }
    with open("./ModulesOwn/B_SimpleTabbedGUI_Data/02_Sequence.json", "w") as outfile:
        json.dump(dictSequence, outfile, indent = 4, sort_keys = True)
    outfile.close()


def ClearTextandFields(dictSequence, myInput):
    ClearText(dictSequence)
    ClearInputFields(dictSequence, myInput)

def ColorTheSeqMergeGUI(myText, mySequence, mySOIPositions, myColorsTextBox, myDefaultColorTextBox, myColorWarningTextBox):
	from tkinter import Text, INSERT, END, DISABLED
	import tkinter as tk
	import numpy as np
	mySequence = mySequence.upper()
	if type(mySequence) is np.ndarray:
		mySequence = ''.join(str(i) for i in mySequence)
	mySOIPositionsTotal = [0] * len(mySequence)
	for jj in range(0, len(mySOIPositions)):
		mySOIPositionsTotal = mySOIPositionsTotal + mySOIPositions[jj]
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


def LoadDataset(myInput):
    import time
    import json
    from tkinter import Text, INSERT, END, DISABLED
    RestoreExampleDataset()
    time.sleep(0.1)
    with open("./ModulesOwn/B_SimpleTabbedGUI_Data/02_Sequence.json", "r") as openfile:
        dictSequence = json.load(openfile)


    for ii in range(len(dictSequence["SOIs"]) + 1):
        if ii == 0:
            currentKey = "mySequence"
            currentValue = dictSequence["mySequence"]
            myInput[ii].delete(0, END)
            myInput[ii].insert(0, currentValue)
        else:
            currentKey = "mySOI""{:02d}".format(ii)
            currentValue = dictSequence["SOIs"][currentKey]["Seq"]
            myInput[ii].delete(0, END)
            myInput[ii].insert(0, currentValue)


def RestoreExampleDataset():
    import shutil
    shutil.copy("./ModulesOwn/B_SimpleTabbedGUI_Data/02_ExampleDataset.json", "./ModulesOwn/B_SimpleTabbedGUI_Data/02_Sequence.json")


def SaveSequence(dictSequence, myInput):
    import json
    from tkinter import Text, INSERT, END, DISABLED
    for ii in range(len(dictSequence["SOIs"]) + 1):
        if ii == 0:
            dictSequence["mySequence"] = myInput[ii].get()
        else:
            currentKey = "mySOI""{:02d}".format(ii)
            dictSequence["SOIs"][currentKey]["Seq"] = myInput[ii].get()

    with open("./ModulesOwn/B_SimpleTabbedGUI_Data/02_Sequence.json", "w") as outfile:
        json.dump(dictSequence, outfile, indent = 4, sort_keys = True)
    outfile.close()