Ext.define('Softmachine.view.smform.ProtoZoomController', {
    extend: 'Ext.app.ViewController',
    alias: 'controller.protoZoomController',

    onNavFilterFieldChange: function(field, value) {
        var me = this,
            tree = me.getReferences().tree;

        if (value) {
            me.preFilterSelection = me.getViewModel().get('selectedView');
            me.rendererRegExp = new RegExp( '(' + value + ')', "gi");
            field.getTrigger('clear').show();
            me.filterStore(value);
        } else {
            me.rendererRegExp = null;
            tree.store.clearFilter();
            field.getTrigger('clear').hide();

            // Ensure selection is still selected.
            // It may have been evicted by the filter
            if (me.preFilterSelection) {
                    tree.ensureVisible(me.preFilterSelection, {
                    select: true
                });
            }
        }
    },

    onNavFilterClearTriggerClick: function() {
        this.getReferences().navtreeFilter.setValue();
    },

    onNavFilterSearchTriggerClick: function() {
        var field = this.getReferences().navtreeFilter;

        this.onNavFilterFieldChange(field, field.getValue());
    },


});
