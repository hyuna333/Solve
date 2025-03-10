select CART_ID from CART_PRODUCTS where NAME = 'Yogurt'
INTERSECT
select CART_ID from CART_PRODUCTS where NAME = 'Milk'
order by CART_ID;