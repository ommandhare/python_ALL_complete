-- #########################################################
-- seasonality index (monthly sale/monthly avg sale)
-- #########################################################
 select *,round(monthly_sale/avg_monthly_sale,1) as seasonality_index
	from
		(

		select *,round(avg(monthly_sale) OVER (PARTITION BY product_id,year)) as avg_monthly_Sale
		from
			(
			
			select p.product_id,p.description,p.category,year(td.tran_dt) as year,month(td.tran_dt) as month,sum(td.amt) as monthly_sale
			from product p
			join tran_dtl td on p.product_id=td.product_id
			group by p.product_id,description,category,year(td.tran_dt),month(td.tran_dt)
				 ) s
		)s1;
                
