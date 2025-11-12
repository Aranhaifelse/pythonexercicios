

create table produtos(
produto_id serial primary key,
valor float not null,
nome varchar(255)
);

create table pedidos(
pedido_id serial primary key,
garcom_id int not null,
hora varchar(255) not null,
data date,
foreign key (garcom_id) references garcons (garcom_id)
);

create table garcons(
garcom_id serial primary key,
nome varchar(255) not null,
telefone int not null,
email varchar(255) unique not null,
password bytes not null
);

create table admin(
admin_id serial primary key,
nome varchar(255) not null,
email varchar(255) unique not null,
password bytes not null
)


create table mesas(
mesa_id serial primary key,
quantidade int not null 
);
 
create table pedido_produto (
pedido_id int not null,
produto_id int not null,
primary key (pedido_id, produto_id),
foreign key (pedido_id) references pedidos (pedido_id),
foreign key (produto_id) references produtos (produto_id)
);

create table pedido_mesa (
pedido_id int not null,
mesa_id int not null,
primary key (pedido_id, mesa_id),
foreign key (pedido_id) references pedidos (pedido_id),
foreign key (mesa_id) references mesas (mesa_id)
);






insert into produtos (valor, tipo) values
(22.99, 'Pizza de frango'),
(30.00, 'Pizza de camarão'),
(20.00, 'Pizza de calabresa'),
(5.00, 'Coca-cola'),
(2.50, 'Água S/gás');

insert into garcons (nome, telefone) values
('Jackson Marfim', '82998279694'),
('Michele Ribeiro','82985962418');

insert into mesas (quantidade) values
(2),
(5),
(3);

insert into pedidos (hora, data, produto_id, garcom_id) values
('12:50', '2025-10-17', 1, 1),
('12:50', '2025-10-17', 4, 1),
('13:20', '2025-10-17', 3, 2),
('14:00', '2025-10-17', 5, 2),
('17:35', '2025-11-17', 2, 1);

insert into pedido_produto (pedido_id, produto_id) values 
(1, 1),
(1, 4),
(2, 3),
(2, 5),
(3, 2);

insert into pedido_mesa (pedido_id, mesa_id) values
(1, 1),
(2, 2),
(3, 3);









