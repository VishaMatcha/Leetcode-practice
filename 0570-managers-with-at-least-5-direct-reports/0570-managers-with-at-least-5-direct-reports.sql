# Write your MySQL query statement below
select e.name
from (select managerId as i, count(*) as c from employee group by managerId) as t,
employee e
where e.id = t.i and t.c >= 5;