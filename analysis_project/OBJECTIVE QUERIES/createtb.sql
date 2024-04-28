create database retail_project;
use retail_project;

CREATE TABLE member (
    member_id   INT             NOT NULL,
    first_name  VARCHAR(20)     NOT NULL,
    last_name   VARCHAR(20)     NOT NULL,
    store_id    INT             NOT NULL,
    reg_date    DATE            NOT NULL,
    PRIMARY KEY (member_id)
);


use retail;
CREATE TABLE tran_hdr (
   tran_id   VARCHAR(70)     NOT NULL,
   store_id  INT             NOT NULL,
   member_id INT             NOT NULL,
   tran_dt   DATE            NOT NULL,
   PRIMARY KEY(tran_id, tran_dt)
);

CREATE TABLE tran_dtl (
   tran_id      VARCHAR(70)     NOT NULL,
   product_id   INT             NOT NULL,
   qty          INT             NOT NULL,
   amt          FLOAT      NOT NULL,
   tran_dt      DATE            NOT NULL,
   PRIMARY KEY(tran_id,product_id,tran_dt)
);



CREATE TABLE product (
    product_id   INT             NOT NULL,
    description  VARCHAR(40)     NOT NULL,
    price  	 FLOAT(8,5)      NOT NULL,
    category     VARCHAR(40)     NOT NULL,
    max_qty      INT	         NOT NULL,    
    PRIMARY KEY (product_id)
);


create table trip_count(
member_id int,
per_date date,
trip_count int
);

select * from tran_dtl;
select * from tran_hdr;
