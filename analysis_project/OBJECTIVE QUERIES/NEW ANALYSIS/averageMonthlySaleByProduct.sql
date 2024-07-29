use retail_project;


select * from member;

 -- AVERAGE MONTHLY SALE FOR EACH product
 
 select member_id,year,month,round(avg(sum)) average_monthly_Sale
from 
    (select member_id,year(td.tran_dt) year,month(td.tran_dt) month,day(td.tran_dt) per_day,sum(td.amt) as sum
	from tran_dtl td
    join tran_hdr th on td.tran_id=th.tran_id
	 group by member_id,year(td.tran_dt),month(td.tran_dt),day(td.tran_dt) 
	 order by member_id) s
 group by member_id,year,month
 ;
 