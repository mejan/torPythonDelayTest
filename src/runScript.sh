#! /bin/bash

# 10 minutes in seconds for running
# the tests only once every 10 minute.
waitTime=600
# One week in seconds to stop measure after
# one week time.
endTime=604800
# to keep track of total time.
timePast=0

while [ $timePast -le $endTime ]; do
	# Reset the second counter.
	SECONDS=0

	#### Running Tor-based scripts. ####
	# The "&" says the script should be run
	# in another session.
	python hiddenService.py &
	# Sleep to give the service time to setup
	# properly.
	sleep 2m
	python hiddenClient.py
	# Stop the service.
	pkill python

        #Sleep for easlier determine the traffic in wireshark.
        sleep 1m

	#### Running non-Tor scripts. ####
	# The "&" says the script should be run
	# in another session.
	python service.py &
	# Sleep to give the service time to setup
	# properly.
	sleep 1 #in this case it is only a "safty" because it might be needed.
	python client.py
	# Stop the service.
	pkill python

	# Making sure we'll only measure
	# every 10 minutes.
	rerun=$((waitTime-SECONDS))
	while [ $rerun -ge 0 ]; do
		# echo "$rerun s until rerun."
		rerun=$((waitTime-SECONDS))
	done
	# Add the past time to the total time.
	let "timePast += $SECONDS"
done
# For testing purposes.
echo "The time past is: $timePast"
