(Ext.cmd.derive("Admin.view.authentication.AuthenticationModel", Ext.app.ViewModel, {
    data : {
        userid : "",
        fullName : "",
        password : "",
        email : "",
        persist : false,
        agrees : false
    }
}, 0, 0, 0, 0, [ "viewmodel.authentication" ], 0, [
    Admin.view.authentication,
    "AuthenticationModel" ], 0));