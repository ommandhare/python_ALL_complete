

select th.member_id,
round(avg(td.amt)) as Average_total_Sale
from tran_dtl td
join tran_hdr th on td.tran_id=th.tran_id
group by th.member_id
order by th.member_id;