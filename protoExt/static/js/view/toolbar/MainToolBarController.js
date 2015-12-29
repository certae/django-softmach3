/* MainToolBar Controller 
 * @DarioGomez 
 * Licence: GPL 
 */

Ext.define('Softmachine.view.toolbar.MainToolBarController', {
    extend : 'Ext.app.ViewController',
    alias : 'controller.maintoolbar',

    mainQbeLoadData : function(tbar, sFilter, sTitle, sorter){

        __MasterDetail.mdGridLoadData(sFilter, sorter);
        __MasterDetail.protoMasterGrid.filterTitle = sTitle;
        __MasterDetail.protoMasterGrid.setGridTitle(__MasterDetail.protoMasterGrid);

    }

})
