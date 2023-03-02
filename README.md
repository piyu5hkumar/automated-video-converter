# automated-video-converter
A python script that will automatically convert .webm file to mp4 | watchdog | Ubuntu
  

## install supervisor
**sudo apt-get install supervisor -y**


## creating supervisor conf for the script
 **sudo gedit /etc/supervisor/conf.d/automated-video-converter.conf**
 - *paste the following with proper paths*

[program:automated-video-converter]
command=*{path to your env}*/bin/python3 *{path to your script}*/script.py
autostart=true
autorestart=true
stderr_logfile=/var/log/automated-video-converter.err.log
stdout_logfile=/var/log/automated-video-converter.out.log


## make supervisor recognise your conf
**sudo supervisorctl reread**
- output => **automated-video-converter: available**


## Add your conf process group
**sudo supervisorctl update**
- output => **automated-video-converter: added process group**

## Check if your script is running
**sudo supervisorctl**
output => **automated-video-converter        RUNNING   pid 22788, uptime 0:20:45**

## Logs
- your stderr_logfile will be /var/log/automated-video-converter.err.log(you can edit this in the conf file)
- your stdout_logfile will be /var/log/automated-video-converter.out.log(you can edit this in the conf file)
- you can also use tail -f for better output. ex => **tail -f /var/log/automated-video-converter.out.log**

## More commands
 - sudo supervisorctl start <process_name>
 - sudo supervisorctl stop <process_name>
 - sudo supervisorctl restart <process_name>
 - sudo supervisorctl stop all