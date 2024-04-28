use retail_project;

select * from tran_dtl;
select * from product;
select * from member;
select * from tran_hdr;

select m.member_id,m.first_name,month(th.tran_dt) as per_month,sum(td.amt) as total_purchase
from tran_dtl td
join tran_hdr th on td.tran_id=th.tran_id
join member m on m.member_id=th.member_id
group by m.member_id,per_month;
