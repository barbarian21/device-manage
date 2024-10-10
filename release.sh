#!/bin/bash
git pull
docker restart 98ea04572e4f
docker exec -it 98ea04572e4f /bin/bash -c "cd /root/MaterialVisual/ && uwsgi --ini uwsgi/uwsgi.ini && /etc/init.d/nginx restart"
