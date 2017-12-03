import subprocess
import mysql.connector
import signal
import time

#MySQL connection setup
mysql_cnx = mysql.connector.connect(user='root', password='password',host='192.168.56.1',database='UG_DB')

run = True

#Signal handling for graceful exit of program
def signal_handler(signal, frame):
    global run
    print "...Exiting sniff mode..."
    run = False
signal.signal(signal.SIGINT, signal_handler)

# MySQL cursor -> aids insert
cursor = mysql_cnx.cursor()
add_ipsoc = ("INSERT INTO stats (Collisions,  RX_Bytes, RX_CRC_Errors, RX_Dropped, RX_Frame_Error, RX_Over_Error, RX_Packets, TX_Bytes, TX_Dropped, TX_Error, TX_Packets) VALUES (%(coll)s,%(rb)s,%(rcrc)s,%(rd)s,%(rfe)s,%(roe)s,%(rp)s,%(tb)s,%(td)s,%(te)s,%(tp)s)")

complete = subprocess.Popen("ovs-vsctl get Interface s1-eth2 statistics", shell=True, stdout=subprocess.PIPE).stdout.read()

complete = complete[1:(len(complete)-2)]
list = complete.split(',')
coll = list[0].split('=')[1]
rb = list[1].split('=')[1]
rcrc = list[2].split('=')[1]
rd = list[3].split('=')[1]
rfe = list[4].split('=')[1]
roe = list[5].split('=')[1]
rp = list[6].split('=')[1]
tb = list[7].split('=')[1]
td = list[8].split('=')[1]
te = list[9].split('=')[1]
tp = list[10].split('=')[1]
data_ipsoc = {'coll': coll, 'rb': rb, 'rcrc': rcrc,'rd': rd,'rfe':rfe,'roe':roe,'rp':rp,'tb':tb,'td':td,'te':te,'tp':tp}
cursor.execute(add_ipsoc,data_ipsoc)
mysql_cnx.commit()
print "start wait"
time.sleep(5)
print "Done da Sabari Nathaaaa"

cursor.close()
mysql_cnx.close()