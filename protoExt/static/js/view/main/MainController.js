/**
 * This class is the controller for the main view for the application. It is specified as the
 * "controller" of the Main view class.
 */

Ext.define('Softmachine.view.main.MainController', {
    extend : 'Ext.app.ViewController',
    alias : 'controller.main',


    onClickLogOut : function(){
        // Remove the localStorage key/value
        localStorage.removeItem('SmLoggedIn');

        // Remove Main View
        this.getView().destroy();

        // Add the Login Window
        Ext.create({
            xtype : 'login'
        });
    }, 


    loadPciFromMenu: function(menuOpt) {

        var viewCode = menuOpt;
        var me = this;

        var options = {
            scope: this,
            success: function(obj, result, request) {

                me.openProtoOption(viewCode);

            },
            failure: function(obj, result, request) {
                return;
            }

        };

        if (_SM.loadPci(viewCode, true, options)) {
            me.openProtoOption(viewCode);

        }

    },    

    openProtoOption: function(viewCode) {

        var me = this;
        var myMeta = _SM._cllPCI[viewCode];

        if (myMeta.pciStyle == 'form') {
            var formController = Ext.create('ProtoUL.UI.FormController', {});
            formController.openProtoForm.call(formController, viewCode, -1, true);
        } else {
            me.mainTabContainer.addTabPanel(viewCode);
        }

    },
});
