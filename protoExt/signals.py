# from protoExt.models import CustomDefinition
# 
# def context2customdefinition(sender, instance, created, **kwargs):
#     """
#     Crea el filtro en el contexto dependiendo cuando se agregen o modifiquen criterios 
#     instance : ContextUser() #   
#     
#     """
# 
#     isRaw = kwargs.get('raw', False)          
#     if isRaw : return 
#     
#     viewCode = '_context.%s.%s' % ( instance.modelCType.app_label, instance.modelCType.name )    
# 
#     protoDef = CustomDefinition.smObjects.get_or_create(
#            code = viewCode, 
#            smOwningUser = instance.smOwningUser, 
#            defaults = { 'metaDefinition' : [] }
#            )[0]
# 
#     # Elimina el filtro si existe      
#     for i in range(len(protoDef.metaDefinition)-1, -1, -1): 
#         item = protoDef.metaDefinition[ i ]    
#         if item.get('property', '') ==  instance.propName:
#             protoDef.metaDefinition.pop(i)
# 
#     protoDef.metaDefinition.append( {
#            'property': instance.propName,
#            'propValue': instance.propValue, 
#            'propDescription': instance.propDescription,
#            # 'isFilter': instance.isFilter, 
#            # 'isDefault': instance.isDefault, 
#            } )
# 
#     protoDef.active = True 
#     protoDef.overWrite = False 
# 
#     protoDef.save()  
#     


