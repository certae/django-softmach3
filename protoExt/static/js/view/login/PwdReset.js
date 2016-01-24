Ext.define('Softmachine.view.login.PwdReset', {
    extend : 'Ext.window.Window',
    alias : 'widget.pwdResetForm',

    iconCls : 'st-key-go',
    title : _SM.__language.Title_Window_Password_Change,

    floating : true,
    closable : true,
    modal : true,
    width : 450,
    // height : 250,
    bodyPadding : 5,
    labelWidth : 160,

    // The fields
    username : '',

    controller : 'login',

    items : {
        xtype : 'form',
        reference : 'pwdReset',

        bodyStyle : "padding:10px",
        labelWidth : 160,
        labelAlign : 'right',
        redirectUrl : false,

        layout : 'anchor',
        defaultType : 'textfield',

        defaults : {
            anchor : '100%',
            enableKeyEvents : true
        },
        items : [
            {
                fieldLabel : _SM.__language.Textfield_User_Login,
                name : "login",
                value : this.username,
                allowBlank : false,
            },
            {
                fieldLabel : _SM.__language.Textfield_Password_Login,
                inputType : 'password',
                name : 'current',
                allowBlank : false
            },
            {
                fieldLabel : _SM.__language.Textfield_New_Password,
                name : 'newPassword1',
                inputType : 'password',
                allowBlank : false
            },
            {
                fieldLabel : _SM.__language.Textfield_Confirm_Password,
                name : 'newPassword2',
                inputType : 'password',
                allowBlank : false,
            }
        ],

        // Reset and Submit buttons
        buttons : [
            {
                text : _SM.__language.Text_change_Password_Button,
                itemId : 'btPwdResetSubmit',
                iconCls : 'st-key-go',
                formBind : true,
                disabled : true,

                listeners : {
                    click : 'doPwdReset'
                }

            }
        ],
    },

});
