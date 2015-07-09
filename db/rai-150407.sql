CREATE TABLE "rai01ref_doctype" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "document" varchar(11) NOT NULL,
    "dtype" varchar(200) NOT NULL,
    "category" varchar(50),
    "notes" text,
    "description" text,
    UNIQUE ("document", "dtype")
);
;
CREATE TABLE "rai01ref_docattribute" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "docType_id" integer NOT NULL REFERENCES "rai01ref_doctype" ("id"),
    "code" varchar(200) NOT NULL,
    "baseType" varchar(50),
    "prpLength" integer,
    "prpScale" integer,
    "vType" varchar(50),
    "prpDefault" varchar(50),
    "prpChoices" text,
    "isRequired" bool NOT NULL,
    "isSensitive" bool NOT NULL,
    "crudType" varchar(20),
    "description" text,
    UNIQUE ("docType_id", "code")
);
;
CREATE TABLE "rai01ref_domain" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "code" varchar(200) NOT NULL,
    "description" text,
    UNIQUE ("code")
);
;
CREATE TABLE "rai01ref_source" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "code" varchar(200) NOT NULL,
    "reference" varchar(200),
    "notes" text,
    "description" text,
    UNIQUE ("code")
);
;

CREATE TABLE "rai01ref_artefact" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "code" varchar(200) NOT NULL,
    "domain_id" integer NOT NULL REFERENCES "rai01ref_domain" ("id"),
    "dtype" varchar(200) NOT NULL,
    "description" text,
    "info" text NOT NULL,
    "refArtefact_id" integer REFERENCES "rai01ref_artefact" ("id"),
    UNIQUE ("code")
);
;
CREATE TABLE "rai01ref_artefactsource" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "source_id" integer REFERENCES "rai01ref_source" ("id"),
    "artefact_id" integer REFERENCES "rai01ref_artefact" ("id"),
    "notes" text,
    "description" text,
    UNIQUE ("source_id", "artefact_id")
);
;
CREATE TABLE "rai01ref_artefactcomposition" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "containerArt_id" integer NOT NULL REFERENCES "rai01ref_artefact" ("id"),
    "inputArt_id" integer NOT NULL REFERENCES "rai01ref_artefact" ("id"),
    "outputArt_id" integer REFERENCES "rai01ref_artefact" ("id"),
    "condition" text,
    "notes" text,
    "description" text
);
CREATE TABLE "rai01ref_artefactrequirement" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "artefact_id" integer NOT NULL REFERENCES "rai01ref_artefact" ("id"),
    "requirement_id" integer NOT NULL REFERENCES "rai01ref_requirement" ("id"),
    "notes" text,
    "description" text,
    UNIQUE ("artefact_id", "requirement_id")
);
;
CREATE TABLE "rai01ref_artefactcapacity" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "artefact_id" integer NOT NULL REFERENCES "rai01ref_artefact" ("id"),
    "capacity_id" integer NOT NULL REFERENCES "rai01ref_capacity" ("id"),
    "notes" text,
    "description" text,
    UNIQUE ("artefact_id", "capacity_id")
);
;
CREATE TABLE "rai01ref_capacity" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "code" varchar(200) NOT NULL,
    "domain_id" integer NOT NULL REFERENCES "rai01ref_domain" ("id"),
    "dtype" varchar(200) NOT NULL,
    "description" text,
    "info" text NOT NULL,
    "refCapacity_id" integer REFERENCES "rai01ref_capacity" ("id"),
    UNIQUE ("code")
);

CREATE TABLE "rai01ref_projet" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "domain_id" integer NOT NULL REFERENCES "rai01ref_domain" ("id"),
    "code" varchar(200) NOT NULL,
    "notes" text,
    "description" text,
    UNIQUE ("domain_id", "code")
);
;
CREATE TABLE "rai01ref_projectartefact" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "projet_id" integer NOT NULL REFERENCES "rai01ref_projet" ("id"),
    "artefact_id" integer NOT NULL REFERENCES "rai01ref_artefact" ("id"),
    "notes" text,
    "description" text,
    UNIQUE ("artefact_id", "projet_id")
);
;
CREATE TABLE "rai01ref_projectcapacity" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "projet_id" integer NOT NULL REFERENCES "rai01ref_projet" ("id"),
    "capacity_id" integer NOT NULL REFERENCES "rai01ref_capacity" ("id"),
    "notes" text,
    "description" text,
    UNIQUE ("projet_id", "capacity_id")
);
;
CREATE TABLE "rai01ref_projectrequirement" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "projet_id" integer NOT NULL REFERENCES "rai01ref_projet" ("id"),
    "requirement_id" integer NOT NULL REFERENCES "rai01ref_requirement" ("id"),
    "notes" text,
    "description" text,
    UNIQUE ("projet_id", "requirement_id")
);

;
CREATE TABLE "rai01ref_requirement" (
    "id" integer NOT NULL PRIMARY KEY,
    "smOwningUser_id" integer REFERENCES "auth_user" ("id"),
    "smOwningTeam_id" integer REFERENCES "protoLib_teamhierarchy" ("id"),
    "smCreatedBy_id" integer REFERENCES "auth_user" ("id"),
    "smModifiedBy_id" integer REFERENCES "auth_user" ("id"),
    "smRegStatus" varchar(50),
    "smWflowStatus" varchar(50),
    "smCreatedOn" datetime,
    "smModifiedOn" datetime,
    "smUUID" varchar(32),
    "code" varchar(200) NOT NULL,
    "domain_id" integer NOT NULL REFERENCES "rai01ref_domain" ("id"),
    "dtype" varchar(200) NOT NULL,
    "description" text,
    "info" text NOT NULL,
    "refRequirement_id" integer REFERENCES "rai01ref_requirement" ("id"),
    UNIQUE ("code")
);
;
