# Write your MySQL query statement below
select distinct person1.email from Person person1,Person person2 where person1.email = person2.email and person1.id > person2.id;