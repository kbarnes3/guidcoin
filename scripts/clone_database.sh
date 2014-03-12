#!/bin/bash
dropdb guidcoin_staging
createdb --locale en_US.UTF-8 --encoding UTF8 --template template0 guidcoin_staging
pg_dump --format=custom guidcoin_prod > guidcoin_prod.dump
pg_restore --dbname=guidcoin_staging guidcoin_prod.dump
rm guidcoin_prod.dump
echo guidcoin_prod copied to guidcoin_staging!

