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
        'Softmachine.view.main.MainController' ],

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
            items : [ {
                title : 'Menu',
                region : 'west',
                xtype : 'panel',
                margin : '5 0 0 5',
                width : 200,
                collapsible : true, // make collapsible
                id : 'west-region-container',
                layout : 'fit'
            }, {
                // xtype: 'panel' implied by default
                title : 'Center Region',
                region : 'center', // center region is required, no width/height specified
                xtype : 'panel',
                layout : 'fit',
                margin : '5 5 0 0'
            }, {
                title : 'Status',
                region : 'south', // position for region
                xtype : 'panel',
                height : 100,
                split : true, // enable resizing
                margin : '0 5 5 5'

            }, {
                title : 'Header',
                region : 'north', // position for region
                xtype : 'panel',
                height : 100,
                split : true, // enable resizing
                margin : '0 5 5 5', 
                collapsible: true,
                collapseMode: 'mini',
                collapsed: _SM._siteTitleCollapsed, 

                // To hide title bar, having title 
                header: false

            }
            // this.createHeaderPanel(),
            // this.createFooterPanel(),
            // this.createMenuPanel(),
            // this.createProtoTabContainer()
            ]

        });

        this.callParent();

    },

    createFooterPanel : function(){

        // StatusBar Global
        _SM.__StBar = Ext.create('Ext.ux.StatusBar', {
            region : 'south',
            split : false,
            collapsible : false
        });
        if (_SM.showFooterExtraContent) {
            var panelContent = Ext.create('Ext.panel.Panel', {
                html : _SM.footerExtraContent,
                margins : '0 0 0 0',
                border : false,
                align : 'middle',
                collapsible : true,
                split : true
            });
            var vbox = Ext.create('Ext.panel.Panel', {
                region : 'south',
                header : false,
                layout : {
                    type : 'vbox',
                    align : 'stretch'
                },
                defaults : {
                    bodyStyle : 'padding:15px',
                    split : true
                },
                items : [ _SM.__StBar, panelContent ]
            });
            return vbox;
        } else {
            return _SM.__StBar;
        }

    },

    createHeaderPanel : function(){
        var content = Ext.create('Ext.panel.Panel', {
            html : _SM._siteTitle,
            margins : '0 0 0 0',
            border : false,
            align : 'middle',
            split : true
        });
        var headerPanel = Ext.create('Ext.panel.Panel', {
            region : 'north',
            header : false,
            collapsible : true,
            collapseMode : 'mini',
            collapsed : _SM._siteTitleCollapsed,
            height : 90,
            layout : {
                type : 'vbox',
                align : 'stretch'
            },
            defaults : {
                bodyStyle : 'padding:5px',
                split : true
            },
            items : [ content ]
        });
        return headerPanel;
    },

    createMenuPanel : function(){

        if (_SM._MENU_COLLAPSED == undefined) {
            _SM._MENU_COLLAPSED = false;
        }

        this.menuPanel = {
            region : 'west',
            width : 300,
            title : _SM.__language.Title_Main_Menu,
            collapsible : true,
            collapsed : _SM._MENU_COLLAPSED,

            xtype : 'menuTree'

        };

        return this.menuPanel;
    },

    createProtoTabContainer : function(){
        this.protoTabContainer = Ext.create('widget.protoTabContainer', {
            region : 'center',
            border : false,
            minWidth : 300
        });
        return this.protoTabContainer;
    }

});
