gold = 100
wood = 100
worker = 5
warrior =  5
challengeDifficulty = 1
loopholder = 5
print("You have "+str(gold)+" gold, "+str(wood)+" wood, "+str(worker)+" worker(s), and "+str(warrior)+" warrior(s).")
while (loopholder > 0):
    playerOption = input("Enter choice, R to check resources, G to gather, T to train: ")
    playerOption = str(playerOption)
    if playerOption == "G":
        gPlayerOption = input("Enter choice, G to mine for gold, W to mine for wood: ")
        if gPlayerOption == "G":
            workersAssigned = input("How many workers do you wish to assign to mine gold?")
            if int(workersAssigned) <= worker:
                gold = int(gold) + int(workersAssigned)*10
                gold = str(gold)
                resourceGathered = int(workersAssigned)*10
                print("You assigned "+str(workersAssigned)+" workers to mine gold and gathered "+str(resourceGathered)+" gold. Totalling "+gold+ " gold.")
            else:
                print("You don't have enough workers!")
                loopholder = 5
        elif gPlayerOption == "W":
            workersAssigned = input("How many workers do you wish to assign to mine wood?")
            if int(workersAssigned) <= worker:
                wood = int(wood) + int(workersAssigned)*10
                wood = str(wood)
                resourceGathered = int(workersAssigned)*10
                print(workersAssigned)
                print("You assigned "+str(workersAssigned)+" workers to mine wood and gathered "+str(resourceGathered)+" wood. Totalling "+wood+ " wood.")
            else:
                print("You don't have enough workers!")
                loopholder = 5
    elif playerOption == "R":
        print("You have "+str(gold)+" gold, "+str(wood)+" wood, "+str(worker)+" worker(s), and "+str(warrior)+" warrior(s).")
    elif playerOption == "T":
        playerOption = input("Enter choice, WORK to train workers, WAR to train warriors: ")
        playerOption = str(playerOption)
         if str(workersAssigned) == WORK:
            gPlayerOption = input("How many workers do you wish to train? Each worker cost 50 gold:  ")
            gPlayerOption = int(gPlayerOption)
            if gPlayerOption <= gold/10:
                worker = worker+gPlayerOption
            
