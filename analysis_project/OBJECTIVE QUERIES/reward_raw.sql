


use retail_project;



select *,
 CASE 
   WHEN reward_points BETWEEN 0.8 and 1 THEN 'PLATINUM '
   WHEN reward_points BETWEEN 0.5 and 0.8 THEN 'GOLD'
   WHEN reward_points BETWEEN 0.2 and 0.5 THEN 'SILVER '
   WHEN reward_points BETWEEN 0 and 0.2 THEN 'BRONZE'
		
END as REWARD_TITLE
from
(

	select member_id,total_sale,
	  ( total_sale-min_sale) /  (max_sale-min_sale) as reward_points
	 from
	(   -- calculating min_max 
		select *,
		 MAX(total_sale) OVER () AS max_sale,
		 MIN(total_sale) OVER () as min_sale
		from
			(   -- calculate total sale
			   select th.member_id, sum(amt) AS total_sale FROM tran_hdr th
			   join tran_dtl td  ON th.tran_id = td.tran_id 
			   group by th.member_id
					)s
			group by member_id
	)s2
	)s3
    ;





-- test

SELECT th.member_id, product_id, COUNT(*) AS trip  FROM tran_hdr th
JOIN tran_dtl td  ON th.tran_id = td.tran_id 
WHERE product_id=3 and member_id='1001' 
GROUP BY th.member_id,product_id