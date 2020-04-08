-- https://leetcode.com/problems/customers-who-never-order/
select
    Name as Customers
from Customers
where Customers.Id not in (select DISTINCT(CustomerId) from Orders)