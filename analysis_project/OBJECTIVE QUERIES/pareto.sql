select * from tran_dtl;
select * from product;
select * from member;
select * from tran_hdr;

select member_id,y,m,sum(s) as sale from
(select th.member_id,year(th.tran_dt) as y,month(td.tran_dt) as m,sum(amt) as s from tran_dtl td
join tran_hdr th on th.tran_id=td.tran_id
group by th.member_id,y,m
having  y=2023 and m between 7 and 12
order by th.member_id)s1
group by member_id,y,m
order by sale desc;
 
-- member pareto
select member_id,y,sum(s) as total from (
select th.member_id,year(th.tran_dt) as y,month(td.tran_dt) as m,sum(amt) as s from tran_dtl td
join tran_hdr th on th.tran_id=td.tran_id
group by th.member_id,y,m
having  y=2023 and m between 7 and 12
order by s desc)s1
group by member_id,y
order by total desc;

-- product pareto
SELECT SUM(sale) AS total
	FROM(
		SELECT product_id, SUM(s) sale
		FROM(
			SELECT product_id, YEAR(tran_dt) AS y, MONTH(tran_dt)AS m, SUM(amt) AS s
			FROM tran_dtl
			GROUP BY product_id, y, m
			HAVING y = 2023 AND m BETWEEN 6 AND 12
			ORDER BY product_id, s
			) s1
		GROUP BY product_id
		) s2;
        
        
        
        


-- total
select year(tran_dt) as y,month(tran_dt)as m,sum(amt) 
from tran_dtl
group by amt,y,m
having  y=2023 and m between 7 and 12
order by amt desc;

select member_id,sum(total) as total from (
select member_id,year(td.tran_dt) as y,month(td.tran_dt)as m,sum(amt) as total 
from tran_dtl td
join tran_hdr th on th.tran_id=td.tran_id
group by member_id,amt,y,m
having  y=2023 and m between 7 and 12)s
group by member_id
order by total desc;

use retail_project;

select max(qty) from tran_dtl ;