

-- ############################
-- member transition matrix
-- ##########################
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
	   WHEN yearly_trip_count between 310 and 340 THEN 'platinum'
	   WHEN yearly_trip_count between 300 and 310 THEN 'gold'
	   WHEN yearly_trip_count  between 270 and 300 THEN 'silver'
	   WHEN yearly_trip_count <=270 THEN 'bronze'
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
						-- WHERE td.tran_dt < current_date() AND td.tran_dt >= DATE_SUB(CURRENT_DATE(), interval 1 year)
						group by th.member_id, date(td.tran_dt),td.tran_id
						order by member_id )s
			group by member_id,per_year
		)s1
		group by member_id
	)s2
	order by yearly_trip_count
	)s3 ;
    