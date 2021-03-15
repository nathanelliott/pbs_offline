# pbs_offline

Ensure mysql client is installed
```
mysql -V
```

Be sure to set local envs
```
export DB_HOST=changeme
export DB_USERNAME=changeme
export DB_PASSWORD=changeme
```
The Database is secured restricting access by IP address. You will need to add the IP of the offline backup server to AWS security group.

Run by calling the following script:
```
python3 backup.py
```
