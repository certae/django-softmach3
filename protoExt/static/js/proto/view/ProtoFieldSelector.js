/*
 * ProtoFieldSelector,  Primer paso para crear la pcl, seleccionar loscampos
 *
 * 1.  presentar el arbol de campos para seleccionar los fields  ( Solo en la configuracion de fields )
 * 2.  presentar los campos disponibles como una lista de campos a seleccionar, por ejemplo, en listDiplay, order by,  etc,
 *
 * Los campos UDP se agregan directamente a la lista(2).
 *
 */

Ext.define('ProtoUL.proto.view.ProtoFieldSelector', {
    extend : 'Ext.panel.Panel',
    alias : 'widget.protoFieldSelector',

    // @viewCode Required
    viewCode : null,

    // @myMeta Required
    myMeta : null,

    initComponent : function(){

        me = this;

        var tBar = Ext.create('ProtoUL.proto.ProtoToolBar', {
            dock : 'top'
        })
        tBar.setButton('add', true, true, 'add UDP')

        var elemTree = Ext.create('ProtoUL.proto.view.ProtoFieldTree', {
            viewCode : me.viewCode,
            myMeta : me.myMeta
        })

        var elemList = Ext.create('ProtoUL.ux.ProtoList', {
            checkStyle : false,
            idTitle : 'SelectedFields'
        })

        // --------------------------------------------------

        elemTree.on({
            'loadComplete' : function(treeStore, records, successful, eOpts){
                configureCurrentFields();
            },
            'checkModif' : function(node, checked, eOpts){
                var idx = node.get('id');
                elemList.addOrRemove(idx, checked);
            },
            scope : me
        });

        tBar.on({
            'preview' : function(){
                savePreview();
            },
            'save' : function(){
                savePreview();

                _SM.savePclCache(me.myMeta.viewCode, me.myMeta, true);
                _SM.savePci(me.myMeta);
            },
            'add' : function(){

                var msg = _SM.__language.Msg_Window_New_Folder;
                Ext.Msg.prompt(_SM.__language.MetaConfig_Add_Fields, msg, function(btn, pName){
                    if (btn != 'ok') {
                        return;
                    }
                    elemTree.addUdpField({
                        'name' : 'smInfo__' + pName,
                        'checked' : false
                    });

                }, me, false, '');

            },
            scope : me
        });

        // ----------------------------------------------------

        var panelItems = getSelectorsPanels(elemTree, elemList);

        Ext.apply(this, {
            layout : 'border',
            items : panelItems,
            dockedItems : [
                tBar
            ]
        });

        this.callParent(arguments);

        // TODO Add functions
        function configureCurrentFields() {

            // Crea los campos activos en la grilla
            for (var ix in me.myMeta.fields ) {
                var vFld  =  me.myMeta.fields[ix];

                elemList.addDataItem ( vFld.name, true  );

                // Lo marca o lo adiciona como UDP
                var vNode =  elemTree.treeStore.getNodeById( vFld.name );
                if ( vNode ) {
                    vNode.set( 'checked', true );
                } else {
                    vFld.checked = true;
                    elemTree.addUdpField( vFld );
                }
            }
        }

        function getDefaultField( name  ) {

            var rec =  elemTree.treeStore.getNodeById( name );
            return  {
                name : rec.get( 'id' ),

                type :  rec.get( 'type' ),
                readOnly :  rec.get( 'readOnly' ),
                required :  rec.get( 'required' ),
                tooltip :  rec.get( 'tooltip' ),
                header :  rec.get( 'header' ),

                cpFromZoom :  rec.get( 'cpFromZoom' ),
                cpFromField :  rec.get( 'cpFromField' ),

                zoomModel :  rec.get( 'zoomModel' ),
                fkField :  rec.get( 'fkField' ),
                fkId :  rec.get( 'fkId' ),
                vType :  rec.get( 'vType' ),
                prpDefault :  rec.get( 'prpDefault' ),
                choices :  rec.get( 'choices' )
            };
        }

        function savePreview() {

            var myFieldDict = _SM.getFieldDict( me.myMeta ), 
                names = elemList.getList(),
                field = {},
                fields = [];

            for (var ix in names  ) {

                field = myFieldDict[names[ix]];
                if ( ! field ) {
                    field = getDefaultField( names[ix] );
                }
                if ( field ) {
                    fields.push( _SM.clearProps( field ));
//                  console.log( "Field no encontrado", names[ix]  )
                }
            }

            // Actualiza los nuevos campos
            me.myMeta.fields = fields;

        }
    }

});
