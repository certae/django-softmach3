(Ext.cmd.derive("Admin.view.authentication.AuthenticationController", Ext.app.ViewController, {
    onFaceBookLogin : function(a, b){
        this.redirectTo("dashboard")
    },
    onLoginButton : function(b, c, a){
        this.redirectTo("dashboard")
    },
    onLoginAsButton : function(b, c, a){
        this.redirectTo("authentication.login")
    },
    onNewAccount : function(b, c, a){
        this.redirectTo("authentication.register")
    },
    onSignupClick : function(b, c, a){
        this.redirectTo("dashboard")
    },
    onResetClick : function(b, c, a){
        this.redirectTo("dashboard")
    }
}, 0, 0, 0, 0, [ "controller.authentication" ], 0, [
    Admin.view.authentication,
    "AuthenticationController" ], 0));