import subprocess
# subprocess.call('dir', shell=True)
y=subprocess.run('cd ../', shell=True, capture_output=True).stdout
print(y)
