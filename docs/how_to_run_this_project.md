- Create a sample (akila) database and insert sample data using attached sql script

sql-server-sakila-insert-data.sql

sql-server-sakila-schema.sql

- Install and configure (source and destination) Airbyte on Windows using the link below:
https://medium.com/@akashsinghal14_31618/how-to-get-started-with-airbyte-windows-b0a1c84feff1

- Configure dbt profile.yml file to point to the destination database

- Spin up the docker containers from the images specified in docker-compose.yml and Dockerfile files.

- Build the images

$ docker compose build --no-cache

- Run the containers

$ docker compose up

- Create an Airbyte sync connection to copy data from the source to the desination database, copy the connection id and add to the airbyte sync dag

![image](https://github.com/user-attachments/assets/9cf194ee-e0f8-4086-a266-2ee6b4b936e8)

- Create an airbyte connection under the admin menu, add the host, port and connection credential of airbyte
