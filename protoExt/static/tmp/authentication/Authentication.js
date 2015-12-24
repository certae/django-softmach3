// -----------
Ext.define("Admin.view.authentication.Register",
                {
                    extend : "Admin.view.authentication.LockingWindow",

                    title : "User Registration",
                    defaultFocus : "authdialog",
                    items : [ {
                        xtype : "authdialog",
                        bodyPadding : "20 20",
                        width : 455,
                        reference : "authDialog",
                        defaultButton : "submitButton",
                        autoComplete : true,
                        cls : "auth-dialog-register",
                        layout : {
                            type : "vbox",
                            align : "stretch"
                        },
                        defaults : {
                            margin : "10 0",
                            selectOnFocus : true
                        },
                        items : [
                            {
                                xtype : "label",
                                cls : "lock-screen-top-label",
                                text : "Create an account"
                            },
                            {
                                xtype : "textfield",
                                cls : "auth-textbox",
                                height : 55,
                                hideLabel : true,
                                allowBlank : false,
                                emptyText : "Fullname",
                                name : "fullName",
                                bind : "{fullName}",
                                triggers : {
                                    glyphed : {
                                        cls : "trigger-glyph-noop auth-email-trigger"
                                    }
                                }
                            },
                            {
                                xtype : "textfield",
                                cls : "auth-textbox",
                                height : 55,
                                hideLabel : true,
                                allowBlank : false,
                                name : "userid",
                                bind : "{userid}",
                                emptyText : "Username",
                                triggers : {
                                    glyphed : {
                                        cls : "trigger-glyph-noop auth-email-trigger"
                                    }
                                }
                            },
                            {
                                xtype : "textfield",
                                cls : "auth-textbox",
                                height : 55,
                                hideLabel : true,
                                allowBlank : false,
                                name : "email",
                                emptyText : "user@example.com",
                                vtype : "email",
                                bind : "{email}",
                                triggers : {
                                    glyphed : {
                                        cls : "trigger-glyph-noop auth-envelope-trigger"
                                    }
                                }
                            },
                            {
                                xtype : "textfield",
                                cls : "auth-textbox",
                                height : 55,
                                hideLabel : true,
                                allowBlank : false,
                                emptyText : "Password",
                                name : "password",
                                inputType : "password",
                                bind : "{password}",
                                triggers : {
                                    glyphed : {
                                        cls : "trigger-glyph-noop auth-password-trigger"
                                    }
                                }
                            },
                            {
                                xtype : "checkbox",
                                flex : 1,
                                name : "agrees",
                                cls : "form-panel-font-color rememberMeCheckbox",
                                height : 32,
                                bind : "{agrees}",
                                allowBlank : false,
                                boxLabel : "I agree with the Terms and Conditions",
                                isValid : function(){
                                    var a = this;
                                    return a.checked || a.disabled
                                }
                            },
                            {
                                xtype : "button",
                                scale : "large",
                                ui : "soft-blue",
                                formBind : true,
                                reference : "submitButton",
                                bind : false,
                                margin : "5 0",
                                iconAlign : "right",
                                iconCls : "x-fa fa-angle-right",
                                text : "Signup",
                                listeners : {
                                    click : "onSignupClick"
                                }
                            },
                            {
                                xtype : "box",
                                html : '<div class="outer-div"><div class="seperator">OR</div></div>'
                            },
                            {
                                xtype : "button",
                                scale : "large",
                                ui : "soft-blue",
                                margin : "5 0",
                                iconAlign : "right",
                                iconCls : "x-fa fa-facebook",
                                text : "Login with Facebook",
                                listeners : {
                                    click : "onFaceBookLogin"
                                }
                            },
                            {
                                xtype : "component",
                                html : '<div style="text-align:right"><a href="#authentication.login" class="link-forgot-password">Back to Log In</a></div>'
                            } ]
                    } ]
                }, 0, [ "authregister" ], [
                    "component",
                    "box",
                    "container",
                    "panel",
                    "window",
                    "lockingwindow",
                    "authregister" ], {
                    component : true,
                    box : true,
                    container : true,
                    panel : true,
                    window : true,
                    lockingwindow : true,
                    authregister : true
                }, [ "widget.authregister" ], 0, [ Admin.view.authentication, "Register" ], 0));