use testserver;

DROP procedure IF EXISTS spAddEquipament;
DELIMITER $$
use testserver$$
CREATE PROCEDURE spAddEquipament (
  IN p_idEquipamento  int,
  IN p_tipo           varchar(45)
)
BEGIN

if (select exists (select 1 from Equipamentos where idEquipamento = p_idEquipamento)) THEN
  select 'Equipament Exists !!';

ELSE

insert into Equipamentos
(
  idEquipamento,
  tipo
)
values
(
  p_idEquipamento,
  p_tipo
);
END IF;
END$$

DELIMITER ;
