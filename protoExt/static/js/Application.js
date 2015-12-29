/**
 * The main application class. An instance of this class is created by app.js when it
 * calls Ext.application(). This is the ideal place to handle application launch and
 * initialization details.
 * Licence GPLv3, 
 * CeRTAE, Dario Gomez 
 */

Ext.Loader.setConfig({
    enabled: true,
    paths : {  
        'Softmachine' : 'static/js', 
        'Softmachine.view' : 'static/js/view'
    }
});

Ext.define('Softmachine.Application', {
    extend: 'Ext.app.Application',
    name: 'Softmachine',

    stores: [
        // TODO: add global / shared stores here
    ],

    views: [
        'Softmachine.view.login.Login',
        'Softmachine.view.main.Main'
    ],
    
    launch: function () {

        // It's important to note that this type of application could use
        // any type of storage, i.e., Cookies, LocalStorage, etc.
        var loggedIn;

        // Check to see the current value of the localStorage key
        loggedIn = localStorage.getItem("SmLoggedIn");
        if ( loggedIn ) {
            _SM._UserInfo = _SM.obj2tx( localStorage.getItem("SmUserInfo" ));
            if ( ! _SM._UserInfo ) { loggedIn = false }
        } else { 
            _SM._UserInfo = { perms : {}, isStaff : false }; 
        }

        // This ternary operator determines the value of the SmLoggedIn key.
        // If SmLoggedIn isn't true, we display the login window,
        // otherwise, we display the main view

        getLanguage()

        Ext.create({
            xtype: loggedIn ? 'app-main' : 'login'
        });

        function getLanguage(){
            _SM.__language = _SM.__language.fr
        }
        

    },

    onAppUpdate: function () {
        Ext.Msg.confirm('Application Update', 'This application has an update, reload?',
            function (choice) {
                if (choice === 'yes') {
                    window.location.reload();
                }
            }
        );
    }
});

// Add csrf token to every ajax request
Ext.Ajax.on('beforerequest', function(conn, options) {
    if ( typeof (options.headers) == "undefined") {
        options.headers = {
            'X-CSRFToken': Ext.util.Cookies.get('csrftoken')
        };
    } else {
        options.headers.extend({
            'X-CSRFToken': Ext.util.Cookies.get('csrftoken')
        });
    }
}, this);
