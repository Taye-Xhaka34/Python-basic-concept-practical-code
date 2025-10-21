#!/bin/bash

user="Nathan"
pass="2123"
i=1

while [ $i -le 5 ]
do
    echo "Attempt $i of 5"
    read -p "Enter username: " username
    read -p "Enter password: " password

    if [[ "$username" == "$user" ]]; 
    then
        if [[ "$password" == "$pass" ]]; 
        then
            echo "Welcome to GTST Company"
            exit 0
        else
            echo "Incorrect password"
        fi
    else
        echo "Incorrect username"
    fi

    i=$((i+1))
done

echo "Sorry, you are limited."
