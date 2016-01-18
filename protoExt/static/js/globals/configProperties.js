/**
 * @author Giovanni Victorette
 */
// DOC ajouter dans le guide d'installation

_SM = _SM || {};

_SM._siteTitleCollapsed = true;
_SM._versionProto = 'Version 1.0.2';
_SM.loginTitle = 'SM-Identification';

_SM._HelpPath = 'static/help/index.html';
_SM._requiredField = '<span style="color:red;font-weight:bold" data-qtip="Required">*</span>';

_SM.footerExtraContent = '';
_SM._siteTitle = ''; 
_SM.showFooterExtraContent = false;


//=====  TITLE MODELS 

// _SM._siteTitle = '<div class="top-piv">' + 
//     '<div class="piv">' +
//         '<div class="logo">' +
//         '</div>' +
//         '<div class="content">' +
//             '<div class="title"> CeRTAE </div>' +
//             '<div class="subtitle">' + _SM._versionProto + '</div>' +
//         '</div>' +
//     '</div>' +
// '</div>';


// _SM._siteTitle = '<div class="top-piv">'+
//     '<div class="menu-piv">'+
//         '<div class="alignright">'+ _SM._versionProto + '</div>' +
//     '</div>'+
//     '<div class="piv">'+
//         '<div class="logo">'+
//         '</div>'+
//         '<div class="content">'+
//             '<div class="title">'+
//             '</div>'+
//             '<div class="subtitle"></div>'+
//         '</div>'+
//     '</div>'+
// '</div>';

//======  FOOTER MODELS 

// _SM.footerExtraContent = '<div class="centre">' +
// 	'<div id="pied">'+
// 	'</div>'+
// '</div>';




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

_SM.getSimpleProperties = function( oData, ptType ){
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
            cValue = _SM.verifyPrpType(lKey, cValue);
            if (cValue) {
                cData[lKey] = cValue;
            }
        }
    }
    return cData;

};


_SM.verifyPrpType = function(   lKey,  cValue ){
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


