# SDET for RISC-V realm

You are expected to: 

- Design test frameworks, not just test cases 

- Write production‑grade automation code 

- Understand CPU architecture + software stack 

- Debug issues across software + hardware boundaries 

Key domains: 

- RISC‑V architecture 

- Linux kernel & user space 

- Compiler toolchains 

- QEMU & FPGA-based validation 

- CI/CD automation 

- Performance & regression testing

<pre>
my lab repo riscv/ level 1 directories:
riscv/
riscv/toolchain-validation
riscv/gcc => git submodule add https://github.com/gcc-mirror/gcc.git gcc, for toolchain regression test suites
    TEST_INPUT_FOLDER="/root/riscv/gcc/gcc/testsuite/gcc.c-torture/execute"
riscv/busybox => https://github.com/mirror/busybox.git, for riscv64 minimal linux command lines
riscv/opensbi => https://github.com/riscv-software-src/opensbi.git, for fw_jump.bin in boot up riscv64 kernel in QEUM TCG full software emulator
riscv/linux => git submodule add https://github.com/torvalds/linux.git linux , for riscv64 kernel
    
    make ARCH=riscv defconfig
    make ARCH=riscv CROSS_COMPILE=riscv64-linux-gnu- -j$(nproc)
    #built deiliverable linux/arch/riscv/boot/Image
    #for later argument value
    #    -kernel ./linux/arch/riscv/boot/Image 



riscv/rootfs => for create initrd(ramdisk) for riscv64 based on busybox repo


command line to bring up a riscv64 linux kenel with QEMU TCG (full software emulator) 

qemu-system-riscv64 \
  -machine virt \
  -m 1G \
  -nographic \
  -bios ./opensbi/build/platform/generic/firmware/fw_jump.bin \
  -kernel ./linux/arch/riscv/boot/Image \
  -initrd ./rootfs.cpio.gz \
  -append "console=ttyS0"


</pre>

</pre>
