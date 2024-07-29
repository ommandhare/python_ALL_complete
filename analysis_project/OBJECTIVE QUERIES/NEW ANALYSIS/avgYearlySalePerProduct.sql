use retail_project;


select product_id,year(td.tran_dt) year,round(avg(td.amt)) as Average_yearly_sale
from tran_dtl td
group by product_id,year(td.tran_dt)
order by product_id ;
 