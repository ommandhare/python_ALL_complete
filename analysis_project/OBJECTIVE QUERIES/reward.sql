
-- ################################
-- reward by member and product_id
-- ################################

use retail_project;
truncate table member_product_reward;
-- calculating reward title on basis of reward points
-- insert into member_product_reward 
select * ,
CASE 
   WHEN REWARD_TITLE = 'PLATINUM' then '15%'
   WHEN REWARD_TITLE = 'GOLD' then '10%' 
   WHEN REWARD_TITLE = 'SILVER' then '5%' 
   WHEN REWARD_TITLE = 'BRONZE' then '-' 

   END as reward_discount
from
(select *,
 CASE 
   WHEN reward_points BETWEEN 0.8 and 1 THEN 'PLATINUM'
   WHEN reward_points BETWEEN 0.5 and 0.8 THEN 'GOLD'
   WHEN reward_points BETWEEN 0.2 and 0.5 THEN 'SILVER'
   WHEN reward_points BETWEEN 0 and 0.2 THEN 'BRONZE'
		
END as REWARD_TITLE
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
               WHERE td.tran_dt < current_date() AND td.tran_dt >= DATE_SUB(CURRENT_DATE(), interval 1 year)
			   group by th.member_id,product_id
			
            )s
			group by member_id,product_id
	)s2
)s3
   )s4 ;
    
    
     -- WHERE td.tran_dt < current_date() AND td.tran_dt >= DATE_SUB(CURRENT_DATE(), interval 1 year)