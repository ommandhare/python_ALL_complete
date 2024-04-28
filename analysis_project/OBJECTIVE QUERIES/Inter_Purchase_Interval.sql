use retail_project;
select * from tran_hdr th
join tran_dtl td on th.tran_id=td.tran_dt
 where th.member_id='1001' and month(td.tran_dt)=1;
select * from tran_dtl;


-- total count of visit per year
select member_id,per_year,sum(count) from (
	select member_id,year(tran_dt) as per_year,count(tran_dt) as count from 
	(
		select th.member_id,td.tran_dt from tran_dtl td
		join tran_hdr th on td.tran_id=th.tran_id
		)s
			group by member_id,tran_dt
            order by member_id) s1
	group by member_id,per_year
    order by member_id;

-- trip_count
select member_id,date(tran_dt) as per_month,count(tran_dt) as trip_count from 
	(
		select th.member_id,td.tran_dt from tran_dtl td
		join tran_hdr th on td.tran_id=th.tran_id
		)s
			group by member_id,tran_dt
            order by member_id;
            
            
            
-- INTER PURCHASE INTERVAL

	select member_id, per_date,count(*) as trip_count from
		 (select th.member_id,date(td.tran_dt) as per_date,td.tran_id,count(product_id) as count_of_product from tran_dtl td
			join tran_hdr th on td.tran_id=th.tran_id
			group by th.member_id, date(td.tran_dt),td.tran_id
			order by member_id )s
	group by member_id,per_date;
    
    ##############################
    -- final IPI
    ##############################
    
    select *,date_now-last_date as inter_purchase_interval from 
    (
    select member_id,lag(date_now) over (partition by member_id  order by date_now) as last_date,date_now from
    (select member_id,td.tran_dt as date_now from tran_dtl td
    join tran_hdr th on td.tran_id=th.tran_id)s 
    group by member_id,date_now
    )s1
    group by member_id,date_now;
    
            
            
		