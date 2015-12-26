Ext.define('Softmachine.view.main.MainTabContainer', {
    extend : 'Ext.tab.Panel',
    alias : 'widget.mainTabContainer',

    requires : [
        'Softmachine.view.main.MainTabController',
        'Softmachine.view.toolbar.MainToolBar'
    ],
    controller : 'maintab',
    border : false,

    title : 'WorkSpace',
    tabBarHeaderPosition : 2,

    
    // DGT : Es posible, pero por ahora va igual en la grilla 
    dockedItems : [
        {
            xtype : 'mainToolBar',
            dock : 'top',

        }
    ],

    initComponent : function(){

        /*
         * @loCale __TabContainer : Referencia al objeto padre de la interface
         */
        _SM.vp_TabContainer = this;
        this.callParent();
    }

});
