Ext.define('Softmachine.view.login.LoginController', {
    extend : 'Ext.app.ViewController',
    alias : 'controller.login',

    requires: [
        'Softmachine.view.login.PwdLost', 
        'Softmachine.view.login.PwdReset'
    ],

    onKeyEnter: function(me, e) {
        if ((e.getKey() == e.ENTER) &&  this.lookupReference('form').isValid()   ) {
            this.submitLogin(this.lookupReference('submit'));
        }
    },

    submitLogin : function(btn){

        btn.disable();
        var view = this.getView(), user = {}, me = this;

        user.login = this.lookupReference('username').getValue();
        user.password = this.lookupReference('password').getValue();

        // Success
        var successCallback = function(result, request){
            // Get User Info and Permissions
            var myResult = Ext.decode(result.responseText);
            _SM.__language = myResult.language;
            _SM._UserInfo = myResult.userInfo;

            // Set the localStorage value ( Security isue )
            localStorage.setItem("SmLoggedIn", user.login);
            localStorage.setItem("SmUserInfo", Ext.encode(_SM._UserInfo))
            localStorage.setItem("SmLanguage", Ext.encode(_SM.__language))
            _SM._UserInfo.perms = {};

            // Destroy Login Window and Add the main view to the viewport
            view.destroy();

            // Alternatives : this.redirectTo('main') or route
            Ext.create({
                xtype : 'app-main'
            });
        };

        // Failure
        var failureCallback = function(result, request){
            // Show login failure error
            Ext.Msg.alert('Login Failure', result.statusText);
            btn.enable();
        };

        // Login using server-side authentication service
        Ext.Ajax.request({
            method : 'POST',
            scope : me,
            url : _SM._PConfig.urlGetUserRights,
            params : user,
            success : successCallback,
            failure : failureCallback
        });

    },

    resetPassword : function(btn){
        Ext.create('Softmachine.view.login.PwdLost').show();
    },

    changePassword : function(btn){
        Ext.create('Softmachine.view.login.PwdReset').show();
    }

});