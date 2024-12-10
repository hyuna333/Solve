select i.ID, n.FISH_NAME, i.LENGTH
from FISH_INFO i join FISH_NAME_INFO n on i.FISH_TYPE = n.FISH_TYPE
WHERE i.LENGTH = (
    SELECT MAX(LENGTH) 
    FROM FISH_INFO 
    WHERE FISH_TYPE = i.FISH_TYPE)
order by i.ID;