


-- TRIP COUNT MONTHLY
-- >>>>>>>>>>>

select member_id,per_year,per_month,count(*) as trip_count from
(select th.member_id,year(td.tran_dt) per_year,month(td.tran_dt) per_month,td.tran_id,count(product_id) as count_of_product from tran_dtl td
		join tran_hdr th on td.tran_id=th.tran_id
        WHERE td.tran_dt < current_date() AND td.tran_dt >= DATE_SUB(CURRENT_DATE(), interval 1 year)
        group by th.member_id, year(td.tran_dt),td.tran_id,month(td.tran_dt)
        order by member_id )s
group by member_id,per_year,per_month