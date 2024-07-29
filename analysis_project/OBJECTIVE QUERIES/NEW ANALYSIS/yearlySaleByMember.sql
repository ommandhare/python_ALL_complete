use retail_project;


select * from member;

 -- YEARLY SALE FOR EACH MEMBER

select member_id,year(td.tran_dt) year,round(sum(td.amt)) as yearly_sale
from tran_dtl td
join tran_hdr th on td.tran_id=th.tran_id
group by member_id,year(td.tran_dt)
order by member_id ;
 