
Ext.define('Softmachine.view.main.MainTabContainer', {
    extend : 'Ext.tab.Panel',
    alias : 'widget.mainTabContainer',

    requires : [
        'Softmachine.view.main.MainTabController', 
        'Softmachine.view.toolbar.MainToolBar'
    ],
    controller : 'maintab',
    border : false,

            // title : 'Tab Panel',
            tabBarHeaderPosition : 2,

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
        _SM.__TabContainer = this;
        this.callParent();
    }

});
