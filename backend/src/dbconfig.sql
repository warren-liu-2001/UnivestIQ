CREATE DATABASE IF NOT EXISTS defaultdb;

USE defaultdb;

CREATE USER IF NOT EXISTS users;
GRANT CREATE ON DATABASE defaultdb TO users;


DROP SCHEMA IF EXISTS warrenschema CASCADE;
CREATE SCHEMA warrenschema AUTHORIZATION warren;
GRANT USAGE ON SCHEMA warrenschema TO uofthax8hack;


CREATE TABLE defaultdb.warrenschema.userinfo (
                                                 userid INT,
                                                 name STRING,
                                                 email STRING,
                                                 password STRING
);
