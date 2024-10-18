select CATEGORY, sum(SALES) as TOTAL_SALES
from BOOK a join BOOK_SALES b on a.BOOK_ID = b.BOOK_ID
where DATE_FORMAT(b.SALES_DATE, "%Y-%m") = "2022-01"
group by CATEGORY
order by CATEGORY;