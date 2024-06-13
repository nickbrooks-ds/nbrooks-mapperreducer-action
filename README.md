# nbrooks-mapperreducer-action

Here's my take on the mapper reducer script.

My definition of word: a continous string of characters and possibly apostrophes surrounded by spaces on either side.

**Command Used**
mapred streaming \
  -input /user/sandbox/books \
  -output /user/sandbox/words \
  -mapper mapper.py \
  -reducer reducer.py \
  -file scripts/mapper.py \
  -file scripts/reducer.py

**Dataset Used**
shelley.txt (curl https://raw.githubusercontent.com/cd-public/books/main/pg84.txt -o shelley.txt)
