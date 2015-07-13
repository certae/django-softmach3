// @Author : Dario Gomez /  Certae U. Laval Quebec, Qc, Canada


/*global Ext */
/*global _SM */
/*global ProtoUL */

_versionMeta = '15.0701';

function verifyMeta(oMeta, ptType, tNode) {

    //  Verifica un objeto de acuerdo a la estructura
    //  Si es un objeto asociado a un arbol tNode es el de base,

    var __ptConfig = _SM._MetaObjects[ptType];
    var listOfConf, sKey, nBranch, myObj, ix;

    if (!__ptConfig) {
        return oMeta;
    }

    // Verifica las listas
    if (__ptConfig.lists && (_SM.typeOf(__ptConfig.lists) == 'array' )) {
        for (ix in __ptConfig.lists  ) {
            sKey = __ptConfig.lists[ix];
            if ( typeof (sKey) != 'string') {
                continue;
            }

            listOfConf = _SM._MetaObjects[sKey] || {};
            oMeta[sKey] = _SM.verifyList(oMeta[sKey], listOfConf.prpDefault);

            if (tNode) {
                // agrega una nueva lista al arbol
                nBranch = {
                    'text' : sKey,
                    '__ptType' : sKey,
                    '__ptConfig' : {
                        '__ptType' : sKey
                    },
                    'children' : []
                };

                tNode.children.push(nBranch);
            }

        }
    }

    // Verifica los Objetos ( no aplica los default, pues la config puede eliminarlos )
    if (__ptConfig.objects && (_SM.typeOf(__ptConfig.objects) == 'array' )) {
        for (ix in __ptConfig.objects  ) {
            sKey = __ptConfig.objects[ix];
            if ( typeof (sKey) != 'string') {
                continue;
            }

            myObj = oMeta[sKey];
            if (_SM.typeOf(myObj) != 'object') {
                myObj = {};
            };

            if (tNode) {

                // agrega un nuevo objeto al arbol
                nBranch = getNodeBase(sKey, sKey, {
                    '__ptType' : sKey
                });
                tNode.children.push(nBranch);

                // Agrega los hijos tambein al arbol
                oMeta[sKey] = verifyMeta(myObj, sKey, nBranch);

            } else {

                oMeta[sKey] = verifyMeta(myObj, sKey);
            }

        }
    }

    // No es necesario verificar las propiedades pues se hace al momento de guardar la pcl
    // if ( __ptConfig.properties  &&  ( _SM.typeOf( __ptConfig.properties  ) == 'array' ))  {

    return oMeta;

}

function clearPhantonProps(__ptConfig, __ptType) {
    /* Borra las propieades q no hacen parte de la config de base
     */
    var objConfig = _SM._MetaObjects[__ptType] || {};

    if ( objConfig.properties) { 
        for (var ix in __ptConfig ) {
            if (!( ix in _SM.objConv(objConfig.properties.concat(['name', '__ptValue', '__ptList', '__ptType'])))) {
                // console.log( ix )
                delete __ptConfig[ix];
            }
        }
    }
    return __ptConfig;
}
