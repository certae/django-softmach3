
DocumentTreeDefition =  {

    # "viewCode": "rai01ref.Capacity.tree",
    # "viewEntity": "rai01ref.Capacity",
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
        "header": "Parent",
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


    }],

    #  load all dynamic fields in tree definition for formSelector -- need reload after execute 
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


    #  info field is not necesary  
    # }, {
    #     "name": "info",
    #     "type": "text",
    #     "crudType": "storeOnly"


DocServices = {
  "shortTitle": "Services",
  "description": "capacity: services",
  "jsonField": "info",
  "viewEntity": "rai01ref.Capacity",
  "viewCode": "rai01ref.Capacity.61",
  "viewIcon": "icon-1",
  "fields": [
    {
      "fkId": "docType_id",
      "searchable": False,
      "hidden": True,
      "type": "foreigntext",
      "name": "docType",
      "zoomModel": "rai01ref.DocType",
      "prpDefault": "Services",
      "header": "docType",
      "sortable": True,
      "cellLink": True,
      "readOnly": True
    },
    {
      "searchable": True,
      "required": True,
      "type": "string",
      "name": "smUUID",
      "sortable": True,
      "readOnly": True
    },
    {
      "searchable": True,
      "required": True,
      "type": "text",
      "crudType": "storeOnly",
      "name": "info",
      "header": "info",
      "sortable": True,
      "readOnly": True
    },
    {
      "fkId": "refCapacity_id",
      "searchable": False,
      "type": "foreigntext",
      "name": "refCapacity",
      "zoomModel": "rai01ref.Capacity",
      "header": "refCapacity",
      "sortable": True,
      "cellLink": True
    },
    {
      "searchable": True,
      "type": "foreigntext",
      "name": "smOwningTeam",
      "header": "smOwningTeam",
      "sortable": True,
      "cellLink": True,
      "readOnly": True
    },
    {
      "searchable": True,
      "required": True,
      "type": "string",
      "name": "code",
      "header": "code",
      "sortable": True
    },
    {
      "searchable": False,
      "required": False,
      "type": "autofield",
      "name": "id",
      "header": "ID",
      "sortable": False,
      "hidden": True,
      "readOnly": True
    },
    {
      "searchable": True,
      "type": "foreigntext",
      "name": "smOwningUser",
      "header": "smOwningUser",
      "sortable": True,
      "cellLink": True,
      "readOnly": True
    },
    {
      "hidden": True,
      "type": "foreignid",
      "name": "copyFrom_id",
      "header": "copyFrom_id",
      "fkField": "copyFrom",
      "readOnly": True
    },
    {
      "prpDefault": "61",
      "hidden": True,
      "type": "foreignid",
      "name": "docType_id",
      "header": "docType_id",
      "fkField": "docType",
      "readOnly": True
    },
    {
      "searchable": True,
      "type": "string",
      "name": "description",
      "header": "description",
      "sortable": True,
      "vType": "plainText"
    },
    {
      "searchable": True,
      "type": "foreigntext",
      "name": "smCreatedBy",
      "header": "smCreatedBy",
      "sortable": True,
      "cellLink": True,
      "readOnly": True
    },
    {
      "searchable": True,
      "type": "string",
      "name": "smNaturalCode",
      "header": "smNaturalCode",
      "sortable": True,
      "readOnly": True
    },
    {
      "fkId": "id",
      "type": "string",
      "name": "__str__",
      "zoomModel": "rai01ref.Capacity.61",
      "header": "Capacity",
      "sortable": True,
      "flex": 1,
      "cellLink": True,
      "readOnly": True
    },
    {
      "header": "fullPath",
      "type": "string",
      "crudType": "readOnly",
      "name": "fullPath",
      "readOnly": True
    },
    {
      "searchable": True,
      "type": "string",
      "name": "smRegStatus",
      "header": "smRegStatus",
      "sortable": True,
      "readOnly": True
    },
    {
      "searchable": True,
      "type": "string",
      "name": "smWflowStatus",
      "header": "smWflowStatus",
      "sortable": True,
      "readOnly": True
    },
    {
      "searchable": True,
      "type": "datetime",
      "name": "smModifiedOn",
      "header": "smModifiedOn",
      "sortable": True,
      "readOnly": True
    },
    {
      "required": False,
      "prpScale": 0,
      "prpLength": 0,
      "name": "info__responsable",
      "tooltip": "",
      "choices": "",
      "vType": "",
      "prpDefault": "",
      "type": "string",
      "header": "Responsable",
      "crudType": "",
      "readOnly": False
    },
    {
      "searchable": True,
      "type": "foreigntext",
      "name": "smModifiedBy",
      "header": "smModifiedBy",
      "sortable": True,
      "cellLink": True,
      "readOnly": True
    },
    {
      "fkId": "copyFrom_id",
      "searchable": False,
      "type": "foreigntext",
      "name": "copyFrom",
      "zoomModel": "rai01ref.Capacity",
      "header": "copyFrom",
      "sortable": True,
      "cellLink": True
    },
    {
      "required": True,
      "prpScale": 0,
      "prpLength": 0,
      "name": "info__catergory",
      "tooltip": "",
      "choices": "",
      "vType": "",
      "prpDefault": "",
      "type": "string",
      "header": "Catergory",
      "crudType": "",
      "readOnly": False
    },
    {
      "hidden": True,
      "type": "foreignid",
      "name": "refCapacity_id",
      "header": "refCapacity_id",
      "fkField": "refCapacity",
      "readOnly": True
    },
    {
      "searchable": True,
      "type": "datetime",
      "name": "smCreatedOn",
      "header": "smCreatedOn",
      "sortable": True,
      "readOnly": True
    }
  ],
  "actions": [
    {
      "selectionMode": "none",
      "name": "doUpdateMeta",
      "menuText": "doUpdateMeta"
    }
  ],
  "detailsConfig": [
    {
      "conceptDetail": "rai01ref.Capacity",
      "detailName": "capacity.refCapacity",
      "detailField": "refCapacity__pk",
      "menuText": "Capacity.refCapacity",
      "masterField": "pk"
    },
    {
      "conceptDetail": "rai01ref.Capacity",
      "detailName": "capacity.copyFrom",
      "detailField": "copyFrom__pk",
      "menuText": "Capacity.copyFrom",
      "masterField": "pk"
    },
    {
      "conceptDetail": "rai01ref.Artefact",
      "detailName": "artefact.capacity",
      "detailField": "capacity__pk",
      "menuText": "Artefact.capacity",
      "masterField": "pk"
    },
    {
      "conceptDetail": "rai01ref.ArtefactCapacity",
      "detailName": "artefactcapacity.capacity",
      "detailField": "capacity__pk",
      "menuText": "Artefactcapacity.capacity",
      "masterField": "pk"
    },
    {
      "conceptDetail": "rai01ref.ProjectCapacity",
      "detailName": "projectcapacity.capacity",
      "detailField": "capacity__pk",
      "menuText": "Projectcapacity.capacity",
      "masterField": "pk"
    }
  ],
  "gridConfig": {
    "baseFilter": [
      {
        "property": "docType",
        "filterStmt": "=61"
      }
    ],
    "searchFields": [
      "smNaturalCode",
      "smRegStatus",
      "smWflowStatus",
      "code",
      "description",
      "info"
    ],
    "listDisplay": [
      "code",
      "description"
    ]
  },
  "formConfig": {
   "items": [
      {
       "items": [
          {
            "name": "code"
          },
          {
            "fieldLabel": "DocType",
            "xtype": "textfield",
            "name": "docType",
            "readOnly": True
          },
          {
            "prpLength": "1",
            "name": "description"
          },
          {
            "name": "info__catergory"
          },
          {
            "name": "info__responsable"
          }
        ],
        "fsLayout": "2col"
      },
      {
       "items": [
          {
            "name": "refCapacity"
          },
          {
            "name": "copyFrom"
          }
        ],
        "fsLayout": "2col",
        "title": "Document Config"
      },
      {
        "collapsible": True,
        "items": [
          {
            "name": "smOwningTeam"
          },
          {
            "name": "smOwningUser"
          },
          {
            "name": "smCreatedBy"
          },
          {
            "name": "smModifiedOn"
          },
          {
            "name": "smModifiedBy"
          },
          {
            "name": "smCreatedOn"
          }
        ],
        "collapsed": True,
        "title": "Admin",
       "fsLayout": "2col"
      }
    ]
  }
}