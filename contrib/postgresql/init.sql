DO $$
BEGIN
   IF EXISTS (
      SELECT FROM pg_catalog.pg_roles
      WHERE  rolname = 'pet_tasks_role') THEN

      RAISE NOTICE 'Role "pet_tasks_role" already exists. Skipping.';
   ELSE
      CREATE ROLE pet_tasks_role WITH
        NOSUPERUSER
        NOCREATEDB
        NOCREATEROLE
        NOINHERIT
        LOGIN
        NOREPLICATION
        NOBYPASSRLS
        CONNECTION LIMIT -1;
      GRANT CREATE ON SCHEMA public TO pet_tasks_role;
      GRANT USAGE ON SCHEMA public TO pet_tasks_role;

      RAISE NOTICE 'Role "pet_tasks_role" created.';
   END IF;
END $$;


DO $$
BEGIN
    IF NOT EXISTS (
        SELECT 1
        FROM pg_catalog.pg_auth_members
        WHERE roleid = (SELECT oid FROM pg_catalog.pg_roles WHERE rolname = 'pet_tasks_role')
          AND member = (SELECT oid FROM pg_catalog.pg_roles WHERE rolname = 'pet_tasks_role')
    ) THEN
        GRANT pet_tasks_role TO pet_tasks_app;
        RAISE NOTICE 'Role ''%'' granted to ''%''.', 'pet_tasks_role', 'pet_tasks_app';
    ELSE
        RAISE NOTICE 'Role ''%'' already granted to ''%''.', 'pet_tasks_role', 'pet_tasks_appe';
    END IF;
END $$;

set role 'pet_tasks_role';

create table users(
    id BIGSERIAL PRIMARY KEY,
    name VARCHAR,
    email VARCHAR,
    created_at TIMESTAMPTZ default current_timestamp not null,
    UNIQUE(email)
);