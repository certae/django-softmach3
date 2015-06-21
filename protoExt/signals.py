from protoExt.models import CustomDefinition
from protoLib.models.protoContext import UserContext

def context2customdefinition(sender, ctModel, created, **kwargs):
    """
    Crea el filtro en el contexto dependiendo cuando se agregen o modifiquen criterios 
    ctModel : UserContext() # instance  
    
    TODO: delete 
    """
    
    viewCode = '_context.' + ctModel.modelCType.__name  

    protoDef = CustomDefinition.objects.get_or_create(
           code = viewCode, 
           metaDefinition = [], 
           smOwningUser = ctModel.user 
           )

    # Elimina el filtro si existe      
    for i in range(len(protoDef.metaDefinition)-1, -1, -1): 
        item = protoDef.metaDefinition[ i ]    
        if item.get('property', '') ==  ctModel.propName:
            protoDef.metaDefinition.pop(i)

    protoDef.metaDefinition.append( {
           'property': ctModel.propName,
           'filterStmt': ctModel.propValue, 
           } )

    protoDef.active = True 
    protoDef.overWrite = False 

    protoDef.save()  
    
