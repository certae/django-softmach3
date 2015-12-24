// -----------
Ext.create("Admin.view.authentication.Dialog", Ext.form.Panel, {
    controller : "authentication",
    viewModel : {
        type : "authentication"
    },
    defaultFocus : "textfield:focusable:not([hidden]):not([disabled]):not([value])",
    autoComplete : false,
    initComponent : function(){
        var b = this, a;
        if (b.autoComplete) {
            b.autoEl = Ext.applyIf(b.autoEl || {}, {
                tag : "form",
                name : "authdialog",
                method : "post"
            })
        }
        b.addCls("auth-dialog");
        Ext.form.Panel.prototype.initComponent.call(this);
        if (b.autoComplete) {
            a = {
                afterrender : "doAutoComplete",
                scope : b,
                single : true
            };
            Ext.each(b.query("textfield"), function(c){
                c.on(a)
            })
        }
    },
    doAutoComplete : function(a){
        if (a.inputEl && a.autoComplete !== false) {
            a.inputEl.set({
                autocomplete : "on"
            })
        }
    }
}, 0, [ "authdialog" ], [ "component", "box", "container", "panel", "form", "authdialog" ], {
    component : true,
    box : true,
    container : true,
    panel : true,
    form : true,
    authdialog : true
}, [ "widget.authdialog" ], 0, [ Admin.view.authentication, "Dialog" ], 0));


// -----------
Ext.create("Admin.view.authentication.LockingWindow", Ext.window.Window, {
    cls : "auth-locked-window",
    closable : false,
    resizable : false,
    autoShow : true,
    titleAlign : "center",
    maximized : true,
    modal : true,
    frameHeader : false,
    layout : {
        type : "vbox",
        align : "center",
        pack : "center"
    }
}, 0, [ "lockingwindow" ], [ "component", "box", "container", "panel", "window", "lockingwindow" ],
        {
            component : true,
            box : true,
            container : true,
            panel : true,
            window : true,
            lockingwindow : true
        }, [ "widget.lockingwindow" ], 0, [ Admin.view.authentication, "LockingWindow" ], 0));



// -----------
Ext.create("Admin.view.authentication.LockScreen",
                Admin.view.authentication.LockingWindow,
                {
                    title : "Session Expired",
                    defaultFocus : "authdialog",
                    items : [ {
                        xtype : "authdialog",
                        reference : "authDialog",
                        defaultButton : "loginButton",
                        autoComplete : false,
                        width : 455,
                        cls : "auth-dialog-login",
                        defaultFocus : "textfield[inputType=password]",
                        layout : {
                            type : "vbox",
                            align : "stretch"
                        },
                        items : [
                            {
                                xtype : "container",
                                cls : "auth-profile-wrap",
                                height : 120,
                                layout : {
                                    type : "hbox",
                                    align : "center"
                                },
                                items : [
                                    {
                                        xtype : "image",
                                        height : 80,
                                        margin : 20,
                                        width : 80,
                                        alt : "lockscreen-image",
                                        cls : "lockscreen-profile-img auth-profile-img",
                                        src : "resources/images/user-profile/2.png"
                                    },
                                    {
                                        xtype : "box",
                                        html : "<div class='user-name-text'> Goff Smith </div><div class='user-post-text'> Project manager </div>"
                                    } ]
                            },
                            {
                                xtype : "container",
                                padding : "0 20",
                                layout : {
                                    type : "vbox",
                                    align : "stretch"
                                },
                                defaults : {
                                    margin : "10 0"
                                },
                                items : [
                                    {
                                        xtype : "textfield",
                                        labelAlign : "top",
                                        cls : "lock-screen-password-textbox",
                                        labelSeparator : "",
                                        fieldLabel : "It's been a while. please enter your password to resume",
                                        emptyText : "Password",
                                        inputType : "password",
                                        allowBlank : false,
                                        triggers : {
                                            glyphed : {
                                                cls : "trigger-glyph-noop password-trigger"
                                            }
                                        }
                                    },
                                    {
                                        xtype : "button",
                                        reference : "loginButton",
                                        scale : "large",
                                        ui : "soft-blue",
                                        iconAlign : "right",
                                        iconCls : "x-fa fa-angle-right",
                                        text : "Login",
                                        formBind : true,
                                        listeners : {
                                            click : "onLoginButton"
                                        }
                                    },
                                    {
                                        xtype : "component",
                                        html : '<div style="text-align:right"><a href="#authentication.login" class="link-forgot-password">or, sign in using other credentials</a></div>'
                                    } ]
                            } ]
                    } ]
                }, 0, [ "lockscreen" ], [
                    "component",
                    "box",
                    "container",
                    "panel",
                    "window",
                    "lockingwindow",
                    "lockscreen" ], {
                    component : true,
                    box : true,
                    container : true,
                    panel : true,
                    window : true,
                    lockingwindow : true,
                    lockscreen : true
                }, [ "widget.lockscreen" ], 0, [ Admin.view.authentication, "LockScreen" ], 0));



