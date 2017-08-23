use testserverdb;

drop procedure if exists sp_add_rack;

delimiter $$
use testserverdb$$
create procedure sp_add_rack
(
	in p_numero_serie					bigint(15)
)

begin
if (select exists (select 1 from Bastidor where numero_serie = p_numero_serie)) then
	select 'Bastidor Existe!';
else
insert into Bastidor
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

drop procedure if exists sp_add_log_rack;

delimiter $$
use testserverdb$$
create procedure sp_add_log_rack
(
    in p_resultado_teste						        varchar(45),
	in p_numero_serie_rack       		                bigint(15),
	in p_iout0											double,
	in p_iout1											double,
	in p_iout2											double,
	in p_iout3											double,
    in p_delta_iout0    								double,
	in p_delta_iout1      								double,
	in p_delta_iout2  		      						double,
	in p_delta_iout3  				    				double,
	in p_details										text
)

begin
insert into LogBastidor
(
	data,
    resultado_teste,
    numero_serie_bastidor,
	iout0,
	iout1,
	iout2,
	iout3,
    delta_iout0,
    delta_iout1,
    delta_iout2,
    delta_iout3,
	details
)
values
(
    now(),
    p_resultado_teste,
    p_numero_serie_rack,
	p_iout0,
	p_iout1,
	p_iout2,
	p_iout3,
    p_delta_iout0,
	p_delta_iout1,
	p_delta_iout2,
	p_delta_iout3,
	p_details
);
end$$
delimiter ;

drop procedure if exists sp_get_rack_report;

delimiter $$
use testserverdb$$
create procedure sp_get_rack_report()
begin
select
    data, numero_serie_bastidor, iout0, iout1, iout2, iout3,
    delta_iout0, delta_iout1, delta_iout2, delta_iout3,
    details, resultado_teste
from LogBastidor;
end$$
delimiter ;
