def ClearInputFields(dictSequence, myInput):
    from tkinter import BOTH, END, LEFT
    for ii in range(len(dictSequence)):
        myInput[ii].delete(0,END)


def ClearText(dictSequence):
    SequenceFile = open("./Part01Data/02_Sequence.py", "w")
    SequenceFile.write("dictSequence = {}")
    SequenceFile.write("\n")
    SequenceFile.write("\n")
    for ii in range(len(dictSequence)):
        currentKey    = list(dictSequence.keys())[ii]
        currentValue  = list(dictSequence.values())[ii]
        SequenceFile.write("dictSequence[\"" + currentKey + "\"] \t = ")
        SequenceFile.write("\"" + "\"")
        SequenceFile.write("\n")
    SequenceFile.close()


def ClearTextandFields(dictSequence, myInput):
    ClearText(dictSequence)
    ClearInputFields(dictSequence, myInput)


def SaveSequence(dictSequence, myInput):
    SequenceFile = open("./Part01Data/02_Sequence.py", "w")
    SequenceFile.write("dictSequence = {}")
    SequenceFile.write("\n")
    SequenceFile.write("\n")
    for ii in range(len(dictSequence)):
        myCurrentKey    = list(dictSequence.keys())[ii]
        myCurrentValue  = list(dictSequence.values())[ii]
        SequenceFile.write("dictSequence[\"" + myCurrentKey + "\"] \t = ")
        SequenceFile.write("\"" + myInput[ii].get() + "\"")
        SequenceFile.write("\n")
    SequenceFile.close()



