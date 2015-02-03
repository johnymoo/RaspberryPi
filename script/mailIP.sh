#! /bin/sh
# /etc/init.d/mailIP
### BEGIN INIT INFO
# Provides:          mailIP
# Required-Start:   
# Required-Stop:     
# Default-Start:     2 3 4 5
# Default-Stop:      0 1 6
# Short-Description: Start/stops the mailIP
# Description:       Start/stops the mailIP
# sudo update-rc.d /etc/init.d/mailIP 2 3 4 5
### END INIT INFO
 
case "$1" in
  start)
	  echo "Starting mailIP"
	  # run application you want to start
	  python /usr/local/sbin/mailIP.py &
	  ;;
  stop)
	echo "Stopping example"
	# kill application you want to stop
	killall python
	;;
  *)
	  echo "Usage: /etc/init.d/mailIP {start|stop}"
	  exit 1
	  ;;
esac
										   
exit 0
