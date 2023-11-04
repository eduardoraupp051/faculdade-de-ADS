-- comentario]
/*comentario longo
*/

/*
clientes (id int primary key, nome varchar(50));
enderecos (id int pk, logradouro varchar(50), numero int, bairro char(30), cidade varchar(30), estado char(2), id_cliente int references clientes(id))


CREATE TABLE <NOME DA TABELA>
(
    ATRIBUTO|DOMINIO|RESTRIÇÃO DE VAZIOS| CHAVES
)
*/


CREATE TABLE Clientes 
(
    id int not null Primary Key,
    Nome varchar(100)
);

CREATE TABLE enderecos (
    id int not null Primary key,
    logradouro varchar(50),
    numero int, 
    bairro char(30),
    cidade varchar(30),
    estado char(2),
    id_Clientes int not null,
    constraint Clientes_tem_enderecos
        Foreign key (id_Clientes) references Clientes(id)

);

CREATE TABLE professor 
(
    id_prof int not null Primary key,
    Nome varchar(100),
    especializacao varchar(100),
    idade int not null
);

CREATE TABLE Disciplina 
(
    id_disc int not null Primary Key,
    Disciplina varchar(50),
    carga_horaria int not null,
);

CREATE TABLE leciona
(
    id_disc int not null,
    constraint professor_leciona_discplina
        Foreign key (id_disc)
    id_profint not null,
    constraint disciplina_lecionada_professor
        Foreign key (id_prof)
);

CREATE TABLE software
(
    id_soft int not null primary key,
    nome varchar(50), 
    tipo varchar(50)
);

CREATE TABLE utiliza 
(
    id_soft int not null,
    constraint software_utiliza_discplina
        Foreign key (id_soft)

    id_disc int not null,
    constraint Disciplina_utiliza_software
        Foreign key (id_soft)

);

