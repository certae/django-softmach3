/**
 * This class is the main view for the application. It is specified in app.js as the
 * "mainView" property. That setting automatically applies the "viewport"
 * plugin causing this view to become the body element (i.e., the viewport).
 *
 * TODO - Replace this content of this view to suite the needs of your application.
 */
Ext.define('Softmachine.view.main.Main', {
    extend: 'Ext.container.Viewport',
    alias: 'widget.mainview',
    xtype: 'app-main',

    requires: ['Ext.panel.Panel', 'Ext.plugin.Viewport', 'Ext.button.Button', 'Ext.window.MessageBox', 'Softmachine.view.main.MainController'],

    controller: 'main',
    // viewModel: 'main',
    plugins: 'viewport',

    ui: 'navigation',

    layout: 'border',

    items: [{
        xtype: 'panel',
        region: 'north',
        height: 100,
        title: 'Sistema',
        dockedItems: [{
            xtype: 'panel',
            dock: 'right',
            reference: 'loginPanel',
            layout: {
                type: 'hbox',
                align: 'stretch'
            },
            items: [{
                xtype: 'panel',
                flex: 8
            }, {
                xtype: 'button',
                margin: 6,
                flex: 1,
                text: 'Ingresar',
                height: 50,
                listeners: {
                    click: 'onLoginButtonClick'
                }
            }, {
                xtype: 'button',
                margin: 5,
                flex: 1,
                height: 50,
                text: 'Registrar',
                listeners: {
                    click: 'onRegisterButtonClick'
                }
            }]
        }, {
            xtype: 'panel',
            dock: 'right',
            reference: 'logoutPanel',
            hidden: true,
            layout: {
                type: 'hbox',
                align: 'stretch'
            },
            items: [{
                xtype: 'panel',
                flex: 8
            }, {
                xtype: 'button',
                margin: 6,
                flex: 1,
                text: 'Logout',
                listeners: {
                    click: 'onLogoutButtonClick'
                }
            }]
        }]
    }, {
        xtype: 'panel',
        region: 'center',
        itemId: 'contentPanel',
        layout: 'border',
        title: 'Ingreso'
    }]

});
