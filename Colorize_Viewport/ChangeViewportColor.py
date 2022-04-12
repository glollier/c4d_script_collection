# Randomly change viewport color of all objects
# By Guillaume Lollier
# http://instagram.com/guillaumelollier
# Updated: 12.04.2022

import c4d, random
from c4d import gui

def GenerateRandomColor():
    randX = random.random()
    randY = random.random()
    randZ = random.random()
    return c4d.Vector(randX, randY, randZ)

def ResetColor():
    return c4d.Vector()

def ChangeColor(obj):
    #print(obj)
    if(obj[c4d.ID_MG_TRANSFORM_COLOR]):
        obj[c4d.ID_MG_TRANSFORM_COLOR] = GenerateRandomColor()
    else:
        obj[c4d.ID_BASEOBJECT_USECOLOR] = 2
        obj[c4d.ID_BASEOBJECT_COLOR] = GenerateRandomColor()

def ResetColor(obj):
    if(obj[c4d.ID_MG_TRANSFORM_COLOR]):
        obj[c4d.ID_MG_TRANSFORM_COLOR] = c4d.Vector(.6,.6,.6)
    else:
        obj[c4d.ID_BASEOBJECT_USECOLOR] = 0

def IterateHierarchy(obj,ColorChoice):
    while(obj):
        if(ColorChoice):
            ChangeColor(obj)
        else:
            ResetColor(obj)
        if(obj.GetDown() != None):
            IterateHierarchy(obj.GetDown(),ColorChoice)
        obj = obj.GetNext()

def message(id, data):
    doc = c4d.documents.GetActiveDocument()
    if id == c4d.MSG_DESCRIPTION_COMMAND:
        id2 = data['id'][0].id
        if id2 == c4d.ID_USERDATA:
            userDataId = data['id'][1].id
            if userDataId == 2:
                obj = doc.GetFirstObject()
                IterateHierarchy(obj,1)
                c4d.EventAdd()
            if userDataId == 3:
                obj = doc.GetFirstObject()
                IterateHierarchy(obj,0)
                c4d.EventAdd()

def main():
    pass

# Execute main()
if __name__=='__main__':
    main()