import sys
from pyspark import SparkContext
from pyspark import SparkConf



if __name__ == "__main__":
	if len(sys.argv) < 2:
		 print("Usage: WordCount.py <file>")
		 exit(-1)

	sconf = SparkConf().setMaster("local[2]").setAppName("mycode")
	sc = SparkContext(conf=sconf)
# Set logging level to WARN to avoid distracting INFO messages in demos
	sc.setLogLevel("WARN")

	counts = sc.textFile(r'C:\Users\Krishna\data\purplecow.txt').flatMap(lambda line: line.split(' ')).map(lambda w: (w,1)).reduceByKey(lambda v1,v2: v1+v2)
	for pair in counts.collect():
		print(pair)
	sc.stop()
