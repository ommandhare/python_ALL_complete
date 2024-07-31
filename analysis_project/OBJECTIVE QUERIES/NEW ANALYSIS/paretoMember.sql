select *
from
(
select *,
SUM(total) OVER (ORDER BY total DESC) AS cumulative_sum_total,
round(SUM(total) OVER (ORDER BY total DESC) * 100.0 / SUM(total) OVER ()) AS cumulative_percentage
from
(
select 
member_id,
year(td.tran_dt) y,
round(sum(amt)) total
from 
tran_dtl td
join tran_hdr th on td.tran_id=th.tran_id
where year(td.tran_dt)='2024'
group by member_id,y
order by total desc
)s
group by member_id,y,total
)s1
-- where cumulative_percentage<=80 

