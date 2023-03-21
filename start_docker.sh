#!/bin/bash

echo " starting docker container"

docker start ansible d_host7  d_host6 d_host5 d_host3 d_host4 d_host2 d_host1

for i in ansible d_host7  d_host6 d_host5 d_host3 d_host4 d_host2 d_host1; do
    echo "$i"
    docker exec -it $i sudo service ssh restart
done

