#!/usr/bin/env bash

kubectl --namespace=search cp ./bl_db_product/obj_detect.py $1:/usr/src/app/bl_db_product/