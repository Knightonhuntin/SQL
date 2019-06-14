Select Time, Station, count(*)
from   ceesmart.hourlydata
group  by Time, Station
having count(*) > 1;
