use retail_project;


select * from member;

 -- AVERAGE MONTHLY SALE FOR EACH PRODUCT
 
 select product_id,year,month,round(avg(sum)) average_monthly_Sale
from 
    (select product_id,year(tran_dt) year,month(tran_dt) month,day(tran_dt) per_day,sum(amt) as sum
	from tran_dtl
	 group by product_id,year(tran_dt),month(tran_dt),day(tran_dt) 
	 order by product_id) s
 group by product_id,year,month
 ;