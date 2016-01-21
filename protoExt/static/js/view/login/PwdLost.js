Ext.define('Softmachine.view.login.PwdLost', {
    extend : 'Ext.window.Window',
    alias : 'widget.forgotPasswordForm',

    title : _SM.__language.Title_Window_Email_Request,
    iconCls : 'st-user-who',

    floating : true,
    closable : true,
    modal : true,
    width : 600,
    height : 200,
    bodyPadding : 5,
    labelWidth : 160,

    // Fields will be arranged vertically, stretched to full width
    layout : 'anchor',
    defaults : {
        anchor : '100%',
        enableKeyEvents : true
    },

    items : [
        {
            xtype : 'form',
            bodyPadding : 25,
            centered : true,

            fieldDefaults : {
                anchor : '100%',
                labelAlign : 'left',
                allowBlank : false,
                combineErrors : true,
                msgTarget : 'side',
                labelWidth : 80
            },
            items : [
                {
                    xtype : 'textfield',
                    fieldLabel : _SM.__language.Textfield_User_Login,
                    name : 'login',
                    allowBlank : false,
                    flex : 1,
                    listeners : {
                        afterrender : function(field){
                            field.focus(false, 500);
                        },
                        blur : function(){
                            this.setValue(Ext.String.trim(this.getValue()));
                        }
                    }
                },
                {
                    xtype : 'textfield',
                    fieldLabel : _SM.__language.Textfield_User_Email,
                    name : 'email',
                    vtype : 'email',
                    allowBlank : false,
                    flex : 1,
                    listeners : {
                        specialkey : function(f, e){
                            if (e.getKey() == e.ENTER) {
                                var submitButton = Ext.ComponentQuery
                                        .query('button[itemId=btForgotPWDForm]')[0];
                                submitButton.fireEvent('click', submitButton);
                            }
                        }
                    }
                }
            ]
        }
    ],

    dockedItems : [
        {
            xtype : 'toolbar',
            dock : 'bottom',
            ui : 'footer',
            items : [
                '->',
                {
                    text : _SM.__language.Text_Send_Button,
                    itemId : 'btForgotPWDForm',
                    iconCls : "st-key-go",
                    action : 'forgotpassword',
                }
            ]
        }
    ],

});
