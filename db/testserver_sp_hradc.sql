use testserverdb;

drop procedure if exists sp_add_hradc;

delimiter $$
use testserverdb$$
create procedure sp_add_hradc
(
		in p_numero_serie					int,
        in p_variante						varchar(45),
		in p_data_instalacao				datetime,
		in p_nome_operador					varchar(120),
		in p_resistor_burden				double,
		in p_frequencia_corte				double,
		in p_ordem_filtro					int,
		in p_controlador_temperatura		int,
		in p_amplificador_burden			varchar(45),
		in p_jumper_gnd						int,
		in p_jumper_burden					int,
		in p_filtro_modo_comum				int
)

begin
if (select exists (select 1 from Hradc where numero_serie = p_numero_serie)) then
	select 'HRADC Existe!';
else
insert into Hradc
(
	numero_serie,
    variante,
    data_instalacao,
    nome_operador,
    resistor_burden,
    frequencia_corte,
    ordem_filtro,
    controlador_temperatura,
    amplificador_burden,
    jumper_gnd,
    jumper_burden,
    filtro_modo_comum
)
values
(
    p_numero_serie,
    p_variante,
    p_data_instalacao,
    p_nome_operador,
    p_resistor_burden,
    p_frequencia_corte,
    p_ordem_filtro,
    p_controlador_temperatura,
    p_amplificador_burden,
    p_jumper_gnd,
    p_jumper_burden,
    p_filtro_modo_comum
);
end if;
end$$
delimiter ;

drop procedure if exists sp_add_log_hradc;

delimiter $$
use testserverdb$$
create procedure sp_add_log_hradc
(
        in p_resultado_teste				varchar(45),
		in p_numero_serie_hradc       		int
)

begin
insert into LogHradc
(
	data,
    resultado_teste,
    numero_serie_hradc
)
values
(
    now(),
    p_resultado_teste,
    p_numero_serie_hradc
);
end$$
delimiter ;

drop procedure if exists sp_add_calib_hradc;

delimiter $$
use testserverdb$$
create procedure sp_add_calib_hradc
(
        in p_temperatura_hradc				double,
		in p_temperatura_dmm         		double,
        in p_temperatura_fonte              double,
        in p_nome_operador                  varchar(120),
        in p_ganho_vin                      double,
        in p_offset_vin                     double,
        in p_ganho_lin                      double,
        in p_offset_lin                     double,
        in p_vref_p                         double,
        in p_vref_n                         double,
        in p_gnd                            double,
        in p_numero_serie_hradc             int
)

begin
insert into CalibHradc
(
    data,
    temperatura_hradc,
    temperatura_dmm,
    temperatura_fonte,
    nome_operador,
    ganho_vin,
    offset_vin,
    ganho_lin,
    offset_lin,
    vref_p,
    vref_n,
    gnd,
    numero_serie_hradc
)
values
(
    now(),
    p_temperatura_hradc,
    p_temperatura_dmm,
    p_temperatura_fonte,
    p_nome_operador,
    p_ganho_vin,
    p_offset_vin,
    p_ganho_lin,
    p_offset_lin,
    p_vref_p,
    p_vref_n,
    p_gnd,
    p_numero_serie_hradc
);
end$$
delimiter ;
