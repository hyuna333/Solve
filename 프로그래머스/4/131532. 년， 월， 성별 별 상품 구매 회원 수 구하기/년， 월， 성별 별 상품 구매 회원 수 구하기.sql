select YEAR(s.SALES_DATE) as YEAR, MONTH(s.SALES_DATE) as MONTH, 
i.GENDER, count(distinct s.USER_ID) as USERS
from ONLINE_SALE s join USER_INFO i on s.USER_ID = i.USER_ID
where i.gender is not null
group by YEAR(s.SALES_DATE), MONTH(s.SALES_DATE), i.GENDER
order by YEAR, MONTH, GENDER;