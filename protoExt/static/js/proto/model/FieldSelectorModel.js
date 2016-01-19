Ext.define('ProtoUL.proto.model.FieldSelectorModel', {
    extend : 'Ext.data.Model',
    proxy : {
        type : 'ajax',
        url : _SM._PConfig.urlGetFieldTree,
        actionMethods : {
            read : 'POST'
        },
    },

    fields : [
        // Contiene el nombre en notacion objeto ( django )
        {
            name : 'id',
            type : 'string'
        },

        // Contiene el nombre del campo dentro del modelo
        {
            name : 'text',
            type : 'string'
        },
        {
            name : 'type',
            type : 'string'
        },

        {
            name : 'readOnly',
            type : 'boolean'
        },
        {
            name : 'required',
            type : 'boolean'
        },
        {
            name : 'tooltip',
            type : 'string'
        },
        {
            name : 'header',
            type : 'string'
        },

        {
            name : 'zoomModel',
            type : 'string'
        },
        {
            name : 'fkField',
            type : 'string'
        },
        {
            name : 'fkId',
            type : 'string'
        },
        {
            name : 'vType',
            type : 'string'
        },
        {
            name : 'prpDefault',
            type : 'string'
        },
        {
            name : 'choices',
            type : 'string'
        },

        {
            name : 'cpFromZoom',
            type : 'string'
        },
        {
            name : 'cpFromField',
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