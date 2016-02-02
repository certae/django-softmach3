/**
 * This class is the controller for the main view for the application. It is specified as the
 * "controller" of the Main view class.
 */

Ext.define('Softmachine.view.main.MainController', {
    extend : 'Ext.app.ViewController',
    alias : 'controller.main',

    requires : [
        'Softmachine.view.smform.FormController'
    ],

    onClickLogOut : function(){

        // Remove the localStorage key/value
        localStorage.removeItem('SmLoggedIn');

        Ext.Ajax.request({
            url : _SM._PConfig.urlLogOut,
            success : function(response){
                location.reload(true);
            },
            failure : function(){
                location.reload(true);
            }
        });

    },

    loadPciFromMenu : function(menuOpt){

        var viewCode = menuOpt;
        var me = this;

        var options = {
            scope : this,
            success : function(obj, result, request){

                me.openProtoOption(viewCode);

            },
            failure : function(obj, result, request){
                return;
            }

        };

        if (_SM.loadPci(viewCode, true, options)) {
            me.openProtoOption(viewCode);

        }

    },

    openProtoOption : function(viewCode){

        var me = this;
        var myMeta = _SM._cllPCI[viewCode];

        if (myMeta.pciStyle == 'form') {
            var formController = Ext.create('Softmachine.view.smform.FormController', {});
            formController.openProtoForm.call(formController, viewCode, -1, true);
        } else {
            _SM.vp_TabContainer.controller.addTabPanel(viewCode);
        }

    },

    clearCache : function(){
        this.tooltip = '';
        this.clearMainStatus();
        _SM.vp_TabContainer.controller.closeAllTabs();
        _SM._cllPCI = {};
    },

    clearMainStatus : function(text, origin){

        // console.log( 'clear:' + origin, text, this.busyCount );
        _SM.vp_StatusBar.busyCount--;
        if (_SM.vp_StatusBar.busyCount <= 0) {
            _SM.vp_StatusBar.busyCount = 0;
            _SM.vp_StatusBar.clearStatus({
                useDefaults : true
            })
        }

    },

    showError : function(text, origin){

        // console.log( 'error :' + origin , text )
        _SM.vp_StatusBar.setStatus({
            text : 'Oops! ' + text,
            iconCls : 'x-status-error',
            clear : true
        });

    },


    doChangeVersion : function(reference){

    }, 

    doCreateVersion : function(reference){

    }, 

});
