use retail_project;


select * from member;

 -- TOTAL AVERAGE SALE FOR EACH PRODUCT

select product_id,
round(avg(amt)) as average_Sale
from tran_dtl
group by product_id;
 