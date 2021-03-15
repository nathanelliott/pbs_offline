import os
# from subprocess import Popen, PIPE
import subprocess

varpass = True
env_vars = {
    "DB_HOST",
    "DB_USERNAME",
    "DB_PASSWORD"
}
for var in env_vars:
    if os.getenv(var) is None:
        print(f'\033[91m' + f"Missing environment variable: {var}" + '\033[0m')
        varpass = False
if varpass == False:
    print("Cannot continue with backup")
    exit()

print("starting backup")



mysql_connect = f'mysql -h {os.getenv("DB_HOST")} -P 3306 -u {os.getenv("DB_USERNAME")} -p\'{os.getenv("DB_PASSWORD")}\' -D {os.getenv("DB_NAME")}'
mysql_dump = f'mysqldump --column-statistics=0 -h {os.getenv("DB_HOST")} -P 3306 -u {os.getenv("DB_USERNAME")} -p\'{os.getenv("DB_PASSWORD")}\' --set-gtid-purged=OFF --all-databases --triggers --routines --events > `date +%d_%b_%Y_%H_%M_%S`.sql'
print("backing up database...")
subprocess.Popen(mysql_dump, shell=True).communicate()



print("completed backup")

