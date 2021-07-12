import numpy as np
import random
import time

def DoorAndPrizeSim(switch, loopNum) :
    win = 0
    total = 0
    
    for loop in range(loopNum) :
        strLoop = str(loop).rjust(6, " ") + " B "
        strOne = "  [0]  "
        strTwo = "  [1]  "
        strThree = "  [2]  "
        strTitle = strLoop + strOne + strTwo + strThree
        print(strTitle)
        prize = random.randint(0, 2)
        strPrize = "       P " + strOne + strTwo + strThree
        strPrize = strPrize.replace("[" + str(prize) + "]", "[&]")
        print(strPrize)
        time.sleep(1)

        initialChoice = random.randint(0,2)
        strChoice = "       C " + strOne + strTwo + strThree
        strChoice = strChoice.replace(" [" + str(initialChoice) + "] ", "([" + str(initialChoice) + "])")
        strChoice = strChoice.replace("[" + str(prize) + "]", "[&]")
        print(strChoice)
        time.sleep(1)

        doors = [0, 1, 2]
        doors.remove(prize)

        if (initialChoice in doors) :
            doors.remove(initialChoice)

        n = len(doors)
        r = random.randint(0, n - 1)

        openDoor = doors[r]
        strOpened = "       O " + strOne + strTwo + strThree
        strOpened = strOpened.replace(" [" + str(initialChoice) + "] ", "([" + str(initialChoice) + "])")
        strOpened = strOpened.replace("[" + str(prize) + "]", "[&]")
        strOpened = strOpened.replace("[" + str(openDoor) + "]", "[] ")
        print(strOpened)
        time.sleep(1)

        if (switch) :
            secondChoice = 3 - openDoor - initialChoice
            strOpened = "       S " + strOne + strTwo + strThree
            strOpened = strOpened.replace(" [" + str(secondChoice) + "] ", "([" + str(secondChoice) + "])")
            strOpened = strOpened.replace("[" + str(prize) + "]", "[&]")
            strOpened = strOpened.replace("[" + str(openDoor) + "]", "[] ")
            print(strOpened)
            time.sleep(1)
        else :
            secondChoice = initialChoice
            strOpened = "       H " + strOne + strTwo + strThree
            strOpened = strOpened.replace(" [" + str(secondChoice) + "] ", "([" + str(secondChoice) + "])")
            strOpened = strOpened.replace("[" + str(prize) + "]", "[&]")
            strOpened = strOpened.replace("[" + str(openDoor) + "]", "[] ")
            print(strOpened)
            time.sleep(1)


        total += 1
        if (secondChoice == prize) :
            print("       Win!! " + str(win) + "/" + str(total) + "=" + str(win / total))
            win += 1
        else :
            print("       Lose!" + str(win) + "/" + str(total) + "=" + str(win / total))

        print(" ")

    return (win / total)


print("Switch: ", DoorAndPrizeSim(True, 100000))
print("  Hold: ", DoorAndPrizeSim(False, 100000))