-- Create a user
CREATE USER 'pipeline'@'%' IDENTIFIED BY 'XXX#';

-- Create a database
CREATE DATABASE pipelinedb
CHARACTER
SET utf8mb4
COLLATE utf8mb4_general_ci;

-- Grant privileges to the user on the database
GRANT ALL PRIVILEGES ON pipelinedb.* TO 'pipeline'@'%';

-- Note the endpoint (For your reference)

-- Save data from filtering
-- Create a table
CREATE TABLE channel_marketing_tb
(
    serviceType VARCHAR(50) NULL,
    gtmLongTime VARCHAR(200) NULL,
    base_dt VARCHAR(200) NULL,
    channel_name VARCHAR(200) NULL,
    conversion_name VARCHAR(200) NULL,
    platform VARCHAR(200) NULL,
    user_type VARCHAR(200) NULL
);
