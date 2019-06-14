CREATE TABLE ceesmart.hourlydata3 LIKE ceesmart.hourlydata;
INSERT INTO ceesmart.hourlydata3 SELECT distinct * FROM ceesmart.hourlydata GROUP BY Time,station;
RENAME TABLE ceesmart.hourlydata TO ceesmart.hourlydataold, ceesmart.hourlydata3 TO ceesmart.hourlydata;
DROP TABLE ceesmart.hourlydataold;