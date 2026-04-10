#!/bin/bash

sudo apt update
sudo apt install -y \
  qemu-system-misc \
  qemu-utils \
  gcc-riscv64-linux-gnu \
  binutils-riscv64-linux-gnu \
  build-essential \
  device-tree-compiler \
  git \
  python3 python3-pip \
  flex bison    \
  libncurses-dev libncursesw5-dev libtinfo-dev pkg-config \
  qemu-user qemu-user-static


#確認： 
qemu-system-riscv64 --version 
qemu-system-riscv64 -bios 
  
