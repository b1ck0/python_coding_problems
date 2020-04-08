-- https://leetcode.com/problems/department-highest-salary/
select
    department_table.Name as "Department",
    employee_table.Name as "Employee",
    employee_table.Salary as "Salary"
from Employee as employee_table
join Department as department_table
on employee_table.DepartmentId = department_table.Id
join (
    select
        DepartmentId,
        max(Salary) as "Salary"
    from Employee
    group by DepartmentId
) as max_salary_table
on
    employee_table.DepartmentId = max_salary_table.DepartmentId
and
    employee_table.Salary = max_salary_table.Salary

