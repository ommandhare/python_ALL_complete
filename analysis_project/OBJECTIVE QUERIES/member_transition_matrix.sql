

-- ############################
-- member transition matrix
-- ##########################
use retail_project;
select * from member_reward_by_trip;
truncate table member_reward_by_trip;
-- insert into member_reward_by_trip 

select *,
CASE 
   WHEN membership = 'platinum' then '20%'
   WHEN membership = 'gold' then '10%' 
   WHEN membership = 'silver' then '5%' 
   WHEN membership = 'bronze' then '-' 
   END as member_discount 
from (
	select member_id,yearly_trip_count,
	CASE 
	   WHEN yearly_trip_count BETWEEN 110 and 120 THEN 'platinum'
	   WHEN yearly_trip_count BETWEEN 90 and 110 THEN 'gold'
	   WHEN yearly_trip_count BETWEEN 80 and 90 THEN 'silver'
	   WHEN yearly_trip_count BETWEEN 70 and 80 THEN 'bronze'
	end as membership
	from
	(
		select member_id,
		sum(trip_count) as yearly_trip_count
		from
		(
			select member_id, year(per_date) as per_year,count(*) as trip_count
            from
				(       select th.member_id,date(td.tran_dt) as per_date,td.tran_id,
						count(product_id) as count_of_product from tran_dtl td
						join tran_hdr th on td.tran_id=th.tran_id
						WHERE td.tran_dt < current_date() AND td.tran_dt >= DATE_SUB(CURRENT_DATE(), interval 1 year)
						group by th.member_id, date(td.tran_dt),td.tran_id
						order by member_id )s
			group by member_id,per_year
		)s1
		group by member_id
	)s2
	order by yearly_trip_count
	)s3 ;
    