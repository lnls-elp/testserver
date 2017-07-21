-- MySQL Script generated by MySQL Workbench
-- Fri Jul 21 16:02:38 2017
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema testserverdb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `testserverdb` ;

-- -----------------------------------------------------
-- Schema testserverdb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `testserverdb` DEFAULT CHARACTER SET utf8 ;
USE `testserverdb` ;

-- -----------------------------------------------------
-- Table `testserverdb`.`Hradc`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testserverdb`.`Hradc` ;

CREATE TABLE IF NOT EXISTS `testserverdb`.`Hradc` (
  `numero_serie` BIGINT(15) NOT NULL,
  `variante` VARCHAR(45) NULL,
  `data_instalacao` DATETIME NULL,
  `nome_operador` VARCHAR(120) NULL,
  `resistor_burden` DOUBLE NULL,
  `frequencia_corte` DOUBLE NULL,
  `ordem_filtro` INT NULL,
  `controlador_temperatura` INT NULL,
  `amplificador_burden` VARCHAR(45) NULL,
  `jumper_gnd` INT NULL,
  `jumper_burden` INT NULL,
  `filtro_modo_comum` INT NULL,
  PRIMARY KEY (`numero_serie`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testserverdb`.`Udc`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testserverdb`.`Udc` ;

CREATE TABLE IF NOT EXISTS `testserverdb`.`Udc` (
  `numero_serie` BIGINT(15) NOT NULL,
  PRIMARY KEY (`numero_serie`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testserverdb`.`ModuloPotencia`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testserverdb`.`ModuloPotencia` ;

CREATE TABLE IF NOT EXISTS `testserverdb`.`ModuloPotencia` (
  `numero_serie` BIGINT(15) NOT NULL,
  PRIMARY KEY (`numero_serie`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testserverdb`.`Bastidor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testserverdb`.`Bastidor` ;

