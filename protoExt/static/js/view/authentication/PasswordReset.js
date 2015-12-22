
// -----------
Ext.create("Admin.view.authentication.PasswordReset",
                Admin.view.authentication.LockingWindow,
                {
                    title : "Reset Password",
                    defaultFocus : "authdialog",
                    items : [ {
                        xtype : "authdialog",
                        width : 455,
                        defaultButton : "resetPassword",
                        autoComplete : true,
                        bodyPadding : "20 20",
                        layout : {
                            type : "vbox",
                            align : "stretch"
                        },
                        defaults : {
                            margin : "10 0"
                        },
                        cls : "auth-dialog-login",
                        items : [
                            {
                                xtype : "label",
                                cls : "lock-screen-top-label",
                                text : "Enter your email address for further reset instructions"
                            },
                            {
                                xtype : "textfield",
                                cls : "auth-textbox",
                                height : 55,
                                name : "email",
                                hideLabel : true,
                                allowBlank : false,
                                emptyText : "user@example.com",
                                vtype : "email",
                                triggers : {
                                    glyphed : {
                                        cls : "trigger-glyph-noop auth-email-trigger"
                                    }
                                }
                            },
                            {
                                xtype : "button",
                                reference : "resetPassword",
                                scale : "large",
                                ui : "soft-blue",
                                formBind : true,
                                iconAlign : "right",
                                iconCls : "x-fa fa-angle-right",
                                text : "Reset Password",
                                listeners : {
                                    click : "onResetClick"
                                }
                            },
                            {
                                xtype : "component",
                                html : '<div style="text-align:right"><a href="#authentication.login" class="link-forgot-password">Back to Log In</a></div>'
                            } ]
                    } ]
                }, 0, [ "passwordreset" ], [
                    "component",
                    "box",
                    "container",
                    "panel",
                    "window",
                    "lockingwindow",
                    "passwordreset" ], {
                    component : true,
                    box : true,
                    container : true,
                    panel : true,
                    window : true,
                    lockingwindow : true,
                    passwordreset : true
                }, [ "widget.passwordreset" ], 0, [ Admin.view.authentication, "PasswordReset" ], 0));


