/* 
 * Definicion de las propiedades, 
 * 
 * las propiedades tienen 
 * 
 *      help         : description 
 *      type    
 *      choices      : lista de valores en caso de ser string 
 *      required     : 
 * 
 *  EL nombre de la propiedad contiene el prpDefault q solo se aplcia 
 *  si no existe y es requerida  
 * 
 */

// La defincion de tipos es   xxx.type = [ 'boolean' | 'date' | 'string' | 'number' ] 


function getSimpleProperties(oData, ptType) {
    // Retorna los valores simples, verificando los tipos de cada propiedad

    // Solo deben llegar objetos, si llega un array no hay props q mostrar
    if (_SM.typeOf(oData) == 'array') {
        return [];
    }

    // Inicializa con el type
    var cData = {}, cValue;
    
    if (ptType) {
        cData.__ptType = ptType;
    }

    for (var lKey in oData ) {
        cValue = oData[lKey];

        // Los objetos o arrays son la imagen del arbol y no deben ser tenidos en cuenta, generarian recursividad infinita
        if (_SM.typeOf(cValue) in _SM.objConv(['object', 'array'])) {
            continue;
        }

        // Si son valores codificados, los decodifica y los agrega
        if ( lKey in _SM.objConv(['__ptValue', '__ptList'])) {
            try {
                cData = Ext.decode(cValue);
            } catch (e) {
                // console.log( "Error de encodage", cValue )
            }

        } else {
            cValue = verifyPrpType(lKey, cValue);
            if (cValue) {
                cData[lKey] = cValue;
            }
        }
    }
    return cData;

};

function verifyPrpType(  lKey,  cValue ) {
    /* Verifica los tipos de las  propiedades
     * recibe el valor y el tipo y verifica si 
     * corresponden entre si
     * 
     * Intenta la conversion, sin no regresa nulo 
     */ 
    
    var pType = _SM._MetaProperties[ lKey + '.type' ]; 
    if ( ! pType )  { 
        if ( typeof ( cValue ) == 'string') { return cValue.replace(/~+$/, '');  }
        else { return cValue; }      
    }
    
    if ( pType == typeof( cValue ) ) 
    { return cValue;  }    
    
    switch ( pType ) {
    case "boolean":
        if  ( (typeof( cValue ) == 'number') ){ cValue = cValue.toString(); }
        if  ( (typeof( cValue ) == 'string') ){
            if ( cValue.substr(0,1).toLowerCase()  in _SM.objConv([ 'y', 's', '1','o', 't' ]) )
            { return true; } else { return false; } 
        } else { return false; }  
    case "number":
        return parseFloat( cValue );
    case "null":
        return null; 
    default:
        return cValue;
    }
}
