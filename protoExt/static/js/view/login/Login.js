
Ext.define('Softmachine.view.login.Login', {
    extend : 'Ext.window.Window',
    xtype : 'login',

    iconCls : 'st-user-who',
    layout : 'fit',
    width : 450,

    requires : [
        'Softmachine.view.login.LoginController'
    ],

    controller : 'login',
    bodyPadding : 10,
    title : 'Login Window',
    closable : false,
    autoShow : true,


    items : {
        xtype : 'form',
        reference : 'form',

        bodyStyle : "padding:10px",
        labelWidth : 120,
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
                allowBlank : false
            },
            {
                xtype : 'textfield',
                name : 'password',
                reference : 'password',
                inputType : 'password',
                fieldLabel : _SM.__language.Textfield_Password_Login,
                allowBlank : false
            }
        ],
        buttons : [
            {
                // text: _SM.__language.Text_Forgotten_Password,
                // iconCls: "st-user-who",
                // listeners: {
                // click: 'resetPassword'
                // }
                // }, {
                // text: _SM.__language.Text_change_Password_Button,
                // iconCls: "st-key-go",
                // listeners: {
                // click: 'changePassword'
                // }
                // },{
                text : _SM.__language.Text_Validate_Login_Button,
                iconCls : "st-user-go",
                formBind : true,
                listeners : {
                    click : 'submitLogin'
                }
            }
        ]
    }, 
    // initComponent : function(){
    //     var a = 1; 
    // }
});
