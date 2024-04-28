

select m.member_id,a.target1,a.target2,m.REWARD_TITLE,m.reward_points,a.ratio , reward_points*ratio as recomend from member_product_reward m
join affinity a on m.product_id=a.target1
;
