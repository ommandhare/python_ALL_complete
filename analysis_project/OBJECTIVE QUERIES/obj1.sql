use retail_project;
use retail;
select * from tran_dtl;
select * from product;
select * from product_by_category;

select * from member;

 -- AVERAGE MONTHLY SALE FOR EACH PRODUCT
 
 select product_id,y,m,round(avg(sum)) average_monthly_Sale
from 
    (select product_id,year(tran_dt) y,month(tran_dt) m,day(tran_dt) per_day,sum(amt) as sum
	from tran_dtl
	 group by product_id,year(tran_dt),month(tran_dt),day(tran_dt) 
	 order by product_id) s
 group by product_id,y,m
 ;
 