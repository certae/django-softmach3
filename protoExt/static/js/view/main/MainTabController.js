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

});



_SM.closeTabListener = function(){

    // _SM.vp_TabContainer.on
    // Ext.destroy( Ext.ComponentQuery.query('protoZoom') )
    // Ext.destroy( Ext.ComponentQuery.query('smGrid') )

};

_SM.closeTabListener = function(){

    // _SM.vp_TabContainer.on
    // Ext.destroy( Ext.ComponentQuery.query('protoZoom') )
    // Ext.destroy( Ext.ComponentQuery.query('smGrid') )

};
