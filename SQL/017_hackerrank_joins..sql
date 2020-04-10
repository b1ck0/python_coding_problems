-- https://www.hackerrank.com/challenges/african-cities/problem
select city.name
from city
inner join country on city.countrycode = country.code
where country.continent = 'Africa'

-- https://www.hackerrank.com/challenges/average-population-of-each-continent/problem
select
    country.continent,
    floor(avg(city.population))
from country
inner join city on city.countrycode = country.code
group by country.continent;

-- https://www.hackerrank.com/challenges/the-report/problem
select
    student.name,
    student.marks,
    grades.grade
from students
inner join grades on 