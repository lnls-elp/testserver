use testserverdb;

drop procedure if exists sp_add_power_module;

delimiter $$
use testserverdb$$
create procedure sp_add_power_module
(
	in p_numero_serie					bigint(15)
)

begin
if (select exists (select 1 from ModuloPotencia where numero_serie = p_numero_serie)) then
	select 'Módulo Potência Existe!';
else
insert into ModuloPotencia
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

drop procedure if exists sp_add_log_power_module;

delimiter $$
use testserverdb$$
create procedure sp_add_log_power_module
(
    in p_resultado_teste						        varchar(45),
	in p_numero_serie_power_module       		        bigint(15),
	in p_iload0											double,
	in p_iload1											double,
	in p_iload2											double,
	in p_iload3											double,
	in p_iload4											double,
	in p_iload5											double,
    in p_vload0											double,
	in p_vload1											double,
	in p_vload2											double,
	in p_vload3											double,
	in p_vload4											double,
	in p_vload5											double,
    in p_vdclink0										double,
	in p_vdclink1										double,
	in p_vdclink2										double,
	in p_vdclink3										double,
	in p_vdclink4										double,
	in p_vdclink5										double,
    in p_temperatura0   								double,
	in p_temperatura1 								    double,
	in p_temperatura2 								    double,
	in p_temperatura3 								    double,
	in p_temperatura4 								    double,
	in p_temperatura5 								    double,
	in p_details										text
)

begin
insert into LogModuloPotencia
(
	data,
    resultado_teste,
    numero_serie_modulo_potencia,
	iload0,
	iload1,
	iload2,
	iload3,
	iload4,
	iload5,
    vload0,
	vload1,
	vload2,
	vload3,
	vload4,
	vload5,
    vdclink0,
	vdclink1,
	vdclink2,
	vdclink3,
	vdclink4,
	vdclink5,
    temperatura0,
	temperatura1,
	temperatura2,
	temperatura3,
	temperatura4,
	temperatura5,
	details
)
values
(
    now(),
    p_resultado_teste,
    p_numero_serie_power_module,
	p_iload0,
	p_iload1,
	p_iload2,
	p_iload3,
	p_iload4,
	p_iload5,
    p_vload0,
    p_vload1,
    p_vload2,
    p_vload3,
    p_vload4,
    p_vload5,
    p_vdclink0,
    p_vdclink1,
    p_vdclink2,
    p_vdclink3,
    p_vdclink4,
    p_vdclink5,
    p_temperatura0,
    p_temperatura1,
    p_temperatura2,
    p_temperatura3,
    p_temperatura4,
    p_temperatura5,
	p_details
);
end$$
delimiter ;

drop procedure if exists sp_get_pm_report;

delimiter $$
use testserverdb$$
create procedure sp_get_pm_report()
begin
select
    data, numero_serie_modulo_potencia, iload0, iload1, iload2,
    iload3, iload4, iload5, vload0, vload1, vload2,
    vload3, vload4, vload5, vdclink0, vdclink1, vdclink2,
    vdclink3, vdclink4, vdclink5, temperatura0, temperatura1, temperatura2,
    temperatura3, temperatura4, temperatura5, resultado_teste, details
from LogModuloPotencia;
end$$
delimiter ;
