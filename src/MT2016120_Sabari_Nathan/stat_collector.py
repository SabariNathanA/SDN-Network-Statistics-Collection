import subprocess

complete = subprocess.Popen("ovs-vsctl get Interface s1-eth2 statistics", shell=True, stdout=subprocess.PIPE).stdout.read()

complete = complete[1:(len(complete)-2)]
list = complete.split(',')
print list[0].split('=')[1]