-- https://www.hackerrank.com/challenges/revising-the-select-query-2/problem
select NAME
from CITY
where
    COUNTRYCODE = 'USA'
    and POPULATION > 120000;