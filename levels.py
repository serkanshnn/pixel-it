##Level Add
import sys
sys.path.insert(1, 'levels')
import levelone
import leveltwo
import levelthree
import levelfour
import levelfive

levelList = []
levelList.append(levelone)
levelList.append(leveltwo)
levelList.append(levelthree)
levelList.append(levelfour)
levelList.append(levelfive)

squareList = []
squareList.append(16)
squareList.append(13)
squareList.append(16)
squareList.append(8)
squareList.append(16)

imagePathList = []
imagePathList.append("images/LevelOne.gif")
imagePathList.append("images/LevelTwo.gif")
imagePathList.append("images/LevelThree.gif")
imagePathList.append("images/LevelFour.gif")
imagePathList.append("images/LevelFive.gif")






def randCounter():
    return len(levelList)

def randomLevelImage(count):
    return imagePathList[count]
    
def randomLevelSquareCount(count):
    return squareList[count]

def randomLevelCorrection(count):
    return levelList[count].correction()