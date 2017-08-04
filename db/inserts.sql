use testserverdb;

insert into CanalDcct(id, descricao) values (1, 'Canal 1');
insert into CanalDcct(id, descricao) values (2, 'Canal 2');

insert into CanalFonte(id, descricao) values (1, 'Canal 1');
insert into CanalFonte(id, descricao) values (2, 'Canal 2');
insert into CanalFonte(id, descricao) values (3, 'Canal 3');
insert into CanalFonte(id, descricao) values (4, 'Canal 4');

insert into TipoTesteFonte(id, descricao) values (1, 'Normal');
insert into TipoTesteFonte(id, descricao) values (2, 'Burn-In');

insert into Medida(id, descricao) values (1, 'HRADC');
insert into Medida(id, descricao) values (2, 'DM');
