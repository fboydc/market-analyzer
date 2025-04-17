CREATE DATABASE economic_data
WITH
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.UTF-8'
    LC_CTYPE = 'en_US.UTF-8'
    TEMPLATE = template0;

\connect economic_data;

CREATE TABLE IF NOT EXISTS "events" (
    "id" SERIAL PRIMARY KEY,
    "event_name" VARCHAR(255) NOT NULL,
    "event_time" VARCHAR(255) NOT NULL,
    "event_date" DATE NOT NULL,
    "ranking" INT NOT NULL,
    "country" VARCHAR(50) NOT NULL,
    "actual_value" VARCHAR(50) NOT NULL,
    "forecast_value" VARCHAR(50) NOT NULL
);


