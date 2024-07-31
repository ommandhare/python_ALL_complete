 
 -- INTER_PURCHASE_INTERVAL AVERAGE YEARLY
 
 
 select member_id,yearly,round(avg(inter_purchase_interval))  as average_IPI
 from
 (
 select *,date_now-last_date as inter_purchase_interval from 
    (
    select member_id,yearly,monthly,lag(date_now) over (partition by member_id  order by date_now) as last_date,date_now from
    (select member_id,year(td.tran_dt) as yearly,month(td.tran_dt) as monthly,td.tran_dt as date_now from tran_dtl td
    join tran_hdr th on td.tran_id=th.tran_id)s 
    group by member_id,date_now
    )s1
    group by member_id,date_now,yearly
  )s2
  group by member_id,yearly