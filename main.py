from pyspark import SparkConf, SparkContext

conf = (SparkConf()
         .setMaster("local[*]")
         .setAppName("My example app")
         .set("spark.executor.memory", "1g"))
sc = SparkContext(conf = conf)

rdd1 = sc.textFile("data/La divina commedia.txt")
rdd2 = rdd1.flatMap(lambda x: x.split(" "))
rdd3 = rdd2.map(lambda x: x.lower())
rdd4 = rdd3.map(lambda x: x.replace("'", "").replace(".", "").replace("!", "").replace("?", "").replace(":", ""))
rdd5 = rdd4.map(lambda x: (x, 1))
rdd6 = rdd5.reduceByKey(lambda x, y: x + y)
rdd7 = rdd6.map(lambda x: (x[1], x[0]))
rdd8 = rdd7.sortByKey(False)



