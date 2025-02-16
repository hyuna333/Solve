select f.CATEGORY, f.PRICE as MAX_PRICE, f.PRODUCT_NAME
from FOOD_PRODUCT f join (select CATEGORY, max(PRICE) as MAX_PRICE
from FOOD_PRODUCT
where CATEGORY in ("과자", "국", "김치", "식용유")
group by CATEGORY) j 
on f.CATEGORY = j.CATEGORY and f.PRICE = j.MAX_PRICE
where f.CATEGORY in ("과자", "국", "김치", "식용유")
order by MAX_PRICE desc;