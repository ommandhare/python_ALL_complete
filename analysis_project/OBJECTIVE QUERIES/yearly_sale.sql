select * from tran_dtl;



select year(tran_dt) as per_year,concat(round(sum(amt)),"$")as yearly_sale from tran_dtl
group by per_year
order by per_year desc
;
