select CAR_TYPE, count(*) as CARS
from CAR_RENTAL_COMPANY_CAR
WHERE FIND_IN_SET('통풍시트', OPTIONS) > 0
   OR FIND_IN_SET('열선시트', OPTIONS) > 0
   OR FIND_IN_SET('가죽시트', OPTIONS) > 0
group by CAR_TYPE
order by CAR_TYPE;