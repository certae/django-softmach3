/*jslint nomen: true, sloppy : true, white : true, sub : true */
/*global Ext */
/*global _SM */

Ext.define('ProtoUL.view.Viewport', {
    extend: 'Ext.Viewport',
    layout: 'fit',

    initComponent: function() {

        Ext.apply(this, {
            layout: 'border',
            autoRender: true,
            padding: 5,
            defaults: {
                split: true
            },
            items: [this.createHeaderPanel(), this.createMenuPanel(), this.createProtoTabContainer(), this.createFooterPanel()]

        });

        this.callParent(arguments);

    },


    createMenuPanel: function() {

        if (_SM._MENU_COLLAPSED == undefined) {
            _SM._MENU_COLLAPSED = false;
        }

        this.menuPanel = {
            region: 'west',
            width: 300,
            title: _SM.__language.Title_Main_Menu,
            collapsible: true,
            collapsed: _SM._MENU_COLLAPSED,

            xtype: 'menuTree'

            // ---------------------  Do not delete
            // layout: 'accordion',
            // items: [{
            // // title: 'Menu',
            // layout: 'fit',
            // xtype: 'menuTree'
            // // xtype: 'treepanel',
            // }, {
            // title: 'Favorits',
            // hidden: true,
            // }]
        };
        // );

        // listeners: {
        // scope: this,
        // feedselect: this.onFeedSelect
        // };

        return this.menuPanel;
    },

    loadPciFromMenu: function(menuOpt) {

        var viewCode = menuOpt;
        var me = this;

        var options = {
            scope: this,
            success: function(obj, result, request) {

                me.openProtoOption(viewCode);

            },
            failure: function(obj, result, request) {
                return;
            }

        };

        if (_SM.loadPci(viewCode, true, options)) {
            me.openProtoOption(viewCode);

        }

    },

    openProtoOption: function(viewCode) {

        var me = this;
        var myMeta = _SM._cllPCI[viewCode];

        if (myMeta.pciStyle == 'form') {
            var formController = Ext.create('ProtoUL.UI.FormController', {});
            formController.openProtoForm.call(formController, viewCode, -1, true);
        } else {
            me.protoTabContainer.addTabPanel(viewCode);
        }

    },

    createProtoTabContainer: function() {
        this.protoTabContainer = Ext.create('widget.protoTabContainer', {
            region: 'center',
            border: false,
            minWidth: 300
        });
        return this.protoTabContainer;
    },

    _loadMetaStructure: function() {

        var me = this;

        Ext.Ajax.request({
            method: 'POST',
            url: _SM._PConfig.urlGetMetaStructure,
            success: function(result, request) {
                var myResult = Ext.decode(result.responseText);
                _SM._MetaObjects = myResult.metaObjects;
                _SM._MetaProperties = myResult.metaProperties;
            },
            failure: function(result, request) {
                _SM._MetaObjects = {};
                _SM._MetaProperties = {};
                _SM.errorMessage('Error loading MetaDefinition', 'MetaDefinition not found');
            },
            scope: this
        });

    },

    afterRender: function() {
        this.callParent(arguments);

        _SM.__StBar.showBusy('loading ... ', 'vPort', 3000);

        // Load MetaDefinition
        this._loadMetaStructure();

        // Load PCI
        // TODO: This could be configured by user
        for (var autoPci in _SM._AUTOLOAD_PCI) {
            this.loadPciFromMenu(_SM._AUTOLOAD_PCI[autoPci]);
        }

        _SM._mainWin = this;

    },

});
