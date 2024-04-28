
select * from member_reward_by_trip;
select * from member_product_reward;


select *,
CASE WHEN membership = 'Platinum' THEN concat(member_discount+reward_discount,'%') else '-' end as added_prime_discount
from
(
select mpr.member_id,mtr.membership,mpr.reward_discount,mtr.member_discount from member_product_reward mpr
join member_reward_by_trip mtr on mtr.member_id=mpr.member_id
)s1; 