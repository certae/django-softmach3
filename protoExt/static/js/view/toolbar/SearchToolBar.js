/*
 * Text Search + QBE toolbar 
 * 
 */

Ext.define('Softmachine.view.toolbar.SearchToolBar', {
    extend : 'Ext.toolbar.Toolbar',
    alias : 'widget.searchToolBar',

    /**
     * @private MetaData initialization
     */
    myMeta : null,
    protoEnable : true, 
    /**
     * @private Component initialization override: ToolBar setup
     */
    initComponent : function(){

        var me = this;
        var myMeta = this.myMeta;

        // Load Data button
        var searchBtn = new Ext.button.Button({
            tooltip : _SM.__language.Tooltip_Filter_Grid_Button,
            iconCls : 'icon-filter',
            handler : onClickSearchBtn
        });

        var QBEBtn = new Ext.button.Button({
            tooltip: _SM.__language.Text_Toolbar_Advanced_Filter,
            iconCls: 'icon-filterqbe',
            handler: onClickViewQBE, 
            scope : me 
        });

        var clearBtn = new Ext.button.Button({
            tooltip : _SM.__language.Text_Toolbar_Remove_Filters,
            iconCls : 'icon-filterdelete',
            handler : onClickClearFilter
        });

        // Criteria
        var searchCr = new Ext.form.TextField({
            emptyText : _SM.__language.Text_Toolbar_Search_Field,
            enableKeyEvents : true,
            width : 200,
            listeners : {
                keydown : function(me, e){
                    if (e.getKey() == e.ENTER) {
                        onClickSearchBtn(searchBtn);
                    }
                }
            }
        });



        Ext.apply(me, {
            border : false,
            disabled : !me.protoEnable,
            items : [
                searchCr,
                searchBtn,
                QBEBtn,
                clearBtn
            ]
        });

        // me.addEvents('qbeLoadData');
        me.callParent();

        // Inicializa Combos
        clearCombos();

        function onClickSearchBtn(btn){
            var sFilter = searchCr.getValue();
            var sTitle = '" ' + searchCr.getValue() + ' "';

            me.fireEvent('qbeLoadData', me, [
                {
                    'property' : '_allCols',
                    'filterStmt' : sFilter
                }
            ], sTitle);
        }

        // BG
        function onClickClearFilter(item){
            // resetea los fitros tambien
            clearCombos();
            me.fireEvent('qbeLoadData', me, [], '', []);
        }

        function onClickViewQBE(item){

            var qbeParams = [ "name", "tooltip", "fieldLabel" ]
            var qbeField, pAction = {};
            
            pAction.viewCode = me.myMeta.viewCode; 
            pAction.actionName = 'Qbe search' 
            pAction.parameters = []


            for ( var ix in me.myMeta.fields) {
                var vFld = me.myMeta.fields[ix];

                if ( vFld.QbeField || vFld.searchable  ) {
                    qbeField = _SM.clone( vFld, 0, [], qbeParams )
                    qbeField.type = 'string' 

                    if ( vFld.type in _SM.objConv(['string', 'text', 'combo', 'foreigntext'])) {
                        qbeField.tooltip = 'wildchar selection *';                        
                    } else if ( vFld.type in _SM.objConv(['int', 'decimal', 'money'])) {
                        qbeField.tooltip = 'wildchar selection *';                        
                    }
                    pAction.parameters.push( qbeField ) 
                }

            } 

            var myOptions = {
                scope: me,
                acceptFn: function(parameters) {
                    var a = 1;
                    // this.doAction(me, pGrid.viewCode, {}, selectedKeys, parameters, detKeys);
                }

            };
            
            var myWin = Ext.create('ProtoUL.ux.ParameterWin', {
                title: pAction.actionName,
                viewCode : pAction.viewCode,
                parameters: pAction.parameters,
                options: myOptions
            });

            myWin.show();

        }

        // BG
        function clearCombos(){
            // comboCols.setValue('');
            // comboOp.setValue('');
            searchCr.setValue('');
        }

    }, 



});
