
Ext.define('Softmachine.view.main.MenuOption', {
    extend: 'Ext.window.Window',
    alias: 'widget.menuOption',

    constructor: function(config) {

        var formPanelCfg = {
            xtype: 'form',
            frame: true,
            constrain: true,
            bodyPadding: '5 5 0',
            width: 400,

            fieldDefaults: {
                msgTarget: 'side',
                labelWidth: 75
            },
            defaults: {
                anchor: '100%'
            },

            items: [{
                xtype: 'fieldset',
                title: _SM.__language.MenuTree_Title_Fieldset,
                defaultType: 'textfield',
                layout: 'anchor',
                defaults: {
                    anchor: '100%'
                },
                items: [{
                    fieldLabel: 'text',
                    afterLabelTextTpl: _SM._requiredField,
                    name: 'text',
                    allowBlank: false
                }, {
                    fieldLabel: 'option',
                    afterLabelTextTpl: _SM._requiredField,
                    name: 'viewCode',
                    allowBlank: false,

                    __ptType: "formField",
                    editable: true,
                    xtype: "protoZoom",
                    zoomModel: "protoExt.ViewDefinition"
                }]
            }, {
                xtype: 'fieldset',
                defaultType: 'textfield',
                layout: 'anchor',
                defaults: {
                    anchor: '100%'
                },
                items: [{
                    fieldLabel: 'iconCls',
                    name: 'iconCls'
                }, {
                    fieldLabel: 'qtip',
                    name: 'qtip'
                }, {
                    fieldLabel: 'qtitle',
                    name: 'qtitle'
                }]
            }],

            buttons: [{
                text: _SM.__language.Text_Cancel_Button,
                scope: this,
                handler: this.onCancel
            }, {
                text: _SM.__language.Text_Save_Button,
                scope: this,
                handler: this.onSave
            }]
        };

        this.callParent([Ext.apply({
            titleTextAdd: _SM.__language.MenuTree_Text_Add_Event,
            titleTextEdit: _SM.__language.MenuTree_Text_Edit_Event,
            width: 600,
            autocreate: true,
            border: true,
            closeAction: 'hide',
            modal: false,
            resizable: false,
            buttonAlign: 'left',
            savingMessage: _SM.__language.Msg_Saved,
            deletingMessage: _SM.__language.Msg_Deleted_Event,
            layout: 'fit',
            items: formPanelCfg
        }, config)]);
    },

    initComponent: function() {
        this.callParent();
        this.formPanel = this.items.items[0];
    },

    onCancel: function() {
        this.close();
    },

    onSave: function() {
        if (!this.formPanel.form.isValid()) {
            return;
        }
        var tNode = this.formPanel.getForm().getValues();
        tNode.leaf = true;
        this.treeRecord.appendChild(tNode);
        this.close();
    }

});