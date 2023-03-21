#!/bin/bash

echo="This shell script is for ssh-setup for docker container"
host=$1
ssh-copy-id -i ~/.ssh/id_rsa.pub ansible@$host
