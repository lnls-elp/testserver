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
    in p_resultado_teste			    varchar(45),
	in p_numero_serie_udc       	    bigint(15),
    in p_io_expander0                   varchar(45),
    in p_io_expander1                   varchar(45),
    in p_leds                           varchar(45),
    in p_buzzer                         varchar(45),
    in p_eeprom                         varchar(45),
    in p_flash                          varchar(45),
    in p_ram                            varchar(45),
    in p_rtc_communication              varchar(45),
    in p_rtc_interrupt                  varchar(45),
    in p_sensor_temperatura_com         varchar(45),
    in p_sensor_temperatura_val         varchar(45),
    in p_control_aliment_plano_isolado  varchar(45),
    in p_rs4850                         varchar(45),
    in p_rs4851                         varchar(45),
    in p_rs4852                         varchar(45),
    in p_sdcard_inserido                varchar(45),
    in p_sdcard_communication           varchar(45),
    in p_ethernet_inicializacao         varchar(45),
    in p_ethernet_ping                  varchar(45),
    in p_loopback                       text,
	in p_details					    text
)

begin
insert into LogUdc
(
	data,
    resultado_teste,
    numero_serie_udc,
    io_expander0,
    io_expander1,
    leds,
    buzzer,
    eeprom,
    flash,
    ram,
    rtc_communication,
    rtc_interrupt,
    sensor_temperatura_com,
    sensor_temperatura_val,
    control_aliment_plano_isolado,
    rs4850,
    rs4851,
    rs4852,
    sdcard_inserido,
    sdcard_communication,
    ethernet_inicializacao,
    ethernet_ping,
    loopback,
	details
)
values
(
    now(),
    p_resultado_teste,
    p_numero_serie_udc,
    p_io_expander0,
    p_io_expander1,
    p_leds,
    p_buzzer,
    p_eeprom,
    p_flash,
    p_ram,
    p_rtc_communication,
    p_rtc_interrupt,
    p_sensor_temperatura_com,
    p_sensor_temperatura_val,
    p_control_aliment_plano_isolado,
    p_rs4850,
    p_rs4851,
    p_rs4852,
    p_sdcard_inserido,
    p_sdcard_communication,
    p_ethernet_inicializacao,
    p_ethernet_ping,
    p_loopback,
    p_details
);
end$$
delimiter ;
