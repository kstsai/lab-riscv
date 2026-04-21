
qemu-system-riscv64 \
  -machine virt \
  -m 1G \
  -nographic \
  -bios ./opensbi/build/platform/generic/firmware/fw_jump.bin \
  -kernel ./linux/arch/riscv/boot/Image \
  -initrd ./rootfs.cpio.gz \
  -append "console=ttyS0"



