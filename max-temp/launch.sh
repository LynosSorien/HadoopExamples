cat measurements.txt | python ./mapper.py | sort -k1,1 | python ./reducer.py
