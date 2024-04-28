use retail_project;

-- calculating reward title on basis of reward points
select *,
 CASE 
   WHEN reward_points >=1 then '15% discount'
   WHEN reward_points <=0.85  then '5% discount'
   ELSE 'no discount'
		
END as discount_of_product
from
(
    -- calculating reward points
    -- reward=tripcount-mintrip/maxtrip-mintrip
	select member_id,product_id,trip_count,
	  ( trip_count-min_trip) /  (max_trip-min_trip) as reward_points
	 from
	(   -- calculating min_max 
		select *,
		 MAX(trip_count) OVER (PARTITION BY member_id) AS max_trip,
		 MIN(trip_count)OVER (PARTITION BY member_id) as min_trip
		from
			( 
			   -- calculate trip_count per member per product
			   select th.member_id, product_id, COUNT(*) AS trip_count FROM tran_hdr th
			   join tran_dtl td  ON th.tran_id = td.tran_id 
			   group by th.member_id,product_id
			
            )s
			group by member_id,product_id
	)s2
)s3
    ;