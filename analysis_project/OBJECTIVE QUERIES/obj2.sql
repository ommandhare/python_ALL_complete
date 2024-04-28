use retail_project;

select * from tran_dtl;
select * from product;
select * from member;
select * from tran_hdr;

-- MONTHLY,YEARLY SALE FOR EACH PRODUCT,MONTH

select th.member_id,td.product_id, year(td.tran_dt) as per_year,
month(td.tran_dt) as per_month,round(sum(td.amt)) as total_sale
from tran_dtl td
join tran_hdr th on td.tran_id=th.tran_id 

group by th.member_id,td.product_id,per_year,per_month;