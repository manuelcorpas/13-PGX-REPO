USE `pgx`

DROP TABLE IF EXISTS `lc`.`00_study_parameters` ;

CREATE TABLE IF NOT EXISTS `lc`.`00_study_parameters` (
	`Study_Parameters_ID`			INT NOT NULL,
	`Variant_Annotation_ID`			INT NOT NULL,
	`Study_Type`				TEXT,
	`Study_Cases`				INT,
	`Study_Controls`			INT,
	`Characteristics`			TEXT,
	`Characteristics_Type`			TEXT,
	`Frequency_In_Cases`			FLOAT,
	`Allele_Of_Frequency_In_Cases`		TEXT,
	`Frequency_In_Controls`			FLOAT,
	`Allele_Of_Frequency_In_Controls`	TEXT,
	`P_Value`				FLOAT,
	`Ratio_Stat_Type`			VARCHAR(20),
	`Ratio_Stat`				FLOAT,
	`Confidence_Interval_Start`		FLOAT,
	`Confidence_Interval_Stop`		FLOAT,
	`Biogeographical_Groups`		VARCHAR(255),
	PRIMARY KEY(Study_Parameters_ID),
	INDEX(Biogeographical_Groups)
	)
ENGINE = MyISAM;
