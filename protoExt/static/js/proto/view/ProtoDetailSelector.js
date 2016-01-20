/*
 * ProtoDetailSelector,  Selecciona los detalles posibles
 *
 * 1.  presentar el arbol de campos para seleccionar los detalles
 *
 */

/*jslint nomen: true, sloppy : true, white : true, sub : true */
/*global Ext */
/*global _SM */

Ext.define('ProtoUL.proto.view.ProtoDetailSelector', {
    extend : 'Ext.panel.Panel',
    alias : 'widget.detailsSelector',

    requires: [
        'ProtoUL.ux.ProtoList', 
        'ProtoUL.proto.ProtoToolBar', 
        'ProtoUL.proto.view.ProtoDetailTree'
    ],

    // Contenedor para probar el arbol de detalles

    // @viewCode Required
    viewCode : null,

    // @myMeta Required
    myMeta : null,

    initComponent : function(){

        var me = this;
        var tBar = Ext.create('ProtoUL.proto.ProtoToolBar', {
            dock : 'top'
        })

        var elemTree = Ext.create('ProtoUL.proto.view.ProtoDetailTree', {
            viewCode : me.viewCode,
            myMeta : me.myMeta
        })

        var elemList = Ext.create('ProtoUL.ux.ProtoList', {
            checkStyle : false,
            idTitle : 'SelectedDetails'
        })

        // ----------------------------------------------------------------------------

        elemTree.on({
            'loadComplete' : function(treeStore, records, successful, eOpts){
                configureCurrentDetails()
            },
            'checkModif' : function(node, checked, eOpts){
                var idx = node.get('id')
                elemList.addOrRemove(idx, checked)
            },
            scope : me
        });

        tBar.on({
            'preview' : function(){
                savePreview()
            },
            'save' : function(){
                savePreview();
                _SM.savePclCache(me.myMeta.viewCode, me.myMeta, true)
                _SM.savePci(me.myMeta)
            },
            scope : me
        });

        // ----------------------------------------------------------------------------

        var panelItems = getSelectorsPanels(elemTree, elemList)

        Ext.apply(this, {
            layout : 'border',
            items : panelItems,
            dockedItems : [
                tBar
            ]
        });

        this.callParent(arguments);

        function configureCurrentDetails(){

            // Crea los campos activos en la grilla
            for ( var ix in me.myMeta.detailsConfig) {
                var vFld = me.myMeta.detailsConfig[ix];
                elemList.addDataItem(vFld.menuText, true)
            }
        }

        function savePreview(){

            var names = elemList.getList(), detail = {}, details = []

            for ( var ix in names) {

                detail = getExistingDetail(names[ix])
                if (!detail) {
                    detail = getDefaultDetail(names[ix])
                }
                if (detail) {
                    details.push(detail)
                } else {
                    /* console.log( "Detalle no encontrado", names[ix] ) */
                }

            }

            // Actualiza los nuevos detalles
            me.myMeta.detailsConfig = details

            function getExistingDetail(name){
                for ( var ix in me.myMeta.detailsConfig) {
                    var vFld = me.myMeta.detailsConfig[ix];
                    if (vFld.menuText == name) {
                        return vFld
                        break;
                    }
                }
            }

            function getDefaultDetail(name){

                var rec = elemTree.treeStore.getNodeById(name);
                return {
                    menuText : rec.get('id'),
                    conceptDetail : rec.get('conceptDetail'),
                    masterField : "pk",
                    detailField : rec.get('detailField')
                // detailTitleLbl : rec.get( 'detailTitleLbl' ),
                // detailTitlePattern : rec.get( 'detailTitlePattern' )
                }
            }
        }
    }

});
