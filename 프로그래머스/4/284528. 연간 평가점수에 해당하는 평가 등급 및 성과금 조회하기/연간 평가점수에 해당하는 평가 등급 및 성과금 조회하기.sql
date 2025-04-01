select e.EMP_NO, e.EMP_NAME, 
case when SCORE >= 96 then "S"
     when SCORE >= 90 then "A"
     when SCORE >= 80 then "B"
     else "C" end as GRADE,
case when SCORE >= 96 then e.SAL * 0.2
     when SCORE >= 90 then e.SAL * 0.15
     when SCORE >= 80 then e.SAL * 0.1
     else e.SAL * 0 end as BONUS
from (select AVG(SCORE) as SCORE, EMP_NO from HR_GRADE group by EMP_NO) g 
left join HR_EMPLOYEES e on g.EMP_NO = e.EMP_NO
order by EMP_NO;