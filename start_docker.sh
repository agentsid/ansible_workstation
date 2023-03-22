#!/bin/bash

echo " starting docker container"
state=$1

for i in ansible d_host5 d_host3 d_host4  ; do
    echo "$i"
    docker $state $i
done

for i in ansible d_host5 d_host3 d_host4  ; do
    echo "$i"
    docker exec -it $i sudo service ssh restart
done

