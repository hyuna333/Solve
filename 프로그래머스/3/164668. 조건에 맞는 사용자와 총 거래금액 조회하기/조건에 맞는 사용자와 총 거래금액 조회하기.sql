select u.USER_ID, u.NICKNAME, b.TOTAL_SALES
from (
select WRITER_ID, sum(PRICE) as TOTAL_SALES 
from USED_GOODS_BOARD where STATUS = "DONE"
group by WRITER_ID having sum(PRICE) >= 700000) as b join USED_GOODS_USER u
on u.USER_ID = b.WRITER_ID
order by TOTAL_SALES;