#!/bin/bash

for i in `seq 3 8`;
do
	next=$(($i + 1))
	twitterscraper adventofcode -bd 2017-12-0$i -ed 2017-12-0$next -o tweets_$i.json
done

twitterscraper adventofcode -bd 2017-12-09 -ed 2017-12-10 -o tweets_9.json

for i in `seq 10 30`;
do
	next=$(($i + 1))
	twitterscraper adventofcode -bd 2017-12-$i -ed 2017-12-$next -o tweets_$i.json
done    
