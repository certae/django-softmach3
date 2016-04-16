/*
 * Lectura del arbol de campos ( todos los lockup )
 *
 */

Ext.define('ProtoUL.proto.view.ProtoFieldTree', {
    extend :  'Ext.tree.Panel',
    alias:    'widget.protoFieldTree',

    requires: [
        'ProtoUL.proto.model.FieldSelectorModel', 
    ],

 // @viewCode   Required
    viewCode : null,

//  @myMeta   Required
    myMeta : null,

    initComponent: function() {

        me = this;
        // me.addEvents('checkModif', 'loadComplete');


        this.treeStore = Ext.create('Ext.data.TreeStore', {
            autoLoad: false,
            folderSort: false,
            sorters: [{ property: 'text', direction: 'ASC' }],

            model: 'ProtoUL.proto.model.FieldSelectorModel',

            root: {
                text: _SM.__language.Protofield_Fields,
                expanded: true
            },

            listeners: {
                beforeload : function(store, operation, eOpts){
                    store.getProxy().extraParams = {
                        viewCode : me.viewCode,
                        protoEntityId : me.myMeta.protoEntityId
                    }; 
                },

                load: function ( treeStore, records,  successful,  eOpts ) {
                    me.fireEvent('loadComplete', treeStore, records,  successful,  eOpts );
                }
            }, 

        });


        var tree = Ext.apply(this, {
            store: this.treeStore,
            useArrows: true,
            rootVisible: false ,
            minWidth: 400,

            columns: [{
                xtype: 'treecolumn', //this is so we know which column will show the tree
                text: _SM.__language.Protofield_Text,
                flex: 2,
                sortable: true,
                minWidth: 200,
                dataIndex: 'text'
            },{
                xtype: 'booleancolumn',
                trueText: 'req',
                falseText: '',
                width: 50,
                text: _SM.__language.Protofield_Req,
                dataIndex: 'required'
            },{
                xtype: 'booleancolumn',
                trueText: 'rOnly',
                width: 50,
                falseText: '',
                text: _SM.__language.Protofield_ROnly,
                dataIndex: 'readOnly'
            },{
                text: _SM.__language.Protofield_Field_Type,
                dataIndex: 'type'
            },{
                text: _SM.__language.Protofield_Zoom_Model,
                dataIndex: 'zoomModel'
            },{
                text: _SM.__language.Protofield_fk_Field,
                dataIndex: 'fkField'
            },{
                text: _SM.__language.Protofield_fk_Id,
                dataIndex: 'fkId'
            },{
                flex: 2,
                text: _SM.__language.Protofield_Ix,
                dataIndex: 'id'

            },{
                flex: 2,
                text: 'cpFromZoom',
                dataIndex: 'cpFromZoom'
            },{
                flex: 2,
                text: 'cpFromField',
                dataIndex: 'cpFromField'

            },{
                hidden : true,
                text: _SM.__language.Protofield_Header,
                dataIndex: 'header'
            },{
                hidden : true,
                text: _SM.__language.Protofield_Tooltip,
                dataIndex: 'tooltip'
            },{
                hidden : true,
                text: _SM.__language.Protofield_Default_Value,
                dataIndex: 'prpDefault'
            },{
                hidden : true,
                text: _SM.__language.Protofield_vType,
                dataIndex: 'vType'
            },{
                hidden : true,
                text: _SM.__language.Protofield_choices,
                dataIndex: 'choices'
            }]

        })

        tree.on({
            'checkchange': {fn: function (  node,  checked,  eOpts ) {
                me.fireEvent('checkModif', node,  checked,  eOpts );
            }}, scope: me }
        );


        me.callParent(arguments);
        // tree.store.load();


    },


    addUdpField:  function( vFld ) {

        // No lo encontro, lo agrega 
        var sname = vFld.name; 

        tNode = {
            'id'         : vFld.name,
            'text'       : sname,
            'type'       : 'string',
            'checked'    : vFld.checked,
            'required'   : false,
            'leaf'       : true
        }

        this.getRootNode().appendChild( tNode )

    }


    // getCheckedList: function () {
        // var records = this.getView().getChecked(),
            // names = [];
        // Ext.Array.each(records, function(rec){
            // names.push(rec.get('id'));
        // });
        // return names
    // }


});