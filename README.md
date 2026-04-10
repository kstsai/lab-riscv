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
riscv/gcc =>  https://github.com/gcc-mirror/gcc.git, for toolchain regression test suites
riscv/busybox => https://github.com/mirror/busybox.git, for riscv64 minimal linux command lines
riscv/opensbi => https://github.com/riscv-software-src/opensbi.git, for fw_jump.bin in boot up riscv64 kernel in QEUM TCG full software emulator
riscv/linux => https://github.com/torvalds/linux.git , for riscv64 kernel
riscv/rootfs => for create initrd(ramdisk) for riscv64 based on busybox repo
</pre>

</pre>
