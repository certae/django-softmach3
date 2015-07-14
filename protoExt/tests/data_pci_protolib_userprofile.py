# -*- coding: utf-8 -*-

DATA_PCI_protoLib_UserProfile =   {
    'message': '',
    'metaData': {
        'idProperty': 'id',
        'root': 'rows',
        'totalProperty': 'totalCount',
        'messageProperty': 'message',
        'successProperty': 'success'
    },
    'rows': [],
    'protoMeta': {
        'viewIcon': 'icon-1',
        'viewEntity': 'protoLib.UserProfile',
        'gridConfig': {
            'baseFilter': [],
            'initialFilter': [],
            'readOnlyFields': [],
            'initialSort': [],
            'searchFields': ['language', 'userTree', 'userConfig'],
            'filterSetABC': '',
            'sortFields': ['language', 'userTree', 'userConfig'],
            'hideRowNumbers': False,
            'hiddenFields': ['id'],
            'listDisplay': ['__str__']
        },
        'gridSets': {
            'sortersSet': [],
            'filtersSet': [],
            'listDisplaySet': []
        },
        'actions': [{
            'actionParams': [{
                'name': 'User',
                'type': 'string',
                'tooltip': 'UserName',
                'required': True
            }, {
                'name': 'Pwd',
                'type': 'string',
                'tooltip': 'Pwd',
                'required': False
            }, {
                'name': 'EMail',
                'type': 'string',
                'tooltip': 'Email',
                'required': False
            }, {
                'name': 'Team',
                'type': 'string',
                'tooltip': 'Tean',
                'required': False
            }, {
                'name': 'Groups',
                'type': 'string',
                'tooltip': 'gr1,gr2,...',
                'required': False
            }],
            'refreshOnComplete': True,
            'name': 'doAddUser',
            'selectionMode': 'none'
        }],
        'viewCode': 'protoLib.UserProfile',
        'idProperty': 'id',
        'formConfig': {
            'items': [{
                '__ptType': 'fieldset',
                'fsLayout': '2col',
                'items': [{
                    '__ptType': 'formField',
                    'name': 'user'
                }]
            }, {
                '__ptType': 'fieldset',
                'fsLayout': '2col',
                'items': [{
                    '__ptType': 'formField',
                    'name': 'language'
                }, {
                    '__ptType': 'formField',
                    'name': 'userTree'
                }, {
                    '__ptType': 'formField',
                    'name': 'userTeam'
                }]
            }]
        },
        'fieldsAdm': [],
        'detailsConfig': [],
        'metaVersion': '150625',
        'sheetConfig': [],
        'fields': [{
            'fkField': 'userTeam',
            'name': 'userTeam_id',
            'readOnly': True,
            'hidden': True,
            'type': 'foreignid'
        }, {
            'header': 'language',
            'name': 'language',
            'searchable': True,
            'type': 'string',
            'sortable': True
        }, {
            'type': 'proto121',
            'header': 'user',
            'name': 'user',
            'searchable': True,
            'sortable': True,
            'required': True
        }, {
            'readOnly': True,
            'type': 'autofield',
            'header': 'ID',
            'name': 'id',
            'searchable': False,
            'sortable': False,
            'required': False
        }, {
            'header': 'userTree',
            'name': 'userTree',
            'searchable': True,
            'type': 'string',
            'sortable': True
        }, {
            'zoomModel': 'protoLib.UserProfile',
            'cellLink': True,
            'readOnly': True,
            'type': 'string',
            'sortable': True,
            'header': 'User Profile',
            'name': '__str__',
            'flex': 1,
            'fkId': 'id'
        }, {
            'crudType': 'storeOnly',
            'readOnly': True,
            'type': 'text',
            'header': 'userConfig',
            'name': 'userConfig',
            'searchable': True,
            'sortable': False,
            'required': True
        }, {
            'zoomModel': 'protoLib.TeamHierarchy',
            'fkId': 'userTeam_id',
            'type': 'foreigntext',
            'header': 'userTeam',
            'name': 'userTeam',
            'searchable': False,
            'sortable': True
        }],
        'custom': {
            'sortersSet': [],
            'listDisplay': [],
            'listDisplaySet': [],
            'filtersSet': []
        },
        'shortTitle': 'User Profile',
        'businessRules': {},
        'defaultTo': [],
        'description': 'User Profile',
        'exclude': [],
        'fieldsBase': []
    },
    'success': True,
    'permissions': {
        'list': True,
        'change': True,
        'add': True,
        'menu': True,
        'custom': True,
        'delete': True,
        'refallow': True,
        'config': True
    },
    'totalCount': 0
}
