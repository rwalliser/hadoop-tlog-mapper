#!/bin/bash

hdfs dfs -rm -R -skipTrash /public/migros/tlog/xml/new/output


hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming-2.2.0.2.0.6.0-76.jar \
-input /public/migros/tlog/xml/new/input \
-output /public/migros/tlog/xml/new/output \
-file ./mapreduce/Mapper.py \
-file ./mapreduce/Trx.py \
-mapper Mapper.py  \
-numReduceTasks 0 \
