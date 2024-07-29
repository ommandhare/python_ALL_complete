use retail_project;


select * from member;

 -- TOTAL SALE FOR EACH PRODUCT

select product_id,
round(sum(amt)) as total_Sale
from tran_dtl
group by product_id;
 