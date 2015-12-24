Ext.define('Softmachine.view.main.MenuTree', {
    extend : 'Ext.tree.Panel',
    alias : 'widget.menuTree',

    requires : [
        'Softmachine.view.main.MenuOption'
    ],

    viewConfig : {
        plugins : {
            // El dragText no puede reemplazarse por una variable, impide el drag
            ptype : 'treeviewdragdrop',
            dragText : 'Drag to reorder',
            ddGroup : 'menu'
        }
    },

    rootVisible : false,
    lines : true,
    minWidth : 200,

    initComponent : function(){

        Ext.define('Proto.MenuModel', {
            extend : 'Ext.data.Model',
            proxy : {
                type : 'ajax',
                url : _SM._PConfig.urlMenu,
                extraParams : {
                    forceDefault : 0
                },
                actionMethods : {
                    read : 'POST'
                }
            },

            fields : [
                {
                    name : 'id',
                    type : 'string'
                },
                {
                    name : 'viewCode',
                    type : 'string'
                },
                {
                    name : 'text',
                    type : 'string'
                },
                {
                    name : 'leaf',
                    type : 'boolean'
                }
            ]

        });

        this.store = Ext.create('Ext.data.TreeStore', {
            autoLoad : true,
            model : 'Proto.MenuModel',
            rootProperty : {
                text : 'menu',
                expanded : true
            },
            listeners : {
                'datachanged' : function(store, eOpts){
                    this.treeRecord = undefined;
                }

            }

        });

        if (_SM._UserInfo.isStaff || true) {

            Ext.apply(this, {
                dockedItems : [
                    {
                        xtype : 'toolbar',
                        dock : 'bottom',
                        items : [
                            {
                                id : 'newFolder',
                                scope : this,
                                handler : this.newFolder,
                                iconCls : 'menu_new_folder',
                                tooltip : _SM.__language.Tooltip_New_Folder
                            },
                            {
                                // Solo para los admins
                                id : 'newOption',
                                hidden : true,
                                scope : this,
                                handler : this.newOption,
                                iconCls : 'menu_new_option',
                                tooltip : _SM.__language.Tooltip_New_Option
                            },
                            {
                                id : 'editNode',
                                scope : this,
                                handler : this.editNode,
                                iconCls : 'icon-nodeEdit',
                                tooltip : _SM.__language.Tooltip_Edit_Node
                            },
                            {
                                id : 'deleteNode',
                                scope : this,
                                handler : this.deleteNode,
                                iconCls : 'icon-nodeDelete',
                                tooltip : _SM.__language.Tooltip_Del_Node
                            },
                            '->',
                            {
                                id : 'saveMenu',
                                scope : this,
                                handler : this.saveMenu,
                                iconCls : 'menu_save',
                                tooltip : _SM.__language.Tooltip_Save_Menu
                            },
                            {
                                id : 'reloadMenu',
                                scope : this,
                                handler : this.reloadMenu,
                                iconCls : 'menu_reload',
                                tooltip : _SM.__language.Tooltip_Reload_Menu
                            },
                            {
                                id : 'resetMenu',
                                scope : this,
                                handler : this.resetMenu,
                                iconCls : 'menu_reset',
                                tooltip : _SM.__language.Tooltip_Reset_Menu
                            }
                        ]
                    }
                ]
            });
        }

        this.callParent();
        // this.addEvents('menuSelect');

        if (_SM._UserInfo.isSuperUser)
            Ext.getCmp('newOption').show();

    },

    listeners : {

        // .view.View , .data.Model record, HTMLElement item, Number index, .EventObject e, Object
        // eOpts
        'itemclick' : function(view, rec, item, index, evObj, eOpts){
            this.treeRecord = rec;
        },
        'itemdblclick' : function(view, rec, item, index, evObj, eOpts){
            this.treeRecord = rec;
            if (rec.get('leaf')) {
                var viewCode = rec.data.viewCode || rec.data.id;
                this.fireEvent('menuSelect', this, viewCode);
                _SM.ViewPort.controller.loadPciFromMenu(viewCode);
            }
        }

    },

    editNode : function(btn){
        // Verifica si hay un item activo y lo edita
        if (this.treeRecord) {
            var me = this, msg = _SM.__language.Msg_Window_New_Folder;

            Ext.Msg.prompt(_SM.__language.Title_Window_New_Folder, msg, function(btn, pName){
                if ((btn != 'ok') || (!pName) || (pName.length == 0)) {
                    return;
                }
                me.treeRecord.set('text', pName);
            }, me, false, me.treeRecord.get('text'));

        }
    },

    deleteNode : function(btn){
        // Verifica si hay un item activo, confirma y lo borra
        if (this.treeRecord) {
            this.treeRecord.remove();
            this.treeRecord = undefined;
        }
    },

    newFolder : function(btn){
        // prompt por el nombre del menu y lo crea en el arbol
        var me = this, msg = _SM.__language.Msg_Window_New_Folder;

        Ext.Msg.prompt(_SM.__language.Title_Window_New_Folder, msg, function(btn, pName){
            if (btn != 'ok') {
                return;
            }

            var tNode = {
                'text' : pName,
                'children' : []
            }, record;

            if (me.treeRecord && (!me.treeRecord.get('leaf'))) {
                record = me.treeRecord;
            } else {
                record = me.store.getRootNode();
            }

            record.appendChild(tNode);
        }, me, false);

    },

    newOption : function(btn){
        // abre forma para creacion de opcion, la forma se encarga de la creacion
        if (!this.treeRecord || this.treeRecord.get('leaf')) {
            _SM.errorMessage('AddMenuOption', _SM.__language.Msg_Select_Folder);
            return;
        }
        var myWin = Ext.widget('menuOption', {
            treeRecord : this.treeRecord,
            title : _SM.__language.Title_Window_Add_Option
        });
        myWin.show();
    },

    reloadMenu : function(btn){
        // recarga el menu guardado
        this.store.getProxy().extraParams.forceDefault = 0;
        this.store.load();
    },

    resetMenu : function(btn){
        // borra el menu guardado y recarga el menu default basado en modelos
        this.store.getProxy().extraParams.forceDefault = 1;
        this.store.load();
    },
    saveMenu : function(btn){
        // guarda el menu actual
        var sMeta = Ext.encode(Tree2Menu(this.store.getRootNode()));
        _SM.saveProtoObj('__menu', sMeta);

        function Tree2Menu(tNode){
            // Para poder leer de la treeData o del TreeStore ( requiere data )
            var tData = tNode.data, tChilds = tNode.childNodes, mData = {};
            if (tData.rootProperty) {
                mData = getMenuChilds(tChilds);
            } else {
                mData = {
                    "text" : tData.text,
                    "qtip" : tData.qtip,
                    "qtitle" : tData.qtitle,
                    "iconCls" : tData.iconCls,
                    "id" : 'protoMenu-' + Ext.id(),
                    "index" : tData.index
                };
                // Es un menu
                if (tChilds.length > 0) {
                    mData.expanded = tData.expanded;
                    mData.children = getMenuChilds(tChilds);
                    mData.leaf = false;
                    mData.viewCode = tData.viewCode || tData.id;
                } else {
                    mData.expanded = false;
                    mData.children = [];
                    mData.leaf = tData.leaf;
                    mData.viewCode = tData.viewCode || tData.id;
                }
            }
            if (!mData.text || mData.text.length == 0) {
                mData.text = 'null';
            }

            return mData;

            function getMenuChilds(tChilds){
                var mChilds = [];
                for ( var ix in tChilds) {
                    var lNode = tChilds[ix];
                    var nChildData = Tree2Menu(lNode);
                    mChilds.push(nChildData);
                }
                return mChilds;
            }

        }

    }

});
