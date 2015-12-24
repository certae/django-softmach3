Ext.create('Ext.tab.Panel', {
    width : 300,
    height : 200,
    activeTab : 0,
    dockedItems : [
        {
            xtype : 'toolbar',
            dock : 'top',
            items : [
                {
                    xtype : 'button',
                    text : 'Button 1'
                }
            ]
        }
    ],

    items : [
        {
            title : 'Tab 1',
            bodyPadding : 10,
            html : 'A simple tab'
        },
        {
            title : 'Tab 2',
            html : 'Another one'
        }
    ],
    renderTo : Ext.getBody()
});