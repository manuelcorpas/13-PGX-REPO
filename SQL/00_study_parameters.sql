USE `pgx`

DROP TABLE IF EXISTS `pgx`.`00_study_parameters` ;

CREATE TABLE IF NOT EXISTS `pgx`.`00_study_parameters` (
	`Study_Parameters_ID`			INT NOT NULL,
	`Variant_Annotation_ID`			INT NOT NULL,
	`Study_Type`				TEXT,
	`Study_Cases`				TEXT,
	`Study_Controls`			TEXT,
	`Characteristics`			TEXT CHARACTER SET utf8,
	`Characteristics_Type`			TEXT,
	`Frequency_In_Cases`			TEXT,
	`Allele_Of_Frequency_In_Cases`		TEXT,
	`Frequency_In_Controls`			TEXT,
	`Allele_Of_Frequency_In_Controls`	TEXT,
	`P_Value`				TEXT,
	`Ratio_Stat_Type`			TEXT,
	`Ratio_Stat`				TEXT,
	`Confidence_Interval_Start`		TEXT,
	`Confidence_Interval_Stop`		TEXT,
	`Biogeographical_Groups`		TEXT CHARACTER SET utf8,
	PRIMARY KEY(Study_Parameters_ID)
	)
ENGINE = MyISAM;
