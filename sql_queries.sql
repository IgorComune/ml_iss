-------------------------------------------
-- creating the table

CREATE TABLE public.iss_table
(
    name char (50) NOT NULL,
    id char (50) NOT NULL,
    latitude char (50) NOT NULL,
    longitude char (50) NOT NULL,
    altitude char (50) NOT NULL,
    velocity char (50) NOT NULL,
    visibility char (50) NOT NULL,
    footprint char (50) NOT NULL,
    "timestamp" char (50) NOT NULL,
    daynum char (50) NOT NULL,
    solar_lat char (50) NOT NULL,
    solar_lon char (50) NOT NULL,
    units char (50) NOT NULL
);

ALTER TABLE IF EXISTS public.iss_table
    OWNER to postgres;

---------------------------------------------
-- checking the table
select * from iss_table