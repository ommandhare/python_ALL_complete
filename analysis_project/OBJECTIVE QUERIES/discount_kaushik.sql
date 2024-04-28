USE retail_project;


-- INSERT INTO product_reward_by_trip(member_id, product_id, description, reward_score, reward_cat)
SELECT *, CONCAT(discount + extra_discount,'%') AS total_discount
FROM(
	SELECT tccc.member_id, product_id, description, reward_category AS discount,
	CASE WHEN reward = 'Platinum' THEN '5%' ELSE '-' END AS extra_discount
	FROM(
		SELECT member_id, product_id, description, reward_score,
		CASE
			WHEN reward_score < 0.3 THEN 'NO REWARD'
			WHEN reward_score >= 0.3 AND reward_score < 0.6 THEN '5%'
			WHEN reward_score >= 0.6 AND reward_score < 0.9 THEN '12%'
			WHEN reward_score >= 0.9 THEN '18%'
		END AS reward_category
		FROM(
			SELECT *, ROUND((trip-min_trip)/(max_trip-min_trip),4) AS reward_score
			FROM(
				SELECT *, MIN(trip) OVER(PARTITION BY member_id) AS min_trip, MAX(trip) OVER(PARTITION BY member_id) AS max_trip
				FROM(
					SELECT member_id, td.product_id, p.description, COUNT(td.tran_id) AS trip
					FROM tran_dtl td
					JOIN tran_hdr th ON td.tran_id = th.tran_id
					JOIN product p ON p.product_id = td.product_id
					WHERE td.tran_dt < current_date() AND td.tran_dt >= DATE_SUB(CURRENT_DATE(), INTERVAL 1 YEAR)
					GROUP BY member_id, td.product_id
					) t
				) tc
			) tcc
		) tccc
	JOIN member_reward_by_trip m ON m.member_id = tccc.member_id
	) tm
-- 	) tccc
-- GROUP BY reward_category
