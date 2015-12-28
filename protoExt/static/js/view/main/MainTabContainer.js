Ext.define('Softmachine.view.main.MainTabContainer', {
    extend : 'Ext.tab.Panel',
    alias : 'widget.mainTabContainer',

    requires : [
        'Softmachine.view.main.MainTabController',
        'Softmachine.view.toolbar.MainToolBar', 

        'Softmachine.view.smmasterdetail.MDActionsController', 
        'Softmachine.view.smmasterdetail.MDDetailsController', 
        'Softmachine.view.smmasterdetail.MDPrintOptsController', 
        'Softmachine.view.smmasterdetail.MDSetFiltersController', 
        'Softmachine.view.smmasterdetail.MDSetSortersController', 
        'Softmachine.view.smmasterdetail.MDSetTabsController', 
        'Softmachine.view.smmasterdetail.MDTbSortByController', 
        
    ],
    controller : 'maintab',
    border : false,

    title : 'WorkSpace',
    tabBarHeaderPosition : 2,

    
    initComponent : function(){

        /*
         * @loCale __TabContainer : Referencia al objeto padre de la interface
         */
        _SM.vp_TabContainer = this;
        this.callParent();
    }, 



});
