#!/bin/bash

echo " starting docker container"
state=$2

for i in ansible d_host5 d_host3 d_host4 d_host2 ; do
    echo "$i"
    docker restart $i
done
docker $state ansible d_host5 d_host3 d_host4 d_host2 

for i in ansible d_host5 d_host3 d_host4 d_host2 ; do
    echo "$i"
    docker exec -it $i sudo service ssh restart
done

