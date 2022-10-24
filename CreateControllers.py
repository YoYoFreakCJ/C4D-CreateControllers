from typing import Optional
import c4d

doc: c4d.documents.BaseDocument  # The active document
op: Optional[c4d.BaseObject]  # The active object, None if unselected

def main() -> None:
    controllerNameSuffix = '_Controller'
    controllerNullType = 13 # 13 = Sphere
    controllerColor = c4d.Vector(1)
    
    doc.StartUndo()
    
    selectedObjects = doc.GetActiveObjects(c4d.GETACTIVEOBJECTFLAGS_CHILDREN)
    
    doc.SetActiveObject(None, c4d.SELECTION_NEW)
    
    nulls = []
    
    for obj in selectedObjects:
        globalMatrix = obj.GetMg()
        
        null = c4d.BaseObject(c4d.Onull)
        nulls.append(null)
        
        null.SetMg(globalMatrix)
        null.SetName(obj[c4d.ID_BASELIST_NAME] + controllerNameSuffix)
        null[c4d.NULLOBJECT_DISPLAY] = controllerNullType
        null[c4d.ID_BASEOBJECT_USECOLOR] = c4d.ID_BASEOBJECT_USECOLOR_ALWAYS
        null[c4d.ID_BASELIST_ICON_COLORIZE_MODE] = 2 # 2 = Display Color
        null[c4d.ID_BASEOBJECT_COLOR] = controllerColor
        null[c4d.ID_BASELIST_ICON_COLOR] = null[c4d.ID_BASEOBJECT_COLOR]
        
        doc.InsertObject(null)
        doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, null)
        doc.SetActiveObject(null, c4d.SELECTION_ADD)
        c4d.EventAdd()        
        
        tag = obj.MakeTag(c4d.Tcaconstraint)
        doc.AddUndo(c4d.UNDOTYPE_NEWOBJ, tag)
        tag[c4d.ID_CA_CONSTRAINT_TAG_PSR] = True
        tag[c4d.ID_CA_CONSTRAINT_TAG_PSR_MAINTAIN] = True        
        tag[10001] = null # 10001 = Transform Target
        
    doc.EndUndo()
    c4d.EventAdd()

if __name__ == '__main__':
    main()
