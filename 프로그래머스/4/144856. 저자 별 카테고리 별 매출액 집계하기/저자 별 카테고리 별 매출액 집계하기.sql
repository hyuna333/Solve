select a.AUTHOR_ID, a.AUTHOR_NAME, b.CATEGORY, sum(s.SALES*b.PRICE) as TOTAL_SALES
from BOOK_SALES s inner join BOOK b on s.BOOK_ID = b.BOOK_ID
inner join AUTHOR a on a.AUTHOR_ID = b.AUTHOR_ID
where s.SALES_DATE BETWEEN '2022-01-01' AND '2022-01-31'
group by a.AUTHOR_ID, b.CATEGORY
order by a.AUTHOR_ID, b.CATEGORY desc;