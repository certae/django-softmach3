Ext.define('ProtoUL.proto.model.DetailsTreeModel', {
    extend : 'Ext.data.Model',
    proxy : {
        type : 'ajax',
        url : _SM._PConfig.urlGetDetailsTree,
        actionMethods : {
            read : 'POST'
        },
        extraParams : {
            viewCode : '',
            protoEntityId : -1
        }
    },

    fields : [
        {
            name : 'id',
            type : 'string'
        },
        {
            name : 'menuText',
            type : 'string'
        },
        {
            name : 'masterField',
            type : 'string'
        },
        {
            name : 'detailField',
            type : 'string'
        },
        {
            name : 'conceptDetail',
            type : 'string'
        },

        {
            name : 'checked',
            type : 'boolean'
        },
        {
            name : 'leaf',
            type : 'boolean'
        }
    ]

});
