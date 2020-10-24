ps aux | grep break | awk '{print $2}' | xargs kill -9
