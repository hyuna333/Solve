select DISTINCT CAR_ID, 
(case when exists (
    select 1 from CAR_RENTAL_COMPANY_RENTAL_HISTORY AS sub
    where sub.CAR_ID = main.CAR_ID 
    and "2022-10-16" between sub.START_DATE and sub.END_DATE) then "대여중" 
 else "대여 가능" end) as AVAILABILITY
from CAR_RENTAL_COMPANY_RENTAL_HISTORY as main
order by CAR_ID desc;