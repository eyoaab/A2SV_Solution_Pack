# Write your MySQL query statement below
select name 
from Employee
where id in (
 select managerid from Employee
 group by managerid
 having count(managerid) >= 5
);