/*jslint nomen: true, sloppy : true, white : true, sub : true */
/*global Ext */
/*global _SM */

Ext.define('ProtoUL.view.Viewport', {
    extend : 'Ext.Viewport',
    layout : 'fit',

    _loadMetaStructure : function(){
        /*
         * Load MetaDefinition ( MetaObjects, MetaProperties ) for PCI Config
         */

        var me = this;

        Ext.Ajax.request({
            method : 'POST',
            url : _SM._PConfig.urlGetMetaStructure,
            success : function(result, request){
                var myResult = Ext.decode(result.responseText);
                _SM._MetaObjects = myResult.metaObjects;
                _SM._MetaProperties = myResult.metaProperties;
            },
            failure : function(result, request){
                _SM._MetaObjects = {};
                _SM._MetaProperties = {};
                _SM.errorMessage('Error loading MetaDefinition', 'MetaDefinition not found');
            },
            scope : this
        });

    },

    afterRender : function(){
        this.callParent(arguments);

        _SM.__StBar.showBusy('loading ... ', 'vPort', 3000);

        // Load MetaDefinition
        this._loadMetaStructure();

        // Load PCI
        // TODO: This could be configured by user
        for ( var autoPci in _SM._AUTOLOAD_PCI) {
            this.loadPciFromMenu(_SM._AUTOLOAD_PCI[autoPci]);
        }

        _SM._mainWin = this;

    },

});
