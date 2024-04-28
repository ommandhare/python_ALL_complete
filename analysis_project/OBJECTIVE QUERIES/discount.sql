use retail_project;
    ###############
    -- discount
    #################
   select member_id,total_IPI,
   
   case
		         WHEN total_IPI BETWEEN 80  and 85 THEN '5% discount '
         		 WHEN total_IPI BETWEEN 70  and 80 THEN '25% discount '
                 WHEN total_IPI BETWEEN 65 and 70 THEN '40% discount'
        else 'no discount'
   end as discount
   from
    (
    select member_id,avg(inter_purchase_interval) as total_IPI
    from
    (
		select *,date_now-last_date as inter_purchase_interval from 
		(
		  select member_id,lag(date_now) over (partition by member_id  order by date_now) as last_date,date_now from
			(   select member_id,td.tran_dt as date_now from tran_dtl td
				join tran_hdr th on td.tran_id=th.tran_id
			)s 
				group by member_id,date_now
		)s1
		group by member_id,date_now
        )s2
        group by member_id
    )s3;