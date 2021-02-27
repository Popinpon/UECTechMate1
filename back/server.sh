#! /bin/bash
trap killall SIGINT

killall(){
    echo 'good bye.'
    kill 0
}

echo 'Start up websocket server.'
node ./server.js &
echo 'Start up twitter server.'
pipenv run python ./twitter.py &
# echo 'Start up youtube server.'
# python ./youtube.py &
echo 'Start up main server.'
pipenv run python ./main.py &

wait
