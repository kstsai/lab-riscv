cat <<EOF | kubectl apply -f -
apiVersion: kubevirt.io/v1
kind: VirtualMachine
metadata:
  name: test-vm
spec:
  running: true
  template:
    metadata:
      labels:
        kubevirt.io/domain: test-vm
    spec:
      domain:
        cpu:
          cores: 1
        resources:
          requests:
            memory: 1Gi
        devices:
          disks:
          - name: containerdisk
            disk:
              bus: virtio
          - name: cloudinitdisk
            disk:
              bus: virtio
      volumes:
      - name: containerdisk
        containerDisk:
          image: quay.io/kubevirt/cirros-container-disk-demo
      - name: cloudinitdisk
        cloudInitNoCloud:
          userData: |
            #cloud-config
            password: cirros
            chpasswd: { expire: False }
EOF
