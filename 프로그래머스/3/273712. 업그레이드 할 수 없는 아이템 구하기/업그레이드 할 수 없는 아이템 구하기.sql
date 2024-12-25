select i.ITEM_ID, i.ITEM_NAME, i.RARITY
from ITEM_INFO i right join ITEM_TREE t on i.ITEM_ID = t.ITEM_ID
where t.ITEM_ID 
not in (SELECT DISTINCT(PARENT_ITEM_ID) FROM ITEM_TREE where PARENT_ITEM_ID is not null)
order by i.ITEM_ID desc;