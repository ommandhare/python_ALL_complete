select product_id,year(tran_dt),month(tran_dt),avg(amt)
from tran_dtl
 group by product_id,year(tran_dt),month(tran_dt)
 order by product_id;	
    
select product_id,y,m,avg(sum)
from 
    (select product_id,year(tran_dt) y,month(tran_dt) m,day(tran_dt) per_day,sum(amt) as sum
	from tran_dtl
	 group by product_id,year(tran_dt),month(tran_dt),day(tran_dt) 
	 order by product_id) s
 group by product_id,y,m
 ;
 
 use retail_project;
 
 