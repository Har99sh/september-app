FROM postgres
ENV POSTGRES_PASSWORD docker
ENV POSTGRES_USER adminUser
ENV POSTGRES_DB db_just_4_work
COPY clean_dump.sql /docker-entrypoint-initdb.d/

