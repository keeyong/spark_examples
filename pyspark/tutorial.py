from pyspark.sql import SparkSession
from pyspark.sql.functions import col

S3_DATA_INPUT_PATH = 's3://spark-tutorial-dataset/survey_results_public.csv'
S3_DATA_OUTPUT_PATH = 's3://spark-tutorial-dataset/data-output'

spark = SparkSession.builder.appName('Tutorial').getOrCreate()

df = spark.read.csv(S3_DATA_INPUT_PATH, header=True)
print('# of records {}'.format(df.count()))

learnCodeUS = df.where((col('Country') == 'United States of America')).groupby('LearnCode').count()

learnCodeUS.write.mode('overwrite').csv(S3_DATA_OUTPUT_PATH)  # parquet
print('Selected data is successfully saved to S3: {}'.format(S3_DATA_OUTPUT_PATH))
