#!/bin/bash

riscv64-linux-gnu-gcc   \
  -O2  \
  -static  \
  -march=rv64imafdc  \
  -mabi=lp64d  \
  minimal_add.c  \
  -o add_gcc 

qemu-riscv64 ./add_gcc
echo $?
