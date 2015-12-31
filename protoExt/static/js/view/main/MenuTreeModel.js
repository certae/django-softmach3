Ext.define('Softmachine.view.main.MenuTreeModel', {
    extend : 'Ext.data.Model',
    proxy : {
        type : 'ajax',
        url : _SM._PConfig.urlMenu,
        extraParams : {
            forceDefault : 0
        },
        actionMethods : {
            read : 'POST'
        }
    },

    fields : [
        {
            name : 'id',
            type : 'string'
        },
        {
            name : 'viewCode',
            type : 'string'
        },
        {
            name : 'text',
            type : 'string'
        },
        {
            name : 'leaf',
            type : 'boolean'
        }
    ]

});


