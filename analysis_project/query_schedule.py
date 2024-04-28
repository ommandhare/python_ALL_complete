import pandas as pd
import mysql.connector
import schedule
import csv
import time




def query_run():

    conn = mysql.connector.connect(
        host='localhost',
        user='root',
        password='0777',
        database='retail_project'
    )

    cursor = conn.cursor()

    # member_transition_matrix_csv generator
    query1=(""" select *,
CASE 
   WHEN membership = 'platinum' then '20%'
   WHEN membership = 'gold' then '10%' 
   WHEN membership = 'silver' then '5%' 
   WHEN membership = 'bronze' then '-' 
   END as member_discount 
from (
	select member_id,yearly_trip_count,
	CASE 
	   WHEN yearly_trip_count BETWEEN 110 and 120 THEN 'platinum'
	   WHEN yearly_trip_count BETWEEN 90 and 110 THEN 'gold'
	   WHEN yearly_trip_count BETWEEN 80 and 90 THEN 'silver'
	   WHEN yearly_trip_count BETWEEN 70 and 80 THEN 'bronze'
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
						WHERE td.tran_dt < current_date() AND td.tran_dt >= DATE_SUB(CURRENT_DATE(), interval 1 year)
						group by th.member_id, date(td.tran_dt),td.tran_id
						order by member_id )s
			group by member_id,per_year
		)s1
		group by member_id
	)s2
	order by yearly_trip_count
	)s3 ;
    """)
    cursor.execute(query1)
    results1 = cursor.fetchall()
    count=0
    print(results1)
    mem_tran_path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\member_transition_matrix.csv"
    with open(mem_tran_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, results1)
        csv_writer.writerow(['member_id', 'yearly_trip_count', 'membership', 'member_discount'])
        csv_writer.writerows(results1)

    print(f"Data has been written to {mem_tran_path}")






    # trip_count_csv_generator
    query2=(""" select member_id, per_date,count(*) as trip_count from
(select th.member_id,date(td.tran_dt) as per_date,td.tran_id,count(product_id) as count_of_product from tran_dtl td
		join tran_hdr th on td.tran_id=th.tran_id
        WHERE td.tran_dt < current_date() AND td.tran_dt >= DATE_SUB(CURRENT_DATE(), interval 1 year)
        group by th.member_id, date(td.tran_dt),td.tran_id
        order by member_id )s
group by member_id,per_date
 ;""")
    cursor.execute(query2)
    results2 = cursor.fetchall()
    count=0
    print(results2)
    trip_path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\trip_count.csv"
    with open(trip_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, results2)
        csv_writer.writerow(['member_id', 'per_date', 'trip_count'])
        csv_writer.writerows(results2)

    print(f"Data has been written to {trip_path}")



    # reward_csv_generator
    query3=(""" select *,
 CASE 
   WHEN reward_points BETWEEN 0.8 and 1 THEN 'PLATINUM '
   WHEN reward_points BETWEEN 0.5 and 0.8 THEN 'GOLD'
   WHEN reward_points BETWEEN 0.2 and 0.5 THEN 'SILVER '
   WHEN reward_points BETWEEN 0 and 0.2 THEN 'BRONZE'
		
END as REWARD_TITLE
from
(
    -- calculating reward points
    -- reward=tripcount-mintrip/maxtrip-mintrip
	select member_id,product_id,trip_count,
	  ( trip_count-min_trip) /  (max_trip-min_trip) as reward_points
	 from
	(   -- calculating min_max 
		select *,
		 MAX(trip_count) OVER (PARTITION BY member_id) AS max_trip,
		 MIN(trip_count)OVER (PARTITION BY member_id) as min_trip
		from
			( 
			   -- calculate trip_count per member per product
			   select th.member_id, product_id, COUNT(*) AS trip_count FROM tran_hdr th
			   join tran_dtl td  ON th.tran_id = td.tran_id 
               WHERE td.tran_dt < current_date() AND td.tran_dt >= DATE_SUB(CURRENT_DATE(), interval 1 year)
			   group by th.member_id,product_id
			
            )s
			group by member_id,product_id
	)s2
)s3
    ;""")
    cursor.execute(query3)
    results3 = cursor.fetchall()
    count=0
    print(results3)
    reward_path=r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\reward.csv"
    with open(reward_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, results3)
        csv_writer.writerow(['member_id', 'product_id', 'trip_count','reward_points','reward_title'])
        csv_writer.writerows(results3)

    print(f"Data has been written to {reward_path}")

    # affinity_csv_generator
    query4 = (""" select target1, target2,concat(target1,"_",target2) as combination_pair, count as target1_count,combo_count,(combo_count/count) as affinity_score
 from
 (
select d1.product_id as target1 ,d2.product_id as target2,count(d1.tran_id) as combo_count from tran_dtl d1
join tran_dtl d2 on d1.tran_id=d2.tran_id
where d1.product_id!=d2.product_id  -- and d1.product_id='100'
group by d1.product_id,d2.product_id 
order by combo_count desc
)a
join (
select product_id,count(product_id) as count from tran_dtl
group by product_id)b
on a.target1=b.product_id
;""")
    cursor.execute(query4)
    results4 = cursor.fetchall()
    count = 0
    print(results4)
    affinty_path = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\affinity.csv"
    with open(affinty_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, results4)
        csv_writer.writerow(['target1', 'target2', 'combo_pair', 'target1_count', 'combo_conut','affinity_score'])
        csv_writer.writerows(results4)

    print(f"Data has been written to {affinty_path}")





    # seasonality_csv_generator
    query5 = (""" select *,round(monthly_sale/avg_monthly_sale,1) as seasonality_index
	from
		(

		select *,round(avg(monthly_sale) OVER (PARTITION BY product_id,year)) as avg_monthly_Sale
		from
			(
			
			select p.product_id,p.description,p.category,year(tran_dt)as year,month(td.tran_dt) as month,sum(td.amt) as monthly_sale
			from product p
			join tran_dtl td
			on p.product_id=td.product_id
			group by product_id,description,category,year(tran_dt),month(td.tran_dt)
				 ) s
                 
                 )s1;
                 """)
    cursor.execute(query5)
    results5 = cursor.fetchall()
    count = 0
    print(results5)
    seasonality_path = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\seasonality.csv"
    with open(seasonality_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, results5)
        csv_writer.writerow(['product_id', 'description', 'category', 'year', 'month', 'monthly_sale', 'avg_monthly_Sale', 'seasonality_index'])
        csv_writer.writerows(results5)

    print(f"Data has been written to {seasonality_path}")

    # final_total_dicount_csv_generator
    query6 = (""" select *,
    CASE WHEN membership = 'Platinum' 
    THEN concat(member_discount+reward_discount,'%') else '-' 
    end as added_prime_discount
    from
    (
    select mpr.member_id,mtr.membership,mpr.reward_discount,mtr.member_discount from member_product_reward mpr
    join member_reward_by_trip mtr on mtr.member_id=mpr.member_id
    )s1; 
                     """)
    cursor.execute(query6)
    results6 = cursor.fetchall()
    count = 0
    print(results6)
    discount_path = r"C:\Users\HP\PycharmProjects\pythonProject.py\venv\Assignments\analysis_project\daily_files\final_total_dicount.csv"
    with open(discount_path, 'w', newline='') as csvfile:
        csv_writer = csv.writer(csvfile, results6)
        csv_writer.writerow(
            ['member_id', 'membership', 'reward_discount', 'member_discount', 'added_prime_discount'])
        csv_writer.writerows(results6)

    print(f"Data has been written to {discount_path}")

    conn.commit()
    cursor.close()
    conn.close()


query_run()

# Schedule the daily task to run every day at a specific time (adjust time as needed)
# schedule.every().day.at('12:00').do(daily_task)
# schedule.every(40).seconds.do(query_run)
#
# while True:
#  schedule.run_pending()
#  time.sleep(1)