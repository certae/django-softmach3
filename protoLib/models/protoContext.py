

from .protomodel import ProtoModelBase 
from django.contrib.contenttypes.models import ContentType
from django.db import models

class UserContext(ProtoModelBase):
    """
    Esta tabla maneja los elementos que pueden servir como :
    - valores por default o 
    - como filtros predeterminados  
    
    Al momento de buscar la pci generar valores por defecto  
    Al momento de hacer el query buscar  generar valores de filtro 

    Los registros de esta tabla se agregaran desde la ocurrencia del registro; por ejemplo  
    en project, se selecciona un registro y se invoca la accion que genera el valor por defecto 
    
    El sistema buscara los hijos directos y generara un registro con el valor de la tabla y el campo 
    de referencia ( el fk en la tabla hijo ) marcandolo con el valor seleecionado del padre.     

    En una prox version se podria navegar a diferentes niveles para por ejemplo filtrar solo las 
    propiedades de un determinado projecto, de todas maneras esto podria hacerse manualmente mientras.
    
    Nota: no se genera nunca la tabla de base pues esto impediria la creacion de nuevos defectos 
    En todo caso esta tabla sera editable
    
    Esto debe funcionar a nivel individual,  
    """

    modelCType = models.ForeignKey(ContentType, blank=False, null=False)
    propName = models.CharField(blank=False, null=False, max_length=500)

    propValue = models.CharField(blank=False, null=False, max_length=200)
    propDescription = models.TextField(blank=True, null=True)

    isDefault = models.BooleanField(default=True) 
    isFilter = models.BooleanField(default=True) 


    def __str__(self):
        return "%s %s" % ( self.modelCType.__str__(), self.propName )   
    
    protoExt = { 
        "gridConfig" : {
            "listDisplay": ["__str__", "propDescription", "smOwningUser"]      
        }
    } 

    class Meta:
        unique_together = ('modelCType', 'propName', 'smOwningUser')
