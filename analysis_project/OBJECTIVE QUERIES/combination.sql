select * from tran_dtl;
select * from product;




-- COMBINATION MAXIMUM 
select target1,
     max(combo_count) as high_combo
 from 
(
select d1.product_id as target1 ,d2.product_id as target2,count(d1.tran_id) as combo_count from tran_dtl d1
join tran_dtl d2 on d1.tran_id=d2.tran_id
where d1.product_id!=d2.product_id  -- and d1.product_id='100'
group by d1.product_id,d2.product_id 
order by combo_count desc

)s
group by target1
order by target1;



-- COMBINATION MINIMUM
select target1,
     min(combo_count) as high_combo
 from 
(
select d1.product_id as target1 ,d2.product_id as target2,count(d1.tran_id) as combo_count from tran_dtl d1
join tran_dtl d2 on d1.tran_id=d2.tran_id
where d1.product_id!=d2.product_id  -- and d1.product_id='100'
group by d1.product_id,d2.product_id 
order by combo_count desc

)s
group by target1
order by target1;




 -- combo
select d1.product_id as target1 ,d2.product_id as target2,count(d1.tran_id) as combo_count from tran_dtl d1
join tran_dtl d2 on d1.tran_id=d2.tran_id
where d1.product_id!=d2.product_id  -- and d1.product_id='100'
group by d1.product_id,d2.product_id 
order by combo_count desc;



-- count
select product_id,count(product_id) from tran_dtl
group by product_id;




 -- combination with ratio 
 
 select target1, target2, count,combo_count,(combo_count/count) as ratio
 from
 (
select d1.product_id as target1 ,d2.product_id as target2,count(d1.tran_id) as combo_count from tran_dtl d1
join tran_dtl d2 on d1.tran_id=d2.tran_id
where d1.product_id!=d2.product_id  -- and d1.product_id='100'
group by d1.product_id,d2.product_id 
order by combo_count desc
)a

join 
(
select product_id,count(product_id) as count from tran_dtl
group by product_id)b
on a.target1=b.product_id
;