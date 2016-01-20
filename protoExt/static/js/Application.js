/**
 * The main application class. An instance of this class is created by app.js when it calls
 * Ext.application(). This is the ideal place to handle application launch and initialization
 * details. Licence GPLv3, CeRTAE, Dario Gomez
 */


// There is only one langbase loaded in main page 
_SM.__language = _SM.__langbase

Ext.Loader.setConfig({
    enabled : true,
    paths : {
        'Softmachine' : 'static/js',
        'Softmachine.view' : 'static/js/view', 
        'ProtoUL.ux' : 'static/js/ux', 

        'ProtoUL.proto' : 'static/js/proto', 
        'ProtoUL.proto.model' : 'static/js/proto/model', 
    }
});

Ext.define('Softmachine.Application', {
    extend : 'Ext.app.Application',
    name : 'Softmachine',

    stores : [
    // TODO: add global / shared stores here
    ],

    views : [
        'Softmachine.view.login.Login',
        'Softmachine.view.main.Main'
    ],

    launch : function(){

        // It's important to note that this type of application could use
        // any type of storage, i.e., Cookies, LocalStorage, etc.
        var loggedIn;

        // Check to see the current value of the localStorage key
        loggedIn = localStorage.getItem("SmLoggedIn");
        if (loggedIn) {
            _SM._UserInfo = Ext.decode(localStorage.getItem("SmUserInfo"));
            _SM.__language = Ext.decode(localStorage.getItem("SmLanguage"));
            if (!_SM._UserInfo) {
                loggedIn = false
            } else {
                _SM._UserInfo.perms = {}
            }
        }

        if (!loggedIn) {
            _SM._UserInfo = {
                perms : {},
                isStaff : false
            };
        }

        // This ternary operator determines the value of the SmLoggedIn key.
        // If SmLoggedIn isn't true, we display the login window,
        // otherwise, we display the main view
        Ext.create({
            xtype : loggedIn ? 'app-main' : 'login'
        });

    },

    onAppUpdate : function(){
        Ext.Msg.confirm('Application Update', 'This application has an update, reload?', function(
                choice)
        {
            if (choice === 'yes') {
                window.location.reload();
            }
        });
    }
});

// Add csrf token to every ajax request
Ext.Ajax.on('beforerequest', function(conn, options){
    if (typeof (options.headers) == "undefined") {
        options.headers = {
            'X-CSRFToken' : Ext.util.Cookies.get('csrftoken')
        };
    } else {
        options.headers.extend({
            'X-CSRFToken' : Ext.util.Cookies.get('csrftoken')
        });
    }
}, this);
