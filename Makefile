# Recreate database
recreatedb:
	export PGPASSWORD=trusted_user_password  && \
	psql -h localhost -U trusted_user -d postgres -c 'drop DATABASE IF EXISTS "dev_db"' && \
	psql -h localhost -U trusted_user -d postgres -c 'create DATABASE "dev_db" owner trusted_user'  && \
	psql -h localhost -U trusted_user -d postgres -c 'drop DATABASE IF EXISTS "test_db"' && \
	psql -h localhost -U trusted_user -d postgres -c 'create DATABASE "test_db" owner trusted_user' && \
	hatch run migrate
