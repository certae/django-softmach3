
DocumentTreeDefition =  {

    "viewCode": "rai01ref.Capacity.tree",
    "viewEntity": "rai01ref.Capacity",
    "description": "Capacity",
    "shortTitle": "Capacity Tree",
    "jsonField": "info",

    # Tree ref 
    "pciStyle": "tree",
    "treeRefField": "refCapacity",

    # Form selector 
    "formSelector": "docType_id",

    "fields": [{
        "name": "code",
        "type": "string",
        "searchable": True,
        "required": True,
        "sortable": True
    }, {
        "name": "description",
        "type": "string",
        "searchable": True,
        "sortable": True

    }, {
        "name": "id",
        "type": "autofield",
        "hidden": True,
        "header": "ID",
        "readOnly": True
    }, {
        "name": "__str__",
        "type": "string",
        "zoomModel": "rai01ref.Capacity",
        "flex": 1,
        "fkId": "id",
        "cellLink": True,
        "readOnly": True

    # Static field in model ( docType ) 
    }, {
        "name": "iconCls", 
        "type": "string",
        "crudType": "readOnly",

    # Hierarchy ( Parent : treeRefField )
    }, {
        "name": "refCapacity",
        "type": "foreigntext",
        "zoomModel": "rai01ref.Capacity",
        "fkId": "refCapacity_id",
        "cellLink": True
    }, {
        "name": "refCapacity_id",
        "type": "foreignid",
        "fkField": "refCapacity",
        "readOnly": True


    # Dynamic path hierarchy ( Parent : treeRefField )
    }, {
        "name": "fullPath", 
        "type": "string",
        "crudType": "readOnly",

    # Document Type 
    }, {
        "name": "docType",
        "type": "foreigntext",
        "fkId": "docType_id",
        "zoomFilter": "document, =CAPACITY",
        "zoomModel": "rai01ref.DocType",
        "required": True,
        "cellLink": True
    }, {
        "name": "docType_id",
        "type": "foreignid",
        "fkField": "docType",
        "hidden": True,
        "readOnly": True, 

    # Copy trace 
    }, {
        "name": "copyFrom",
        "type": "foreigntext",
        "zoomModel": "rai01ref.Capacity",
        "fkId": "copyFrom_id",
        "cellLink": True,
        "readOnly": True
    }, {
        "name": "copyFrom_id",
        "type": "foreignid",
        "fkField": "copyFrom",
        "hidden": True,
        "readOnly": True


    #  info field is not necesary  
    # }, {
    #     "name": "info",
    #     "type": "text",
    #     "crudType": "storeOnly"

    }],

    #  need reload after execute 
    "actions": [{
        "name": "doUpdateMeta",
        "menuText": "doUpdateMeta",
        "selectionMode": "none",
        "refreshOnComplete": True
    }],

    "detailsConfig": [{
        "detailName": "artefactcapacity", 
        "menuText": "Artefacts",
        "masterField": "pk",
        "detailField": "capacity__pk",
        "conceptDetail": "rai01ref.ArtefactCapacity",
    }, {
        "detailName": "projectcapacity", 
        "menuText": "Projects",
        "masterField": "pk",
        "detailField": "capacity__pk",
        "conceptDetail": "rai01ref.ProjectCapacity",
    }, {
        "detailName": "copyto", 
        "menuText": "Copies",
        "masterField": "pk",
        "detailField": "copyFrom_id",
        "conceptDetail": "rai01ref.Capacity",
    }]
}