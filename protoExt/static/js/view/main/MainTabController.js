/**
 * This class is the controller for the main view for the application. It is specified as
 * the "controller" of the Main view class.
 */

Ext.define('Softmachine.view.main.MainTabController', {
    extend: 'Ext.app.ViewController',

    alias: 'controller.maintab',
    requires : [
        'Softmachine.view.workspace.TabMasterDetail'
    ],

    addTabPanel : function(viewCode, mdFilter, detailTitle){
        
        // DGT: Verificar esto 
        Ext.suspendLayouts();
         

        var myMeta = _SM._cllPCI[viewCode];
        var title = myMeta.shortTitle;
        if (mdFilter) {
            title = '*' + title;
        }

        var tab = this.add({
            title : title,
            viewCode : viewCode,
            border : false,
            tabConfig : {
                tooltip : title,
                width : 120
            },
            iconCls : myMeta.viewIcon,
            closable : true,
            layout : 'fit',
            items : [
                this.createTabMasterDetail(viewCode, mdFilter, detailTitle)
            ]
        });

        this.setActiveTab(tab);

        Ext.resumeLayouts(true);

    },

    createTabMasterDetail : function(viewCode, mdFilter, detailTitle){

        var MDPanel = Ext.create('widget.tabMasterDetail', {
            viewCode : viewCode,
            mdFilter : mdFilter,
            detailTitle : detailTitle
        });
        return MDPanel;
    },

    closeProtoTab : function(viewCode){

        for (var ix = this.items.items.length; ix--;) {
            var xTab = this.items.items[ix];
            if (xTab.viewCode == viewCode) {
                this.remove(xTab, true);
            }
        }

    },

    closeAllTabs : function(){
        for (var ix = this.items.items.length; ix--;) {
            var xTab = this.items.items[ix];
            this.remove(xTab, true);
        }

        Ext.destroy(Ext.ComponentQuery.query('protoZoom'));
        Ext.destroy(Ext.ComponentQuery.query('protoForm'));
        Ext.destroy(Ext.ComponentQuery.query('protoGrid'));
        Ext.destroy(Ext.ComponentQuery.query('tabMasterDetail'));

        Ext.destroy(Ext.ComponentQuery.query('protoLogin'));
        Ext.destroy(Ext.ComponentQuery.query('searchTB'));

    }

});



_SM.closeTabListener = function(){

    var x = 'TODO:  liberar la memoria';
    // _SM.__TabContainer.on
    // Ext.destroy( Ext.ComponentQuery.query('protoZoom') )
    // Ext.destroy( Ext.ComponentQuery.query('protoGrid') )

};

_SM.closeTabListener = function(){

    var x = 'TODO:  liberar la memoria';
    // _SM.__TabContainer.on
    // Ext.destroy( Ext.ComponentQuery.query('protoZoom') )
    // Ext.destroy( Ext.ComponentQuery.query('protoGrid') )

};
