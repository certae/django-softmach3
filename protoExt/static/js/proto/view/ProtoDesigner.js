/*
 * Author: Dario Gomez . CERTAE - ULaval
 * Copyright 2012,
 *
 License: This source is licensed under the terms of the Open Source LGPL 3.0 license.
 Commercial use is permitted to the extent that the code/component(s) do NOT become
 part of another Open Source or Commercially licensed development library or toolkit
 without explicit permission.Full text: http://www.opensource.org/licenses/lgpl-3.0.html

 */

/*jslint nomen: true, sloppy : true, white : true, sub : true */
/*global Ext, _SM  */

Ext.define('ProtoUL.proto.view.ProtoDesigner', {
    // extend: 'Ext.panel.Panel',
    extend : 'Ext.container.Container',
    alias : 'widget.protoDesigner',

    requires : [
        'ProtoUL.proto.model.PclTreeNodeModel'
    ],

    // @myMeta
    myMeta : null,

    initComponent : function(){

        var me = this;

        Ext.apply(this, {
            layout : 'border',
            defaults : {
                lauyout : 'fit'
            },
            items : this.getPanelItems()
        });

        me.callParent(arguments);

        // Opciones del llamado AJAX
        myObj = _SM.DesignerPanels;

        // Defincion de los objetos del designer
        this.doFormatLayout(myObj);

        // Definicion del arbol basado en la meta
        this.updateFormTree();

    },

    updateFormTree : function(){
        // Genera el arbol a partir de la meta
        var treeData = _SM.Meta2Tree(this.myMeta.formConfig, 'formConfig', 'formConfig');
        treeData.expanded = true;

        this.formTree.getStore().setRootNode(treeData);

    },

    onClickRedraw : function(myObj){

        var formMeta, myForm;

        this.formPreview.removeAll(true);

        formMeta = _SM.Tree2Meta(this.formTree.store.getRootNode());
        this.myMeta.formConfig = formMeta;
        this.formController.myMeta.formConfig = formMeta;

        myForm = this.formController.newProtoForm();
        myForm.setFormReadOnly(true);
        this.formPreview.add(myForm);

    },

    doFormatLayout : function(myObj){

        var me = this, ix, myForm, vNod, propsGrid;

        this.toolsPanel = me.down('#toolsPanel');
        this.toolsTabs = me.down('#toolsTabs');
        this.formTree = me.down('#formTree');
        this.formPreview = me.down('#formPreview');

        this.formController = Ext.create('Softmachine.view.smform.FormController', {
            myMeta : me.myMeta
        });

        myForm = this.formController.newProtoForm();

        // ------------- Nested functions
        function getTreeNodeByText(treeData, textKey){
            // recupera un nodo del arbol segun su texto, para los fields y los details
            for (ix in treeData) {
                vNod = treeData[ix];
                if (vNod.text == textKey) {
                    return vNod;
                }
            }
            // No deberia nunca llegar aqui
            return {};
        }

        // --------------- function body

        myForm.setFormReadOnly(true);
        this.formPreview.add(myForm);

        this.tBar = this.toolsPanel.addDocked({
            xtype : 'toolbar',
            dock : 'top',
            items : myObj.tbar
        })[0];

        this.toolsTabs.add(myObj.toolsTabs);
        this.toolsTree = this.toolsTabs.down('#toolsTree');

        // ******************* Properties

        var propsGrid = Ext.create('ProtoUL.ux.ProtoProperty', {});
        this.properties = this.toolsTabs.down('#properties');
        this.properties.add(propsGrid);
        this.properties = propsGrid;

        propsGrid.on({
            'edit' : function(editor, e, eOpts){

                if (e.value == e.originalValue) {
                    return;
                }

                var oData = me.treeRecord.data.__ptConfig, prpName = e.record.data.name;

                // **** Solo llegan objetos, los Array se manejan en otro lado
                if (_SM.typeOf(oData) == "object") {
                    oData[prpName] = e.value;
                }

                me.onClickRedraw();
            },
            scope : me
        });

        /*
         * Se podrian cargar directamente desde el json, dejando un hook en el store y asignandolo
         * antes de crear el componente.
         */

        // TODO: ??? _SM.defineProtoPclTreeModel(); por q en una funcion 

        var treeData, treeNodAux, treeNodAuxData, ptConfig, vFld;

        treeData = _SM.clone(myObj.toolsTree);

        // Agrega los campos de la pci particular
        treeNodAux = getTreeNodeByText(treeData, 'Fields');
        for (ix in this.myMeta.fields) {
            vFld = this.myMeta.fields[ix];
            ptConfig = _SM.getFormFieldDefinition(vFld);
            ptConfig['name'] = vFld.name;
            treeNodAuxData = {
                "text" : vFld.name,
                "qtip" : vFld.cellToolTip,
                "__ptType" : "formField",
                "leaf" : true,
                "__ptConfig" : ptConfig
            };
            treeNodAux.children.push(treeNodAuxData);
        }
        ;

        // FutureUse : Dont delete ( dgt )
        // "masterField" : vFld.masterField,
        // "detailField" : vFld.detailField,
        // "detailTitleLbl" : vFld.detailTitleLbl,
        // "detailTitleField" : vFld.detailTitleField,
        // "masterTitleField" : vFld.masterTitleField,

        // Agrega los detalles
        treeNodAux = getTreeNodeByText(treeData, 'Details');
        for (ix in this.myMeta.detailsConfig) {
            vFld = this.myMeta.detailsConfig[ix];
            treeNodAuxData = {
                "text" : vFld.menuText,
                "qtip" : vFld.toolTip,
                "__ptType" : "smGrid",
                "leaf" : true,
                "__ptConfig" : {
                    "menuText" : vFld.menuText,
                    "viewCode" : vFld.conceptDetail,
                    "xtype" : "smGrid",
                    "__ptType" : "smGrid"
                }
            };
            treeNodAux.children.push(treeNodAuxData);
        }

        treeNodAux = getTreeNodeByText(treeData, 'DetailsButtons');
        for (ix in this.myMeta.detailsConfig) {
            vFld = this.myMeta.detailsConfig[ix];
            treeNodAuxData = {
                "text" : vFld.menuText,
                "qtip" : vFld.toolTip,
                "__ptType" : "detailButton",
                "leaf" : true,
                "__ptConfig" : {
                    "text" : vFld.menuText,
                    "viewCode" : vFld.conceptDetail,
                    "xtype" : "detailButton",
                    "__ptType" : "detailButton"
                }
            };
            treeNodAux.children.push(treeNodAuxData);
        }

        // -----------------------------------
        // Crea el store
        var treeStore, toolsTree, formTree, formTreeView;

        treeStore = Ext.create('Ext.data.TreeStore', {
            model : 'ProtoUL.proto.model.PclTreeNodeModel',
            root : {
                expanded : true,
                children : treeData
            }
        });

        toolsTree = Ext.create('Ext.tree.Panel', {
            layout : 'fit',
            itemId : 'baseTree',
            store : treeStore,
            // autoScroll : true,
            rootVisible : false,
            viewConfig : {
                plugins : {
                    ptype : 'treeviewdragdrop',
                    enableDrop : false
                }
            }
        });

        this.toolsTree.add(toolsTree);
        this.toolsTree = toolsTree;

        // ------------------------------------------------

        treeStore = Ext.create('Ext.data.TreeStore', {
            model : 'ProtoUL.proto.model.PclTreeNodeModel',
            root : {
                expanded : true,
                text : _SM.__language.Title_Main_Panel,
                children : []
            }
        });

        formTree = Ext.create('Ext.tree.Panel', {
            layout : 'fit',
            store : treeStore,
            autoScroll : true,
            rootVisible : true,
            viewConfig : {
                plugins : {
                    ptype : 'treeviewdragdrop'
                }
            }
        });

        this.formTree.add(formTree);
        this.formTree = formTree;

        // ------------------------------------------------
        var rec, ptType, nParent, nIndex, tNode;

        formTreeView = this.formTree.getView();
        this.formTreeViewId = formTreeView.id;

        formTreeView.on({
            'beforedrop' : {
                fn : function(node, data, overModel, dropPosition, dropHandler, eOpts){

                    // Can not copy items or categories
                    if (data.view.id != this.formTreeViewId) {
                        rec = data.records[0];
                        ptType = rec.get('text');
                        if (ptType in _SM.objConv([
                            'Fields',
                            'Containers',
                            'Grids'
                        ]))
                        {
                            return false;
                        }

                        if (ptType in _SM.objConv([
                            'htmlset',
                            'fieldset'
                        ]))
                        {

                            // FIX store null : Obtiene el padre y el ix  
                            nParent = overModel.store.getById(overModel.data.parentId);
                            nIndex = overModel.data.index;

                            if (!nParent) {
                                nParent = overModel;
                            }

                            if (dropPosition == 'after') {
                                nIndex += 1;
                            }

                            dropHandler.cancelDrop();

                            // Crea un nodo
                            tNode = _SM.getNodeBase(ptType, ptType, {
                                '__ptType' : ptType
                            });
                            nParent.insertChild(nIndex, tNode);

                        }

                        // El drop genera una copia del mismo registro siempre
                        data.copy = true;
                    }

                }
            },
            'drop' : {
                fn : function(){
                    this.onClickRedraw();
                }
            },

            scope : this
        });

        this.formTree.on({
            'select' : function(rowModel, record, rowIndex, eOpts){
                // Guarda el registro actico, para actualizarlo mas tarde
                me.treeRecord = record;

                // prepara las propiedades corresponidnetes,
                // debe cpia las props por defecto de la pcl
                _SM.prepareProperties(record, me.myMeta, me.properties);
            },
            scope : me
        });

        // Para manejar los botones dinamicamente addListener

        // EL wizzard utiliza Ext.element.loader para cargar dinamicamenta la definicion a partir de
        // una URL
        // la URL ya probe q puede ser un archivo json,

        // revisar en el ejemplo como usar jsonForm y jsonPropertyGrid codepress
        var btRedraw = this.tBar.down('#redraw');
        btRedraw.on('click', function(btn, event, eOpts){
            this.onClickRedraw()
        }, me);

        var btSave = this.tBar.down('#save');
        btSave.on('click', function(btn, event, eOpts){

            var formMeta = _SM.Tree2Meta(this.formTree.store.getRootNode());
            this.myMeta.formConfig = formMeta;

            _SM.savePclCache(this.myMeta.viewCode, this.myMeta, true);
            _SM.savePci(this.myMeta);
        }, me);

        var btDel = this.tBar.down('#delete');
        btDel.on('click', function(btn, event, eOpts){
            // var ptType = me.treeRecord.data.__ptType
            me.treeRecord.remove();
        }, me);

    },

    // ==============================================================================

    getPanelItems : function(){

        // this.myForm = Ext.widget('protoform', {
        // myMeta : this.myMeta
        // });

        return [
            {
                region : 'center',
                layout : 'fit',
                itemId : 'formPreview',
                // items : this.myForm,
                // autoScroll : true,
                flex : 2,
                minSize : 200
            },
            {
                region : 'west',
                collapsible : true,
                split : true,
                flex : 1,
                title : _SM.__language.Title_Form_Panel,
                itemId : 'toolsPanel',
                layout : 'border',
                defaults : {
                    lauyout : 'fit'
                },
                items : [
                    {
                        region : 'center',
                        layout : 'fit',
                        itemId : 'formTree',
                        autoScroll : true,
                        minHeight : 150
                    },
                    {
                        region : 'south',
                        layout : 'fit',
                        itemId : 'toolsTabs',
                        collapsible : true,
                        split : true,
                        flex : 1,
                        title : _SM.__language.Title_Panel_Tools
                    }
                ]
            }
        ];

    }
});
