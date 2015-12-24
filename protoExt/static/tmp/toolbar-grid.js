Ext.onReady(function() {

    Ext.define('Company', {
        extend: 'Ext.data.Model',
        fields: ['name', 'day1', 'day2', 'day3', 'day4', 'day5', 'day6', 'day7', 'type']
    });

    Ext.define('Company2', {
        extend: 'Ext.data.Model',
        fields: ['altday', 'altoffshift', 'altstarttime', 'altendtime', 'altcrossesmidnight', 'altflexstat', 'altflexbefore', 'altflexafter', 'altmealduration', 'altactivity']
    });
    var myData = [
        ['Off Shift', false, false, false, false, false, true, true, 'checkbox'],
        ['Start Time', '08:00', '08:00', '08:00', '08:00', '08:00', '00:00', '00:00', 'time'],
        ['End Time', '16:00', '16:00', '16:00', '16:00', '16:00', '00:00', '00:00', 'time'],
        ['Crosses Midnight', false, false, false, false, false, false, false, 'checkbox'],
        ['Flex Status', false, false, false, false, false, false, false, 'checkbox'],
        ['Flex Before', '03:00', '17:32', '12:33', '00:00', '17:32', '12:33', '00:00', 'time'],
        ['Flex After', '03:00', '17:32', '12:33', '00:00', '17:32', '12:33', '00:00', 'time'],
        ['Meal Duration', '03:00', '17:32', '12:33', '00:00', '17:32', '12:33', '00:00', 'time'],
        ['Activity', '', '', '', '', '', '', '', 'combo']
    ];

    var myData2 = [
        ['Sunday', false, '08:00', '16:00', false, false, '00:00', '00:00', '00:00', ''],
        ['Monday', false, '08:00', '16:00', false, false, '00:00', '00:00', '00:00', ''],
        ['Tuesday', false, '08:00', '16:00', false, false, '00:00', '00:00', '00:00', ''],
        ['Wednesday', false, '08:00', '16:00', false, false, '00:00', '00:00', '00:00', ''],
        ['Thursday', false, '08:00', '16:00', false, false, '00:00', '00:00', '00:00', ''],
        ['Friday', false, '08:00', '16:00', false, false, '00:00', '00:00', '00:00', ''],
        ['Saturday', false, '08:00', '16:00', false, false, '00:00', '00:00', '00:00', ''], ];

    specialRender = function(val, meta, rec) {
        var type = rec.get('type');
        var result = val;
        if (type == 'time' && Ext.isDate(val)) {
            result = Ext.util.Format.date(val, 'H:i');
        } else if (type == 'checkbox') {
            return new Ext.ux.CheckColumn().renderer(result);
        } else if (type == 'combo') {
            return new Ext.form.ComboBox().renderer(result);
        } else if (type == 'boolean' && Ext.isBoolean(val)) {
            if (val) {
                result = 'Yes'
            } else {
                result = 'No'
            };
        }
        return Ext.util.Format.htmlEncode(result);
    };
    getCellEditor = function(record, column) {
        return myeditors[record.get('type')];
    };
    var myeditors = {
        'date': Ext.create('Ext.grid.CellEditor', {
            field: Ext.create('Ext.form.field.Date', {
                selectOnFocus: true
            })
        }),
        'checkbox': Ext.create('Ext.grid.CellEditor', {
            field: {
                xtype: 'checkbox',
                style: 'display: inline-block;margin-left: 0.5em;margin-right: 2em;line-height: 2em;',
                listeners: {
                    focus: function(e, The, eOpts) {
                        if (this.getValue == true) {
                            this.setValue(false);
                        } else this.setValue(true);

                    }
                }
            }

        }),
        'string': Ext.create('Ext.grid.CellEditor', {
            field: Ext.create('Ext.form.field.Text', {
                selectOnFocus: true
            })
        }),
        'number': Ext.create('Ext.grid.CellEditor', {
            field: Ext.create('Ext.form.field.Number', {
                selectOnFocus: true
            })
        }),
        'int': Ext.create('Ext.grid.CellEditor', {
            field: Ext.create('Ext.form.field.Number', {
                selectOnFocus: true
            })
        }),
        'time': Ext.create('Ext.grid.CellEditor', {
            field: Ext.create('Ext.form.TimeField', {
                selectOnFocus: true,
                format: 'H:i'
            })
        }),
        'combo': Ext.create('Ext.grid.CellEditor', {
            field: Ext.create('Ext.form.field.ComboBox', {
                editable: false,
                store: [
                    ["", '---'],
                    ['Contractual', 'Contractual'],
                    ['Giveback', 'Giveback'],
                    ['Court', 'Court'],
                    ['Detail', 'Detail'],
                    ['Promotion', 'Promotion'],
                    ['Slippage', 'Slippage'],
                    ['Tour Change', 'Tour Change'],
                    ['Training', 'Training']
                ]
            })
        })
    };

    var cellEditing = Ext.create('Ext.grid.plugin.CellEditing', {
        clicksToEdit: 1
    });
    // create the data store
    var store = Ext.create('Ext.data.ArrayStore', {
        model: 'Company',
        data: myData
    });

    var usersForFiddle = [
        ['Jeroen', 'De Ryck', '458111', '1485007', false, 'COMPUTER SPECIALIST', 'Active'],
        ['John', 'McClane', '479435', '90011', true, 'Detective', 'Active']


    ];


    var storeForFiddle = Ext.create('Ext.data.ArrayStore', {
        data: usersForFiddle,
        storeId: 'fiddleStore',
        fields: ['sorFirstName', 'sorLastName', 'sorCitytimeId', 'sorPmsRef', 'sorMultipleShift', 'sorRankTitle', 'sorStatus']
    });



    var sorDetailsTab = Ext.create('Ext.panel.Panel', {
        title: 'Details',
        id: 'sorDetailsTab',
        items: [{
            xtype: 'gridpanel',
            id: 'sorDetailsGrid',
            store: store,
            stateful: true,
            stateId: 'stateGrid',
            disableSelection: true,
            hidden: true,
            trackMouseOver: false,
            selModel: 'cellmodel',
            plugins: [cellEditing],
            listeners: {
                cellclick: function(e, td, cellIndex, record, tr, rowIndex, e, eOpts) {}
            },
            columns: [{
                text: 'Days',
                flex: 3,
                sortable: false,
                render: specialRender,
                dataIndex: 'name'
            }, {
                text: 'Sunday',
                flex: 1,
                sortable: false,
                renderer: Ext.Function.bind(this.specialRender, this),
                getEditor: Ext.Function.bind(this.getCellEditor, this),
                dataIndex: 'day1'
            }, {
                text: 'Monday',
                flex: 1,
                sortable: false,
                renderer: Ext.Function.bind(this.specialRender, this),
                getEditor: Ext.Function.bind(this.getCellEditor, this),
                dataIndex: 'day2'
            }, {
                text: 'Tuesday',
                flex: 1,
                sortable: false,
                renderer: Ext.Function.bind(this.specialRender, this),
                getEditor: Ext.Function.bind(this.getCellEditor, this),
                dataIndex: 'day3'
            }, {
                text: 'Wednesday',
                flex: 1,
                sortable: false,
                renderer: Ext.Function.bind(this.specialRender, this),
                getEditor: Ext.Function.bind(this.getCellEditor, this),
                dataIndex: 'day4'
            }, {
                text: 'Thursday',
                flex: 1,
                sortable: false,
                renderer: Ext.Function.bind(this.specialRender, this),
                getEditor: Ext.Function.bind(this.getCellEditor, this),
                dataIndex: 'day5'
            }, {
                text: 'Friday',
                flex: 1,
                sortable: false,
                renderer: Ext.Function.bind(this.specialRender, this),
                getEditor: Ext.Function.bind(this.getCellEditor, this),
                dataIndex: 'day6'
            }, {
                text: 'Saturday',
                flex: 1,
                sortable: false,
                renderer: Ext.Function.bind(this.specialRender, this),
                getEditor: Ext.Function.bind(this.getCellEditor, this),
                dataIndex: 'day7'
            }],
            viewConfig: {
                stripeRows: true
            }
        }]

    });

    var sorInfoTab = Ext.create('Ext.panel.Panel', {
        title: 'Additional Info',
        id: 'sorInfoTab'

    });

    var sorReqHistoryTab = Ext.create('Ext.panel.Panel', {
        title: 'Request History',
        id: 'sorReqHistoryTab'

    });

    var sorQueryMode = 0;



    Ext.create('Ext.panel.Panel', {
        renderTo: Ext.getBody(),
        activeTab: 0,
        title: 'Schedule Override',
        dockedItems: [{
            dock: 'top',
            xtype: 'toolbar',
            items: [{
                xtype: 'radiogroup',
                columns: 2,
                vertical: true,
                layout: 'hbox',
                defaults: {
                    name: 'activeStatus'
                },
                items: [{
                    inputValue: 'active',
                    boxLabel: 'Active',
                    checked: true
                }, {
                    inputValue: 'inactive',
                    boxLabel: 'Inactive'
                }

                ]

            }, {
                xtype: 'combobox',
                store: Ext.create('Ext.data.Store', {
                    fields: ['searchOption'],
                    autoLoad: true,
                    data: [{
                        searchOption: 'Name (Last, First)'
                    }, {
                        searchOption: 'PMS Ref #'
                    }, {
                        searchOption: 'CityTime ID'
                    }

                    ]
                }),
                value: 'Name (Last, First)',
                displayField: 'searchOption',
                editable: false,
                listeners: {
                    select: function(cmb, record, eOpts) {
                        var selectedRecord = cmb.getValue();
                        if (selectedRecord == "Name (Last, First)") {
                            Ext.getCmp('sorFirstNameSearch').show();
                            Ext.getCmp('sorLastNameSearch').show();
                            Ext.getCmp('sorPmsRefSearch').hide();
                            Ext.getCmp('sorCityTimeIdSearch').hide();
                            sorQueryMode = 0;
                        } else if (selectedRecord == "PMS Ref #") {
                            Ext.getCmp('sorFirstNameSearch').hide();
                            Ext.getCmp('sorLastNameSearch').hide();
                            Ext.getCmp('sorPmsRefSearch').show();
                            Ext.getCmp('sorCityTimeIdSearch').hide();
                            sorQueryMode = 1;
                        } else if (selectedRecord == "CityTime ID") {
                            Ext.getCmp('sorFirstNameSearch').hide();
                            Ext.getCmp('sorLastNameSearch').hide();
                            Ext.getCmp('sorPmsRefSearch').hide();
                            Ext.getCmp('sorCityTimeIdSearch').show();
                            sorQueryMode = 2;
                        }



                    }
                }
            }, {
                xtype: 'textfield',
                emptyText: 'Last',
                id: 'sorLastNameSearch',
                enableKeyEvents: true,
                listeners: {
                    specialkey: function(field, e) {
                        if (e.getKey() == e.ENTER) {
                            var searchbutton = Ext.getCmp('sorSearchEmployeeBtn');
                            searchbutton.fireEvent('click', searchbutton);
                        }
                    }
                }

            }, {
                xtype: 'textfield',
                emptyText: 'First',
                id: 'sorFirstNameSearch',
                enableKeyEvents: true,
                listeners: {
                    specialkey: function(field, e) {
                        if (e.getKey() == e.ENTER) {
                            var searchbutton = Ext.getCmp('sorSearchEmployeeBtn');
                            searchbutton.fireEvent('click', searchbutton);
                        }
                    }
                }

            }, {
                xtype: 'textfield',
                emptyText: 'PMS Ref',
                id: 'sorPmsRefSearch',
                hidden: true,
                enableKeyEvents: true,
                listeners: {
                    specialkey: function(field, e) {
                        if (e.getKey() == e.ENTER) {
                            var searchbutton = Ext.getCmp('sorSearchEmployeeBtn');
                            searchbutton.fireEvent('click', searchbutton);
                        }
                    }
                }
            }, {
                xtype: 'textfield',
                emptyText: 'CityTime ID',
                id: 'sorCityTimeIdSearch',
                hidden: true,
                enableKeyEvents: true,
                listeners: {
                    specialkey: function(field, e) {
                        if (e.getKey() == e.ENTER) {
                            var searchbutton = Ext.getCmp('sorSearchEmployeeBtn');
                            searchbutton.fireEvent('click', searchbutton);
                        }
                    }
                }
            }, {
                xtype: 'button',
                iconCls: 'x-form-search-trigger',
                id: 'sorSearchEmployeeBtn',
                listeners: {
                    click: function() {
                        var store = Ext.data.StoreManager.lookup('fiddleStore');
                        if (sorQueryMode == 0) {
                            var match = store.findBy(function(record, id) {
                                //if(record.get('sorLastName')==Ext.getCmp('sorLastNameSearch').getValue() && record.get('sorFirstName')==Ext.getCmp('sorFirstNameSearch').getValue()) {
                                var gridForSearch = Ext.getCmp('sorSearchGrid');
                                store.filterBy(function(record, id) {
                                    // 'name' is 'Bart Simpson Something'

                                    // case-insensitive match of 'simpson' in the name
                                    return (record.get('sorFirstName').toLowerCase().indexOf(Ext.getCmp('sorFirstNameSearch').getValue()) > -1 && record.get('sorLastName').toLowerCase().indexOf(Ext.getCmp('sorLastNameSearch').getValue()) > -1);
                                });

                                //gridForSearch.filter([{property: "sorLastName", anyMatch: true, value: Ext.getCmp('sorLastNameSearch').getValue()},{property: "sorFirstName", anyMatch: true, value: Ext.getCmp('sorFirstNameSearch').getValue()}])
                                //  gridForSearch.filter('sorLastName',Ext.getCmp('sorLastNameSearch').getValue());
                                gridForSearch.show();
                                //}
                            });

                        } else if (sorQueryMode == 1) {
                            alert('1');
                        } else {
                            alert('2');
                        }
                    }
                }
            }, {
                xtype: 'label',
                text: 'Week of:'
            }, {
                xtype: 'datefield'
            }, {
                xtype: 'button',
                text: 'Go',
                style: {
                    borderColor: 'darkblue'
                }
            }




            ]
        },


        {
            xtype: 'gridpanel',
            store: storeForFiddle,
            id: 'sorSearchGrid',
            stateId: 'stateGrid',
            emptyText: 'No employees found with those criteria',
            columns: [{
                text: 'Last Name',
                dataIndex: 'sorLastName',
                flex: 1
            }, {
                text: 'First Name',
                dataIndex: 'sorFirstName',
                flex: 1
            }, {
                text: 'Ref #',
                dataIndex: 'sorPmsRef',
                flex: 1
            }, {
                text: 'Rank/Title',
                dataIndex: 'sorRankTitle',
                flex: 2
            }],
            width: 600,
            hidden: true,
            listeners: {
                itemclick: function(dv, record, item, index, e) {
                    Ext.getCmp('sorDisplayName').setValue(record.get('sorFirstName') + " " + record.get('sorLastName'));
                    Ext.getCmp('sorDisplayCTID').setValue(record.get('sorCitytimeId'));
                    Ext.getCmp('sorDisplayRankTitle').setValue(record.get('sorRankTitle'));
                    Ext.getCmp('sorDisplayStatus').setValue(record.get('sorStatus'));

                    Ext.getCmp('sorDisplayToolbar').show();
                    this.hide();
                    Ext.getCmp('sorDetailsGrid').show();
                }
            },
            title: 'Please select an employee'
        }, {
            xtype: 'toolbar',
            dock: 'top',
            hidden: true,
            id: 'sorDisplayToolbar',
            defaults: {
                labelStyle: 'font-weight : bold; color : darkblue',
                labelWidth: 80,
                margin: '0 20 0 0'
            },
            items: [{
                xtype: 'displayfield',
                fieldLabel: 'Dates',
                id: 'sorDisplayDates',
                hidden: true
            }, {
                xtype: 'displayfield',
                id: 'sorDisplayName',
                fieldLabel: 'Name:'
            }, {
                xtype: 'displayfield',
                id: 'sorDisplayCTID',
                fieldLabel: 'CityTime ID:'
            }, {
                xtype: 'displayfield',
                id: 'sorDisplayRankTitle',
                fieldLabel: 'Rank/Title:'
            }, {
                xtype: 'displayfield',
                id: 'sorDisplayReqID',
                fieldLabel: 'Req ID:'
            }, {
                xtype: 'displayfield',
                id: 'sorDisplayStatus',
                fieldLabel: 'Status:'
            }]

        }


        ],
        items: [{
            xtype: 'tabpanel',
            items: [sorDetailsTab, sorInfoTab, sorReqHistoryTab]
        }]
    });

});