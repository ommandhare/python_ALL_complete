-- ###########################
-- reward title by member

select *,
 CASE 
   WHEN reward_points BETWEEN 0.095 and 1 THEN 'PLATINUM '
	   WHEN reward_points BETWEEN 0.07 and 0.095 THEN 'GOLD'
	   WHEN reward_points BETWEEN 0.03 and 0.07 THEN 'SILVER '
	   WHEN reward_points BETWEEN 0 and 0.3 THEN 'BRONZE'
		
END as REWARD_TITLE
from
(

	select member_id,total_sale,
	  round(( total_sale-min_sale) /  (max_sale-min_sale),3) as reward_points
	 from
	(   -- calculating min_max 
		select *,
		 MAX(total_sale) OVER () AS max_sale,
		 MIN(total_sale) OVER () as min_sale
		from
			(   -- calculate total sale
			   select th.member_id, round(sum(amt)) AS total_sale FROM tran_hdr th
			   join tran_dtl td  ON th.tran_id = td.tran_id 
			   group by th.member_id
					)s
			group by member_id
	)s2
	)s3
    ;
