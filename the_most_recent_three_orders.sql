SELECT a.NAME AS customer_name, 
       a.customer_id, 
       b.order_id, 
       b.order_date 
FROM   customers AS a 
       JOIN orders AS b 
         ON a.customer_id = b.customer_id 
WHERE  (SELECT Count(*) 
        FROM   orders AS c 
        WHERE  b.customer_id = c.customer_id 
               AND b.order_date < c.order_date) <= 2 
ORDER  BY customer_name, 
          customer_id, 
          order_date DESC; 
