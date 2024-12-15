select e.DEPT_ID, d.DEPT_NAME_EN, round(avg(e.SAL)) as AVG_SAL
from HR_EMPLOYEES e join HR_DEPARTMENT d on e.DEPT_ID = d.DEPT_ID
group by DEPT_ID
order by AVG_SAL desc;