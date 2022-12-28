USE `pgx`

DROP TABLE IF EXISTS `pgx`.`01_var_drug_ann` ;

CREATE TABLE IF NOT EXISTS `pgx`.`01_var_drug_ann` (
	`Variant_Annotation_ID`			INT NOT NULL,
	`Variant_Haplotypes`			TEXT,
	`Gene`					VARCHAR (50),
	`Drug`					TEXT,
	`PMID`			     		INT,
	`Phenotype_Category`			TEXT,
	`Significance`				TEXT,
	`Notes`					TEXT,
	`Sentence`				TEXT,
	`Alleles`				TEXT,
	`Specialty_Population`			TEXT,
	PRIMARY KEY(Variant_Annotation_ID)
	)
ENGINE = MyISAM;
