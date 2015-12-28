/**
 * This class is the main view for the application. It is specified in app.js as the "mainView"
 * property.
 * 
 * That setting automatically applies the "viewport" plugin causing this view to become the body
 * element (i.e., the viewport).
 * 
 */
Ext.define('Softmachine.view.main.Main', {
    extend : 'Ext.container.Viewport',
    alias : 'widget.app-main',
    xtype : 'app-main',

    requires : [
        'Ext.panel.Panel',
        'Ext.plugin.Viewport',
        'Ext.button.Button',
        'Ext.window.MessageBox',

        'Ext.ux.statusbar.StatusBar',

        'Softmachine.view.main.MainTabContainer',
        'Softmachine.view.main.MainController',
        'Softmachine.view.main.MenuTree'
    ],

    controller : 'main',
    // viewModel: 'main',
    plugins : 'viewport',
    ui : 'navigation',
    layout : 'border',

    initComponent : function(){

        _SM.vp_Main = this;

        Ext.apply(this, {
            autoRender : true,
            padding : 5,
            defaults : {
                split : true
            },
            items : [
                this.createHeaderPanel(),
                this.createMenuPanel(),
                this.createMainTabContainer()
            ]

        });

        this.callParent();


    },

    createHeaderPanel : function(){

        var myPanel = {
            id : 'vp-header',
            xtype : 'panel',
            title : 'Header',
            region : 'north', // position for region

            header : false, // To hide title bar, having title for ARIA
            align : 'middle',
            border : false,
            collapsed : _SM._siteTitleCollapsed,
            collapseMode : 'mini',
            collapsible : true,
            height : 100,
            split : true, // enable resizing
            html : _SM._siteTitle
        };

        return myPanel;
    },

    createMenuPanel : function(){

        var myPanel = {
            id : 'vp-menu',
            xtype : 'menuTree',
            title : _SM.__language.Title_Main_Menu || 'Menu',
            region : 'west',

            margin : '5 0 0 5',
            width : 260,
            collapsible : true, // make collapsible
            collapsed : _SM._MENU_COLLAPSED || false,
            layout : 'fit'
        };

        return myPanel;

    },

    createMainTabContainer : function(){

        var myPanel = {
            id : 'vp-workspace',
            xtype : 'mainTabContainer',
            title : 'WorkSpace',
            region : 'center',

            layout : 'fit',
            minWidth : 300,
            header : false, // To hide title bar, having title for ARIA
            bbar : this.createMainStatusBar()
        };

        _SM.WorkSpace = myPanel;
        return myPanel;
    },

    createMainStatusBar : function(){

        var me = this; 
        var myPanel = Ext.create('Ext.ux.StatusBar', {
            defaultText : '',
            id : 'vp-statusbar',
            items : [
                {
                    itemId : 'btClearCache',
                    xtype : 'button',
                    text : _SM.__language.StatusBar_Text_Clean_Button || 'Clear' + ' cache',
                    tooltip : _SM.__language.StatusBar_Tooltip_Clean_Button,
                    iconCls : 'comment_delete',
                    handler : me.controller.clearCache, 
                    scope : me.controller
                },
                {
                    itemId : 'openTaskForm',
                    xtype : 'button',
                    text : _SM.__language.StatusBar_Text_Task_Button,
                    hidden : true,
                    scope : me,
                    iconCls : 'taskManager',
                    handler : me.openTaskForm, 
                    scope : me.controller

                },
                '-',
                {

                    xtype : 'splitbutton',
                    text : localStorage.getItem("SmLoggedIn"),
                    iconCls : 'icon-user',
                    menu : new Ext.menu.Menu({
                        items : [
                            {
                                text : _SM.__language.StatusBar_Text_Close_Session || 'Logout',
                                handler : me.controller.closeSession,
                                scope : me.controller, 
                                iconCls : 'icon-logout'
                            }
                        ]
                    })
                }
            ]
        })

        _SM.vp_StatusBar = myPanel;
        _SM.vp_StatusBar.busyCount = 0 

        return myPanel;


    },

});
