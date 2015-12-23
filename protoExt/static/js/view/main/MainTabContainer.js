// Contiene  los tabs para crear las pcls

Ext.define('Softmachine.view.main.MainTabContainer', {
    extend : 'Ext.tab.Panel',
    alias : 'widget.mainTabContainer',
    requires : [
        'Softmachine.view.main.MainTabController'
    ],
    controller : 'maintab',
    border : false,

    initComponent : function(){

        /*
         * @loCale __TabContainer : Referencia al objeto padre de la interface
         */
        _SM.__TabContainer = this;
        this.callParent();
    }

});
