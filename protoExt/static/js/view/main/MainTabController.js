/**
 * This class is the controller for the main view for the application. It is specified as
 * the "controller" of the Main view class.
 */

Ext.define('Softmachine.view.main.MainTabController', {
    extend: 'Ext.app.ViewController',

    alias: 'controller.maintab',
    requires : [
        'Softmachine.view.smmasterdetail.TabMasterDetail'
    ],


    addTabPanel : function(viewCode, mdFilter, detailTitle){
        
        Ext.suspendLayouts();
         

        var myMeta = _SM._cllPCI[viewCode];
        var title = myMeta.shortTitle;
        if (mdFilter) {
            title = '*' + title;
        }

        var tab = this.view.add({
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

        this.view.setActiveTab(tab);

        Ext.resumeLayouts(true);

    },

    // setActiveTab : function(){

    //     // Load ToolbarConfig for meta
    //     this.protoEnable = (this.myMeta.gridConfig.searchFields.length > 0);

    // }


    createTabMasterDetail : function(viewCode, mdFilter, detailTitle){

        var MDPanel = Ext.create('widget.tabMasterDetail', {
            viewCode : viewCode,
            mdFilter : mdFilter,
            detailTitle : detailTitle
        });
        return MDPanel;
    },

    closeProtoTab : function(viewCode){

        for (var ix = this.view.items.items.length; ix--;) {
            var xTab = this.view.items.items[ix];
            if (xTab.viewCode == viewCode) {
                this.view.remove(xTab, true);
            }
        }

    },

    closeAllTabs : function(){

        for (var ix = this.view.items.items.length; ix--;) {
            var xTab = this.view.items.items[ix];
            this.view.remove(xTab, true);
        }

        // Ext.destroy(Ext.ComponentQuery.query('protoZoom'));
        // Ext.destroy(Ext.ComponentQuery.query('protoForm'));
        // Ext.destroy(Ext.ComponentQuery.query('smGrid'));
        // Ext.destroy(Ext.ComponentQuery.query('tabMasterDetail'));

        // Ext.destroy(Ext.ComponentQuery.query('protoLogin'));
        // Ext.destroy(Ext.ComponentQuery.query('searchTB'));

    }
    
});



_SM.closeTabListener = function(){

    // _SM.vp_TabContainer.on
    // Ext.destroy( Ext.ComponentQuery.query('protoZoom') )
    // Ext.destroy( Ext.ComponentQuery.query('smGrid') )

};

