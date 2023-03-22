#!/bin/bash
# creating docker container d_host1 d_host2 d_host3

for i in d_host1 d_host2 d_host3 ; do
    echo "$i"
    docker run -d --name='$1' siddharthadmin/ansible-worker-node /bin/bash
done

# start/stop  docker container d_host1 d_host2 d_host3
state=$1
echo " $state docker container"
for i in d_host1 d_host2 d_host3 ; do
    echo "$i"
    docker $state $i
done

for i in d_host1 d_host2 d_host3  ; do
    echo "$i"
    docker exec -it $i  service ssh restart
done

