/* app.js ----------------------
 * This file is generated and updated by Sencha Cmd. You can edit this file as
 * needed for your application, but these edits will have to be merged by
 * Sencha Cmd when upgrading.
 * Licence GPLv3, 
 * CeRTAE, Dario Gomez 
 */


Ext.application({
    name: 'Softmachine',
    extend: 'Softmachine.Application',

    requires: [
        'Softmachine.view.main.Main'
    ],

    // The name of the initial view to create. With the classic toolkit this class
    // will gain a "viewport" plugin if it does not extend Ext.Viewport. With the
    // modern toolkit, the main view will be added to the Viewport.
    //
    // mainView: 'Softmachine.view.main.Main'
    
    //-------------------------------------------------------------------------
    // Most customizations should be made to Softmachine.Application. If you need to
    // customize this file, doing so below this section reduces the likelihood
    // of merge conflicts when upgrading to new versions of Sencha Cmd.
    //-------------------------------------------------------------------------
});



// Ext.application({
//     name: 'ProtoUL',
    
//     appFolder: 'static/js',
//     paths: {
//         'ProtoUL': 'static/js'
//     },

//     extend: 'ProtoUL.Application',
//     launch: function() {

//         Ext.QuickTips.init();

//         if (window.isPasswordReseted === 'True') {
//             this.showResetPasswordForm();
//         } else {
//             this.showLogin();
//         }

//     },
//     showLogin: function() {

//         var me = this;

//         var options = {
//             scope: me,
//             success: function(obj, result, request) {
//                 myWin.hide();

//                 // Globally changing the text of Cancel and Save buttons;
//                 Ext.grid.RowEditor.prototype.saveBtnText = _SM.__language.Text_Save_Button;
//                 Ext.grid.RowEditor.prototype.cancelBtnText = _SM.__language.Text_Cancel_Button;

//                 var app = new ProtoUL.view.Viewport();

//                 Ext.destroy(Ext.ComponentQuery.query('protoLogin'));

//             }
//         };


//     showResetPasswordForm: function() {
//         var resetForm = Ext.create('ProtoUL.view.password.PasswordReset');
//         resetForm.show();
//     }
// });

