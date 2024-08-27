-- setup_database.sql
-- Connect to the PostgreSQL instance as a superuser
-- CREATE DATABASE
CREATE DATABASE mba_db;

-- Create a new user
CREATE USER your_user WITH PASSWORD 'your_password';

-- Grant all privileges on the database to the new user
GRANT ALL PRIVILEGES ON DATABASE mba_db TO your_user;

-- Connect to the new database and grant privileges on the public schema
\c mba_db
GRANT ALL PRIVILEGES ON SCHEMA public TO your_user;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO your_user;
GRANT pg_read_server_files TO your_username;