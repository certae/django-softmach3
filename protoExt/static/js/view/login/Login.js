Ext.define('Softmachine.view.login.Login', {
    extend : 'Ext.window.Window',
    xtype : 'login',

    iconCls : 'st-user-go',
    title : 'Login Window',

    closable : false,
    autoShow : true,

    layout : 'fit',
    width : 400,

    bodyPadding: 5,
    bodyPadding : 10,
    labelWidth: 160,

    requires : [
        'Softmachine.view.login.LoginController'
    ],

    controller : 'login',

    items : {
        xtype : 'form',
        reference : 'form',

        bodyStyle : "padding:10px",
        labelWidth : 160,
        labelAlign : 'right',
        redirectUrl : false,

        defaults : {
            xtype : "textfield",
            anchor : "100%",
            enableKeyEvents : true
        },

        items : [
            {
                xtype : 'textfield',
                name : 'username',
                reference : 'username',
                fieldLabel : _SM.__language.Textfield_User_Login,
                allowBlank : false, 
                value: this.username,
                listeners: {
                    keydown: 'onKeyEnter'
                }

            },
            {
                xtype : 'textfield',
                name : 'password',
                reference : 'password',
                inputType : 'password',
                fieldLabel : _SM.__language.Textfield_Password_Login,
                allowBlank : false, 
                listeners: {
                    keydown: 'onKeyEnter'
                }

            }
        ],
        buttons : [
            {
                text : _SM.__language.Text_Forgotten_Password,
                iconCls : "st-user-who",
                listeners : {
                    click : 'showLostPasswordForm'
                }
            },
            {
                text : _SM.__language.Text_change_Password_Button,
                iconCls : "st-key-go",
                listeners : {
                    click : 'showChangePasswordForm'
                }
            },
            {
                text : _SM.__language.Text_Validate_Login_Button,
                iconCls : "st-user-go",
                reference : 'submit',
                formBind : true,
                listeners : {
                    click : 'submitLogin'
                }
            }
        ]
    },
});
