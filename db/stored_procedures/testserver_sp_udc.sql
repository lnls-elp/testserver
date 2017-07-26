use testserverdb;

drop procedure if exists sp_add_udc;

delimiter $$
use testserverdb$$
create procedure sp_add_udc
(
	in p_numero_serie					bigint(15)
)

begin
if (select exists (select 1 from Udc where numero_serie = p_numero_serie)) then
	select 'UDC Existe!';
else
insert into Udc
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

drop procedure if exists sp_add_log_udc;

delimiter $$
use testserverdb$$
create procedure sp_add_log_udc
(
    in p_resultado_teste						        varchar(45),
	in p_numero_serie_udc       		                bigint(15),
	in p_details										text
)

begin
insert into LogUdc
(
	data,
    resultado_teste,
    numero_serie_udc,
	details
)
values
(
    now(),
    p_resultado_teste,
    p_numero_serie_udc,
	p_details
);
end$$
delimiter ;