CREATE TABLE IF NOT EXISTS `testserverdb`.`Bastidor` (
  `numero_serie` BIGINT(15) NOT NULL,
  PRIMARY KEY (`numero_serie`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testserverdb`.`Fonte`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testserverdb`.`Fonte` ;

CREATE TABLE IF NOT EXISTS `testserverdb`.`Fonte` (
  `numero_serie` BIGINT(15) NOT NULL,
  PRIMARY KEY (`numero_serie`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testserverdb`.`LogBastidor`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testserverdb`.`LogBastidor` ;

CREATE TABLE IF NOT EXISTS `testserverdb`.`LogBastidor` (
  `idLogBastidor` INT NOT NULL AUTO_INCREMENT,
  `data` DATETIME NOT NULL,
  `resultado_teste` VARCHAR(45) NOT NULL,
  `numero_serie_bastidor` BIGINT(15) NOT NULL,
  `iout0` DOUBLE NULL,
  `iout1` DOUBLE NULL,
  `iout2` DOUBLE NULL,
  `iout3` DOUBLE NULL,
  `delta_iout0` DOUBLE NULL,
  `delta_iout1` DOUBLE NULL,
  `delta_iout2` DOUBLE NULL,
  `delta_iout3` DOUBLE NULL,
  `details` TEXT(500) NULL,
  PRIMARY KEY (`idLogBastidor`),
  INDEX `fk_LogBastidor_Bastidor1_idx` (`numero_serie_bastidor` ASC),
  CONSTRAINT `fk_LogBastidor_Bastidor1`
    FOREIGN KEY (`numero_serie_bastidor`)
    REFERENCES `testserverdb`.`Bastidor` (`numero_serie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testserverdb`.`LogFonte`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testserverdb`.`LogFonte` ;

CREATE TABLE IF NOT EXISTS `testserverdb`.`LogFonte` (
  `idLogFonte` INT NOT NULL AUTO_INCREMENT,
  `data` DATETIME NOT NULL,
  `resultado_teste` VARCHAR(45) NOT NULL,
  `numero_serie_fonte` BIGINT(15) NOT NULL,
  PRIMARY KEY (`idLogFonte`),
  INDEX `fk_LogFonte_Fonte1_idx` (`numero_serie_fonte` ASC),
  CONSTRAINT `fk_LogFonte_Fonte1`
    FOREIGN KEY (`numero_serie_fonte`)
    REFERENCES `testserverdb`.`Fonte` (`numero_serie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testserverdb`.`LogHradc`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testserverdb`.`LogHradc` ;

CREATE TABLE IF NOT EXISTS `testserverdb`.`LogHradc` (
  `idLogHradc` INT NOT NULL AUTO_INCREMENT,
  `data` DATETIME NOT NULL,
  `resultado_teste` VARCHAR(45) NOT NULL,
  `numero_serie_hradc` BIGINT(15) NOT NULL,
  PRIMARY KEY (`idLogHradc`),
  INDEX `fk_LogHradc_Hradc_idx` (`numero_serie_hradc` ASC),
  CONSTRAINT `fk_LogHradc_Hradc`
    FOREIGN KEY (`numero_serie_hradc`)
    REFERENCES `testserverdb`.`Hradc` (`numero_serie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testserverdb`.`LogModuloPotencia`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testserverdb`.`LogModuloPotencia` ;

CREATE TABLE IF NOT EXISTS `testserverdb`.`LogModuloPotencia` (
  `idLogModuloPotencia` INT NOT NULL AUTO_INCREMENT,
  `data` DATETIME NOT NULL,
  `resultado_teste` VARCHAR(45) NOT NULL,
  `numero_serie_modulo_potencia` BIGINT(15) NOT NULL,
  `iload0` DOUBLE NULL,
  `iload1` DOUBLE NULL,
  `iload2` DOUBLE NULL,
  `iload3` DOUBLE NULL,
  `iload4` DOUBLE NULL,
  `iload5` DOUBLE NULL,
  `vload0` DOUBLE NULL,
  `vload1` DOUBLE NULL,
  `vload2` DOUBLE NULL,
  `vload3` DOUBLE NULL,
  `vload4` DOUBLE NULL,
  `vload5` DOUBLE NULL,
  `vdclink0` DOUBLE NULL,
  `vdclink1` DOUBLE NULL,
  `vdclink2` DOUBLE NULL,
  `vdclink3` DOUBLE NULL,
  `vdclink4` DOUBLE NULL,
  `vdclink5` DOUBLE NULL,
  `temperatura0` DOUBLE NULL,
  `temperatura1` DOUBLE NULL,
  `temperatura2` DOUBLE NULL,
  `temperatura3` DOUBLE NULL,
  `temperatura4` DOUBLE NULL,
  `temperatura5` DOUBLE NULL,
  `details` TEXT(500) NULL,
  PRIMARY KEY (`idLogModuloPotencia`),
  INDEX `fk_LogModuloPotencia_ModuloPotencia1_idx` (`numero_serie_modulo_potencia` ASC),
  CONSTRAINT `fk_LogModuloPotencia_ModuloPotencia1`
    FOREIGN KEY (`numero_serie_modulo_potencia`)
    REFERENCES `testserverdb`.`ModuloPotencia` (`numero_serie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testserverdb`.`LogUdc`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testserverdb`.`LogUdc` ;

CREATE TABLE IF NOT EXISTS `testserverdb`.`LogUdc` (
  `idLogUdc` INT NOT NULL AUTO_INCREMENT,
  `data` DATETIME NOT NULL,
  `resultado_teste` VARCHAR(45) NOT NULL,
  `numero_serie_udc` BIGINT(15) NOT NULL,
  PRIMARY KEY (`idLogUdc`),
  INDEX `fk_LogUdc_Udc1_idx` (`numero_serie_udc` ASC),
  CONSTRAINT `fk_LogUdc_Udc1`
    FOREIGN KEY (`numero_serie_udc`)
    REFERENCES `testserverdb`.`Udc` (`numero_serie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testserverdb`.`Dcct`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testserverdb`.`Dcct` ;

CREATE TABLE IF NOT EXISTS `testserverdb`.`Dcct` (
  `numero_serie` BIGINT(15) NOT NULL,
  PRIMARY KEY (`numero_serie`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testserverdb`.`LogDcct`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testserverdb`.`LogDcct` ;

CREATE TABLE IF NOT EXISTS `testserverdb`.`LogDcct` (
  `idLogDcct` INT NOT NULL AUTO_INCREMENT,
  `data` DATETIME NOT NULL,
  `resultado_teste` VARCHAR(45) NOT NULL,
  `numero_serie_dcct` BIGINT(15) NOT NULL,
  `iload0` DOUBLE NULL,
  `iload1` DOUBLE NULL,
  `iload2` DOUBLE NULL,
  `iload3` DOUBLE NULL,
  `iload4` DOUBLE NULL,
  `iload5` DOUBLE NULL,
  `iload6` DOUBLE NULL,
  `iload7` DOUBLE NULL,
  `iload8` DOUBLE NULL,
  `iload9` DOUBLE NULL,
  `iload10` DOUBLE NULL,
  `details` TEXT(500) NULL,
  PRIMARY KEY (`idLogDcct`),
  INDEX `fk_LogDcct_Dcct1_idx` (`numero_serie_dcct` ASC),
  CONSTRAINT `fk_LogDcct_Dcct1`
    FOREIGN KEY (`numero_serie_dcct`)
    REFERENCES `testserverdb`.`Dcct` (`numero_serie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `testserverdb`.`CalibHradc`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `testserverdb`.`CalibHradc` ;

CREATE TABLE IF NOT EXISTS `testserverdb`.`CalibHradc` (
  `idCalibHradc` INT NOT NULL AUTO_INCREMENT,
  `data` DATETIME NULL,
  `temperatura_hradc` DOUBLE NULL,
  `temperatura_dmm` DOUBLE NULL,
  `temperatura_fonte` DOUBLE NULL,
  `nome_operador` VARCHAR(120) NULL,
  `ganho_vin` DOUBLE NULL,
  `offset_vin` DOUBLE NULL,
  `ganho_lin` DOUBLE NULL,
  `offset_lin` DOUBLE NULL,
  `vref_p` DOUBLE NULL,
  `vref_n` DOUBLE NULL,
  `gnd` DOUBLE NULL,
  `numero_serie_hradc` BIGINT(15) NOT NULL,
  PRIMARY KEY (`idCalibHradc`),
  INDEX `fk_CalibHradc_Hradc1_idx` (`numero_serie_hradc` ASC),
  CONSTRAINT `fk_CalibHradc_Hradc1`
    FOREIGN KEY (`numero_serie_hradc`)
    REFERENCES `testserverdb`.`Hradc` (`numero_serie`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
