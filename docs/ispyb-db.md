# Installing the unit test database

Assuming you have root access e.g. with root password in your .my.cnf file:

mysql -u root -e "set global log_bin_trust_function_creators=ON;"
mysql -u root < conf/schema.sql
