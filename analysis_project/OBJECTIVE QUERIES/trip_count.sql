

-- FINAL TRIP COUNT QUERY
-- >>>>>>>>>>>
use retail_project;
use retail;
select member_id, per_date,count(*) as trip_count from
(select th.member_id,date(td.tran_dt) as per_date,td.tran_id,count(product_id) as count_of_product from tran_dtl td
		join tran_hdr th on td.tran_id=th.tran_id
        WHERE td.tran_dt < current_date() AND td.tran_dt >= DATE_SUB(CURRENT_DATE(), interval 1 year)
        group by th.member_id, date(td.tran_dt),td.tran_id
        order by member_id )s
group by member_id,per_date
 ;
         -- WHERE td.tran_dt < current_date() AND td.tran_dt >= DATE_SUB(CURRENT_DATE(), interval 1 year)