use testserverdb;

drop procedure if exists sp_add_power_supply;

delimiter $$
use testserverdb$$
create procedure sp_add_power_supply
(
	in p_numero_serie					bigint(15)
)

begin
if (select exists (select 1 from Fonte where numero_serie = p_numero_serie)) then
	select 'Fonte Existe!';
else
insert into Fonte
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

drop procedure if exists sp_add_log_power_supply;

delimiter $$
use testserverdb$$
create procedure sp_add_log_power_supply
(
    in p_id_tipo_teste                  int,
    in p_id_canal_fonte                 int,
    in p_resultado_teste			    varchar(45),
	in p_numero_serie_power_supply      bigint(15),
	in p_result_test_on_off    			varchar(45),
	in p_iout_mais_20_duty_cycle		double,
	in p_iout_menos_20_duty_cycle		double,
	in p_iout0							double,
	in p_iout1							double,
	in p_vout0							double,
    in p_vout1							double,
    in p_vdclink0						double,
	in p_vdclink1						double,
    in p_temperatura0   				double,
	in p_temperatura1 					double,
	in p_details						text
)

begin
insert into LogFonte
(
	data,
    id_tipo_teste_fonte,
    id_canal_fonte,
    resultado_teste,
    numero_serie_fonte,
    resultado_teste_on_off,
    iout_mais_20_duty_cycle,
    iout_menos_20_duty_cycle,
	iout0,
	iout1,
    vout0,
	vout1,
    vdclink0,
	vdclink1,
    temperatura0,
	temperatura1,
	details
)
values
(
    now(),
    p_id_tipo_teste,
    p_id_canal_fonte,
    p_resultado_teste,
    p_numero_serie_power_supply,
    p_result_test_on_off,
    p_iout_mais_20_duty_cycle,
    p_iout_menos_20_duty_cycle,
	p_iout0,
	p_iout1,
    p_vout0,
	p_vout1,
    p_vdclink0,
	p_vdclink1,
    p_temperatura0,
	p_temperatura1,
	p_details
);
end$$
delimiter ;

drop procedure if exists sp_get_ps_report;

delimiter $$
use testserverdb$$
create procedure sp_get_ps_report()
begin
select
    LogFonte.data, LogFonte.numero_serie_fonte, CanalFonte.descricao, TipoTesteFonte.descricao,
    LogFonte.resultado_teste_on_off, LogFonte.iout_mais_20_duty_cycle,
    LogFonte.iout_menos_20_duty_cycle, LogFonte.iout0, LogFonte.iout1, LogFonte.vout0, LogFonte.vout1,
    LogFonte.vdclink0, LogFonte.vdclink1, LogFonte.temperatura0, LogFonte.temperatura1,
    LogFonte.resultado_teste, LogFonte.details
from LogFonte
inner join CanalFonte on LogFonte.id_canal_fonte = CanalFonte.id
inner join TipoTesteFonte on LogFonte.id_tipo_teste_fonte = TipoTesteFonte.id;
end$$
delimiter ;
