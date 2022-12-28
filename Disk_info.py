from subprocess import check_output as sbp
disk_name = (sbp('wmic logicaldisk get deviceid', shell=True).decode())
disk_size = (sbp('wmic logicaldisk get size', shell=True).decode())
boot_drive = (disk_name.splitlines()[2].strip()) + " " + disk_size.splitlines()[2]
print(boot_drive)