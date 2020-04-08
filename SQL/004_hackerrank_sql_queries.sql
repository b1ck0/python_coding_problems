-- https://www.hackerrank.com/challenges/weather-observation-station-3/problem
select
    distinct(CITY)
from STATION
where
    mod(ID,2)=0;