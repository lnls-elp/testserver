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
    in p_rtc_communication              varchar(45),
    in p_rtc_interrupt                  varchar(45),
    in p_sensor_temperatura             varchar(45),
    in p_control_aliment_plano_isolado  varchar(45),
    in p_rs485                          varchar(45),
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
    rtc_communication,
    rtc_interrupt,
    sensor_temperatura,
    control_aliment_plano_isolado,
    rs485,
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
    p_rtc_communication,
    p_rtc_interrupt,
    p_sensor_temperatura,
    p_control_aliment_plano_isolado,
    p_rs485,
	p_details
);
end$$
delimiter ;
