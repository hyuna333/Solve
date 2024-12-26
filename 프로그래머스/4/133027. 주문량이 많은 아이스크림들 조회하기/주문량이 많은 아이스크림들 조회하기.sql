select h.FLAVOR
from FIRST_HALF h join 
(select SHIPMENT_ID, FLAVOR, sum(TOTAL_ORDER) as TOTAL_ORDER from JULY
group by FLAVOR) j 
on h.FLAVOR = j.FLAVOR
order by h.TOTAL_ORDER + j.TOTAL_ORDER desc
limit 3;