# Spark

[link](https://www.toptal.com/spark/introduction-to-apache-spark)

## idea:

upon ***RDD (Resilient Distributed Dataset)***, an ***immutable fault-tolerant, distributed*** collection of objects that can be operated on ***in parallel.***


RDD:

- ***Transformations*** are operations (such as map, filter, join, union, and so on) that are performed on an RDD and which yield a new RDD containing the result.

- ***Actions*** are operations (such as reduce, count, first, and so on) that return a value after running a computation on an RDD.

## features




1. simple
```

sparkContext.textFile("hdfs://...")
            .flatMap(line => line.split(" "))
            .map(word => (word, 1)).reduceByKey(_ + _)
            .saveAsTextFile("hdfs://...")


```
2. real time processing of streaming data, such as ***production web server log files (e.g. Apache Flume and HDFS/S3)***, ***social media like Twitter,*** and various ***messaging queues*** like Kafka.

3. memory management and fault recovery

4. scheduling, distributing and monitoring jobs on a cluster

5. Integrates well with the Hadoop ecosystem and data sources (HDFS, Amazon S3, Hive, HBase, Cassandra, etc.)

> querying data via SparkSQL or Hive

> real time processing of streaming data, such as production web server log files (e.g. Apache Flume and HDFS/S3), social media like Twitter, and various messaging queues like Kafka.

![](/SystemDesign/pics/spark-streaming.webp)

## fault tolerance

1. wide dependencies

## use case

Twitter earthquake

1/ Spark: filter tweets which seem relevant like “earthquake” or “shaking”.
```
TwitterUtils.createStream(...)
            .filter(_.getText.contains("earthquake") || _.getText.contains("shaking"))

```
2/ support vector machine (SVM) to determine relevance

```
// Run training algorithm to build the model
val numIterations = 100
val model = SVMWithSGD.train(training, numIterations)

// Clear the default threshold.
model.clearThreshold()

// Compute raw scores on the test set.
val scoreAndLabels = test.map { point =>
  val score = model.predict(point.features)
  (score, point.label)
}

// Get evaluation metrics.
val metrics = new BinaryClassificationMetrics(scoreAndLabels)
val auROC = metrics.areaUnderROC()

println("Area under ROC = " + auROC)
```
