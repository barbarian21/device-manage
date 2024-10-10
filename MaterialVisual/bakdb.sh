#!/bin/bash
#Luther 2020/4/13
#back up ats 66 server db to another server

time=`date '+%Y-%m-%d %H:%M:%S'`
log=/var/log/backdb.log
logBegin="[${time}]"
bakdir=/bak/mysqlbak

#clear log if the log file modify time > 7 day
clearLog(){

    logPath=${1}
    if [ ! -f $logPath ];then
        "$logBegin log file does not exist" >> $logPath
    else
        oldTime=`stat -c %Y $log`
        currTime=`date +%s`
        deltaTime=`expr $currTime - $oldTime`
        if [ $deltaTime -gt 604800 ];then
            > $logPath
        fi
    fi
}

clearLog ${log}

#if not exist back up dir,create it
if [ ! -d $bakdir ];then
    mkdir -p $bakdir
    echo "${logBegin} mkdir ${bakdir}" >> $log
else
    echo "$logBegin bak dir exist" >> $log
fi

user="root"
passwd="root"
backTime=`date +%Y%m%d%H`

echo "$logBegin start back $backTime database" >> $log
#back all databases
/usr/bin/mysqldump -u $user -p$passwd -h 10.12.120.200 -P 8084 --all-databases > $bakdir/$backTime.sql

backList=`ls ${bakdir}`
echo "$logBegin back dir files:$backList" >> $log

#clear 7 days ago backs
find $bakdir -name "*.sql" -type f -mtime +7 -exec rm {} \; > /dev/null 2>&1

clearList=`ls ${bakdir}`
echo "$logBegin after clear:$clearList" >> $log

echo "$logBegin end back $backTime database" >> $log

