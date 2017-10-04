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
    in p_io_expander                    varchar(45),
    in p_leds                           varchar(45),
    in p_buzzer                         varchar(45),
    in p_eeprom                         varchar(45),
    in p_flash                          varchar(45),
    in p_ram                            varchar(45),
    in p_rtc                            varchar(45),
    in p_sensor_temperatura             varchar(45),
    in p_control_aliment_plano_isolado  varchar(45),
    in p_uart                           varchar(45),
    in p_sdcard                         varchar(45),
    in p_ethernet_inicializacao         varchar(45),
    in p_ethernet_ping                  varchar(45),
    in p_adc_ch_1                       varchar(45),
    in p_adc_ch_2                       varchar(45),
    in p_adc_ch_3                       varchar(45),
    in p_adc_ch_4                       varchar(45),
    in p_adc_ch_5                       varchar(45),
    in p_adc_ch_6                       varchar(45),
    in p_adc_ch_7                       varchar(45),
    in p_adc_ch_8                       varchar(45),
    in p_loopback                       text,
	in p_details					    text
)

begin
insert into LogUdc
(
	data,
    resultado_teste,
    numero_serie_udc,
    io_expander,
    leds,
    buzzer,
    eeprom,
    flash,
    ram,
    rtc,
    sensor_temperatura,
    control_aliment_plano_isolado,
    uart,
    sdcard,
    ethernet_inicializacao,
    ethernet_ping,
    adc_ch_1,
    adc_ch_2,
    adc_ch_3,
    adc_ch_4,
    adc_ch_5,
    adc_ch_6,
    adc_ch_7,
    adc_ch_8,
    loopback,
	details
)
values
(
    now(),
    p_resultado_teste,
    p_numero_serie_udc,
    p_io_expander,
    p_leds,
    p_buzzer,
    p_eeprom,
    p_flash,
    p_ram,
    p_rtc,
    p_sensor_temperatura,
    p_control_aliment_plano_isolado,
    p_uart,
    p_sdcard,
    p_ethernet_inicializacao,
    p_ethernet_ping,
    p_adc_ch_1,
    p_adc_ch_2,
    p_adc_ch_3,
    p_adc_ch_4,
    p_adc_ch_5,
    p_adc_ch_6,
    p_adc_ch_7,
    p_adc_ch_8,
    p_loopback,
	p_details
);
end$$
delimiter ;

drop procedure if exists sp_get_udc_report;

delimiter $$
use testserverdb$$
create procedure sp_get_udc_report()
begin
select data, resultado_teste, numero_serie_udc, leds, buzzer, eeprom, flash, ram,
        control_aliment_plano_isolado, ethernet_ping, loopback, io_expander, rtc,
        sensor_temperatura, uart, adc_ch_1, adc_ch_2, adc_ch_3, adc_ch_4, adc_ch_5,
        adc_ch_6, adc_ch_7, adc_ch_8, details
from LogUdc;
end$$
delimiter ;
