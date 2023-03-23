#!/bin/bash
# description: Description comes here....

create_docker() {
    # creating docker container d_host1 d_host2 d_host3
    docker run -it -d --name='d_host1' siddharthadmin/ansible-worker-node /bin/bash
    docker run -it -d --name='d_host2' siddharthadmin/ansible-worker-node /bin/bash
    docker run -it -d --name='d_host3' siddharthadmin/ansible-worker-node /bin/bash
}

start_docker() {
    echo " starting docker container"
    for i in d_host1 d_host2 d_host3 ; do
        echo "$i"
        docker start $i
    done
}

stop_docker() {
    echo " stopping docker container"
    for i in d_host1 d_host2 d_host3 ; do
        echo "$i"
        docker stop $i
    done
}

restart_docker() {
    echo " Restarting docker container"
    for i in d_host1 d_host2 d_host3 ; do
        echo "$i"
        docker restart $i
    done
}


ssh_start() {
    echo " ssh_start on docker container"
    for i in d_host1 d_host2 d_host3  ; do
    echo "$i"
    docker exec -it $i  service ssh restart
    done
}

create_inventory() {
    echo "[docker_host]" >> inventory/hosts
    for i in d_host1 d_host2 d_host3  ; do
        echo "$i"
        docker exec -it $i  hostname -i >> inventory/hosts
    done
}

case "$1" in 
    create_docker)
       create_docker
       ;;
    start_docker)
       start_docker
       ;;
    stop_docker)
       stop_docker
       ;;
    restart_docker)
       restart_docker
       ;;
    ssh_start)
        ssh_start
        ;;
    create_inventory)
        create_inventory
        ;;
    *)
       echo "Usage: $0 {create_docker|start_docker|stop_docker|restart_docker|ssh_start|create_inventory}"
esac

exit 0 