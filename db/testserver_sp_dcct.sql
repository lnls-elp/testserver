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
    in p_resultado_teste						varchar(45),
		in p_numero_serie_dcct       		int,
		in p_iload0											double,
		in p_iload1											double,
		in p_iload2											double,
		in p_iload3											double,
		in p_iload4											double,
		in p_iload5											double,
		in p_iload6											double,
		in p_iload7											double,
		in p_iload8											double,
		in p_iload9											double,
		in p_iload10										double,
		in p_details										text
)

begin
insert into LogDcct
(
		data,
    resultado_teste,
    numero_serie_dcct,
		iload0,
		iload1,
		iload2,
		iload3,
		iload4,
		iload5,
		iload6,
		iload7,
		iload8,
		iload9,
		iload10,
		details
)
values
(
    now(),
    p_resultado_teste,
    p_numero_serie_dcct,
		p_iload0,
		p_iload1,
		p_iload2,
		p_iload3,
		p_iload4,
		p_iload5,
		p_iload6,
		p_iload7,
		p_iload8,
		p_iload9,
		p_iload10,
		p_details
);
end$$
delimiter ;
