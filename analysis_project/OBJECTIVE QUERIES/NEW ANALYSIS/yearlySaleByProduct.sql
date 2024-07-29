use retail_project;


select * from member;

 -- YEARLY SALE FOR EACH PRODUCT

select product_id,year(td.tran_dt) year,round(sum(td.amt)) as yearly_sale
from tran_dtl td
group by product_id,year(td.tran_dt)
order by product_id ;
 