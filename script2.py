inputFile = open("input.txt", "r")
formula = inputFile.read().splitlines()


rawStartMolecules = formula[0].split(" + ") #['H2 O1']
rawEndMolecules = formula[1].split(" + ")   #['H2', 'O2']


moleculeDictList = []
startListAmount = -2
endListAmount = -1
def processRawMolecules(rawMolecules, position):
    for rawMolecule in rawMolecules:
        atoms = rawMolecule.split()
        if position == "start":
            # Following makes a dict for every molecule.
            startListAmount =+ 2
            moleculeDictList.append(str(startListAmount) + "dict")
            currentDict = moleculeDictList[len(moleculeDictList) - 1]
            for atom in atoms:
                character = list(atom)
                dictToAdd = {}
                try:
                    name = character[0]
                    index = int(character[1])
                except:
                    try:
                        name = character[0] + character[1]
                        index = int(character[2])
                    except:
                        name = character[0] + character[1] + character[2]
                        index = int(character[3])
                dictToAdd[name] = index
                print("dictToAdd: {0}".format(dictToAdd))
                currentDict = dictToAdd
                print("currentDict: {0}\n".format(currentDict))

processRawMolecules(rawStartMolecules, "start")
print("Is niet hetzelfde als: {0}".format(moleculeDictList[0]))



"""
        if position == "end":
            # Following makes a dict for every molecule.
            endListAmount =+ 2
            moleculeDictList.append(endListAmount + "dict")
            moleculeDictList[len(moleculeDictList) - 1] = {}
            
            This end of code still needs to be finished, at the moment, I just want to finish the code for startMolecules and then copy-past it here with some changes.
"""