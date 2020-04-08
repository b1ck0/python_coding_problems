-- https://leetcode.com/problems/second-highest-salary/
select
    (select distinct
            Salary
        from
            Employee
        order by Salary desc
        LIMIT 1 OFFSET 1) AS SecondHighestSalary
;