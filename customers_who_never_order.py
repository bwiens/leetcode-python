# Write your MySQL query statement below
select Name as Customers from Customers where ID not in (select CustomerId from Orders);
