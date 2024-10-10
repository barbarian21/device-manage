#!/bin/bash
logfile="/workspace/build.log"
echo "==============================================" >> $logfile
node --version >> $logfile
npm --version >> $logfile
cd /workspace/
echo "Start install packages" >> $logfile
npm install >> $logfile
echo "End install pacakges" >> $logfile

echo "Start build project" >> $logfile
npm run build:prod >> $logfile
echo "End build project" >> $logfile
echo "==============================================" >> $logfile
