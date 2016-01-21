Ext.define('Softmachine.view.login.PwdReset', {
    extend : 'Ext.window.Window',
    alias : 'widget.pwdResetForm',

    iconCls : 'st-key-go',
    title : _SM.__language.Title_Window_Password_Change,

    floating : true,
    closable : true,
    modal : true,
    width : 600,
    // height : 250,
    bodyPadding : 5,
    labelWidth : 160,


    // The fields
    username : '',

    items : {
        xtype : 'form',
        reference : 'pwdReset',

        bodyStyle : "padding:10px",
        labelWidth : 160,
        labelAlign : 'right',
        redirectUrl : false,
    
        layout : 'anchor',
        defaultType: 'textfield',

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
                // listeners : {
                //     afterrender : function(field){
                //         field.focus(false, 500);
                //     }
                // }
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
            // listeners : {
            // // this is used to fire the click event, so the PasswordManager is able to
            // // capture the form.
            // specialkey : function(f, e){
            // if (e.getKey() == e.ENTER) {
            // var changeButton = Ext.ComponentQuery
            // .query('button[itemId=btChangePWD]')[0];
            // changeButton.fireEvent('click', changeButton);
            // }
            // }
            // }
            }
        ],

        // Reset and Submit buttons
        buttons : [
            {
                text : _SM.__language.Text_change_Password_Button,
                itemId : 'btChangePWD',
                iconCls : 'st-key-go',
                formBind : true,
                disabled : true,
                action : 'changepassword'
            }
        ],
        // listeners : {
        //     afterlayout : function(){
        //         if (window.isPwdReseted === 'True') {
        //             setTimeout(function(){
        //                 Ext.Msg.show({
        //                     title : _SM.__language.Message_Success,
        //                     msg : _SM.__language.Message_Email_New_Password,
        //                     buttons : Ext.Msg.OK,
        //                     icon : Ext.MessageBox.INFO
        //                 });
        //             }, 1000);
        //         }
        //     }
        // },
    },

});
