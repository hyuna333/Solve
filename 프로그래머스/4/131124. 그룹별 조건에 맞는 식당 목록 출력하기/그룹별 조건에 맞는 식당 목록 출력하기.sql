select p.MEMBER_NAME, r.REVIEW_TEXT, 
date_format(r.REVIEW_DATE, '%Y-%m-%d') as REVIEW_DATE
from (select * from REST_REVIEW
where MEMBER_ID = (select MEMBER_ID from REST_REVIEW
group by MEMBER_ID order by count(*) desc limit 1)) r 
join MEMBER_PROFILE p on p.MEMBER_ID = r.MEMBER_ID
order by r.REVIEW_DATE, r.REVIEW_TEXT;


