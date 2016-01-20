/*
 * Lectura del arbol de detalles
 *
 */

Ext.define('ProtoUL.proto.view.ProtoDetailTree', {
    extend : 'Ext.tree.Panel',
    alias : 'widget.detailDefTree',

    /**
     * @requires ProtoUL.proto.model.DetailsTreeModel
     */
    requires : [
        'ProtoUL.proto.model.DetailsTreeModel',
    ],

    // @viewCode Required
    viewCode : null,

    // @myMeta Required
    myMeta : null,

    initComponent : function(){

        var me = this;
        // me.addEvents('checkModif', 'loadComplete');

        definieDetailsConfigTreeModel(me.viewCode, me.myMeta.protoEntityId);

        this.treeStore = Ext.create('Ext.data.TreeStore', {
            autoLoad : true,
            model : 'ProtoUL.proto.model.DetailsTreeModel',
            root : {
                text : _SM.__language.Grid_Detail_Title,
                expanded : true
            },

            listeners : {
                load : function(treeStore, records, successful, eOpts){
                    configureCurrentDetails()
                    me.fireEvent('loadComplete', treeStore, records, successful, eOpts);
                }
            }

        });

        var tree = Ext.apply(this, {
            store : this.treeStore,
            useArrows : true,
            rootVisible : false,
            minWidth : 400,

            columns : [
                {
                    xtype : 'treecolumn', // this is so we know which column will show the tree
                    text : _SM.__language.Tree_Concept_Details_Text,
                    flex : 2,
                    sortable : true,
                    minWidth : 200,
                    dataIndex : 'id'
                },
                {
                    text : _SM.__language.Tree_Concept_Details_Detail,
                    dataIndex : 'conceptDetail'
                },
                {
                    flex : 2,
                    text : _SM.__language.Tree_Details_Field,
                    dataIndex : 'detailField'
                }
            ]

        })

        tree.on({
            'checkchange' : {
                fn : function(node, checked, eOpts){
                    me.fireEvent('checkModif', node, checked, eOpts);
                }
            },
            scope : me
        });

        me.callParent(arguments);

        function configureCurrentDetails(){

            // Recorre el store y marca los campos activos
            // me.getView().getStore().each(function(record){
            me.getRootNode().cascadeBy(
                    function(record){

                        var lRec = {
                            'conceptDetail' : record.get('conceptDetail'),
                            'detailField' : record.get('detailField')
                        }

                        // Evita iterar en el root
                        if (lRec.conceptDetail) {

                            // Marca los campos activos en la grilla
                            for ( var ix in me.myMeta.detailsConfig) {
                                var vFld = me.myMeta.detailsConfig[ix];

                                if ((vFld.conceptDetail == lRec.conceptDetail)
                                        && (vFld.detailField == lRec.detailField))
                                {
                                    record.set('checked', true)

                                    // Agrega los campos personalisados
                                    record.set('id', vFld.menuText)
                                    // record.set( 'detailTitleLbl', vFld.detailTitleLbl )
                                    // record.set( 'detailTitlePattern', vFld.detailTitlePattern )

                                    break;
                                }
                            }
                        }
                    })
        }

        function definieDetailsConfigTreeModel(viewCode, protoEntityId){
            // TODO: Modelo usado en la lista de campos con la jerarquia completa de los de zoom (
            // detalle de fk )

        }
    }

});
