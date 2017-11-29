sudo dhclient eth1

# Scapy v2.3.3
wget https://pypi.python.org/packages/ac/14/c792a14b9f8bc4bb9c74c0594c167a2da36e31964098d9e27202142cbd7d/scapy-2.3.3.tgz#md5=65939356f08760ebef836796d3320b3bA

 tar -xvzf scapy-2.3.3.tgz
 
 cd scapy-2.3.3/
 
 sudo python setup.py install

# Dependancies for Scapy
sudo apt-get install python-dev tcpdump graphviz imagemagick python-pip

pip install numpy

pip install pycrypto

# mysql-connector
wget http://dev.mysql.com/get/Downloads/Connector-Python/mysql-connector-python-2.1.7.tar.gz

tar -xf mysql-connector-python-2.1.7.tar.gz

cd mysql-connector-python-2.1.7

sudo python setup.py install

# Granting access to Mininet to access MySQL
Go to mysql cnf file and commnt out the line saying binding the mysql to localhost.

Restart server.

Inside the mysql terminal 
    - CREATE USER 'root'@'%' IDENTIFIED BY 'password';
    - GRANT ALL PRIVILEGES ON *.* TO 'root'@'%';
    - FLUSH PRIVILEGES;
-------------DO------NOT-------RESTART------------