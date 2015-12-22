/**
 * This class is the main view for the application. It is specified in app.js as the "mainView"
 * property. That setting automatically applies the "viewport" plugin causing this view to become
 * the body element (i.e., the viewport).
 * 
 * TODO - Replace this content of this view to suite the needs of your application.
 */
Ext.define('Softmachine.view.main.Main', {
    extend : 'Ext.container.Viewport',
    alias : 'widget.mainview',
    xtype : 'app-main',

    requires : [
        'Ext.panel.Panel',
        'Ext.plugin.Viewport',
        'Ext.button.Button',
        'Ext.window.MessageBox',
        'Ext.ux.statusbar.StatusBar',

        'Softmachine.view.main.MainController', 
        'Softmachine.view.main.MenuTree' ],

    controller : 'main',
    // viewModel: 'main',
    plugins : 'viewport',
    ui : 'navigation',
    layout : 'border',

    initComponent : function(){

        Ext.apply(this, {
            autoRender : true,
            padding : 5,
            defaults : {
                split : true
            },
            items : [ 
                this.createHeaderPanel(), 
                this.createMenuPanel(),
                this.createProtoTabContainer()
            ]

        });

        this.callParent();

    },

    createHeaderPanel : function(){

        var myPanel = {
            id : 'vp-header',
            title : 'Header',
            header : false, // To hide title bar, having title for ARIA
            region : 'north', // position for region
            xtype : 'panel',
            id : 'vp-header',

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
            xtype : 'menuTree',
            title : _SM.__language.Title_Main_Menu || 'Menu',
            region : 'west',
            margin : '5 0 0 5',
            width : 260,
            collapsible : true, // make collapsible
            collapsed : _SM._MENU_COLLAPSED || false,

            id : 'vp-menu',
            layout : 'fit'
        };

        return myPanel;

    },

    createProtoTabContainer : function(){

        var myPanel = {
            // xtype: 'panel' implied by default
            title : 'Center Region',
            region : 'center', // center region is required, no width/height specified
            xtype : 'panel',
            layout : 'fit',
            minWidth : 300, 
            header : false, // To hide title bar, having title for ARIA

            bbar : Ext.create('Ext.ux.StatusBar', {
                defaultText : '',
                id : 'vp-statusbar',
                items : [ {
                    itemId : 'btClearCache',
                    xtype : 'button',
                    text : _SM.__language.StatusBar_Text_Clean_Button || 'Clear' + ' cache',
                    tooltip : _SM.__language.StatusBar_Tooltip_Clean_Button,
                    iconCls : 'comment_delete',
                    handler : function(){
                        this.tooltip = '';
                        this.ownerCt.clearStatus({
                            useDefaults : true
                        });
                        _SM.__TabContainer.closeAllTabs();
                        _SM._cllPCI = {};
                    }
                }, {
                    itemId : 'openTaskForm',
                    xtype : 'button',
                    text : _SM.__language.StatusBar_Text_Task_Button,
                    hidden : true,
                    scope : this,
                    iconCls : 'taskManager',
                    handler : this.openTaskForm

                }, '-', {

                    xtype : 'splitbutton',
                    text : localStorage.getItem("SmLoggedIn"),
                    iconCls : 'icon-user',
                    menu : new Ext.menu.Menu({
                        items : [ {
                            text : _SM.__language.StatusBar_Text_Close_Session,
                            handler : this.closeSession,
                            iconCls : 'icon-logout'
                        } ]
                    })
                } ]
            })
        };

        return myPanel;
    },


});
