use testserverdb;

drop procedure if exists sp_add_dcct;

delimiter $$
use testserverdb$$
create procedure sp_add_dcct
(
		in p_numero_serie					int
)

begin
if (select exists (select 1 from Dcct where numero_serie = p_numero_serie)) then
	select 'DCCT Existe!';
else
insert into Dcct
(
	numero_serie
)
values
(
    p_numero_serie
);
end if;
end$$
delimiter ;

drop procedure if exists sp_add_log_dcct;

delimiter $$
use testserverdb$$
create procedure sp_add_log_dcct
(
        in p_resultado_teste				varchar(45),
		in p_numero_serie_dcct       		int
)

begin
insert into LogDcct
(
	data,
    resultado_teste,
    numero_serie_dcct
)
values
(
    now(),
    p_resultado_teste,
    p_numero_serie_dcct
);
end$$
delimiter ;
