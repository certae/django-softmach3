Ext.define('DynamicButtonText', {
    extend : 'Ext.button.Button',

    initComponent : function(){
        this.text = new Date();
        this.renderTo = Ext.getBody();
        this.callParent();
    }
});
