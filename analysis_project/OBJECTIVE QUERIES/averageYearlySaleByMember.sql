use retail_project;


select * from member;

 -- AVERAGE YEARLY SALE FOR EACH MEMBER
 
 select member_id,year,round(avg(sum)) average_yearly_Sale
from 
    (select member_id,year(td.tran_dt) year,sum(td.amt) as sum
	from tran_dtl td
    join tran_hdr th on td.tran_id=th.tran_id
	 group by member_id,year(td.tran_dt)
	 order by member_id)s
 group by member_id,year
 ;
 