
import os
import subprocess
import re

TEST_INPUT_FOLDER="/root/riscv/gcc/gcc/testsuite/gcc.c-torture/execute"


def newProcCompile(cfil,optX="2"):

    import time

    aoutFil = os.path.basename(cfil).replace('.c','.a.out')
    optLevel = f"-O{optX}"
    cmd = [
        "riscv64-linux-gnu-gcc",  
        f"{optLevel}",  
        "-static",
        "-march=rv64imafdc",
        "-mabi=lp64d",
        f"{cfil}",
        "-o", f"{aoutFil}"
    ]

    print(cmd)
    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True
    )

    boot_ok = False
    start = time.time()

    line = proc.stdout.readline()
    while line:

        print(line.strip())
        if "Hello from RISC-V" in line:
            boot_ok = True
            break
        line = proc.stdout.readline()

    proc.terminate()

    if boot_ok:
        print("✅ Boot test PASS")
    else:
        print("❌ Boot test FAIL")

def chainCompileRunInSingleShell(cfil,optX="2"):

    aoutFil = os.path.basename(cfil).replace('.c','.a.out')

    try:
        os.popen("rm -f *.a.out").read()
    except:
        pass

    cmdExtractCompileOpt = 'cat ' + cfil + ' | egrep "dg-*"'
    result = subprocess.run(cmdExtractCompileOpt, shell=True, capture_output=True, text=True)
    print(result.stdout)
    matches = re.findall(r'.*options.*"(.*)"', result.stdout, re.MULTILINE)
    if matches:
        print(matches[0])

    optLevel = f"-O{optX}"
    cmdSplitted = [
        "riscv64-linux-gnu-gcc",  
        f"{optLevel}",  
        "-static",
        "-march=rv64imafdc",
        "-mabi=lp64d",
        f"{cfil}",
        "-o", f"{aoutFil}"
    ]

    if matches:
        cmdSplitted.append(matches[0]) 
    
    # Run both with conditional execution
    full_cmd = f"{' '.join(cmdSplitted)} && qemu-riscv64 {aoutFil}"
    result = subprocess.run(
        full_cmd,
        shell=True,  # Required for && operator
        capture_output=True,
        text=True
    )
    #print(f"compile and run {cfil} exit code: {result.returncode}")
    if result.returncode:
        print(f"compile and run {full_cmd}")

    # print(f"Output: {result.stdout}")
    return result.returncode


if __name__ == "__main__":

    tested = 0
    needToCheck = 0
    for f in os.listdir(TEST_INPUT_FOLDER):
        rc = 0
        cfil = ""
        if f.endswith(".c"):
            cfil=os.path.join(TEST_INPUT_FOLDER,f)
            rc = chainCompileRunInSingleShell(cfil=cfil,optX="2")
            tested += 1
        if rc and cfil != "":
            #full_cmd = 'cat ' + cfil + ' | egrep "dg-*"'
            #result = subprocess.run(full_cmd, shell=True, capture_output=True, text=True)
            #print(result.stdout)
            needToCheck += 1 
            

        if tested > 2000:
            break

    print(f"rc non-zero case count {needToCheck} among tested {tested} cases ") 
    try:
        os.popen("rm -f *.a.out").read()
    except:
        pass
