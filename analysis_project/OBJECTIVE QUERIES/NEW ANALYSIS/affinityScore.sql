-- combination with ratio (affinity score)
 select target1, target2,concat(target1,"_",target2) as combination_pair,combo_count, count as target1_count,(combo_count/count) as affinity_score
 from
 (
select d1.product_id as target1,d2.product_id as target2,count(d1.tran_id) as combo_count from tran_dtl d1
join tran_dtl d2 on d1.tran_id=d2.tran_id
where d1.product_id!=d2.product_id  -- and d1.product_id='100'
group by d1.product_id,d2.product_id 
order by combo_count desc
)a
join (
select product_id,count(product_id) as count from tran_dtl
group by product_id)b
on a.target1=b.product_id
;
 -- WHERE td.tran_dt < current_date() AND td.tran_dt >= DATE_SUB(CURRENT_DATE(), interval 1 year)