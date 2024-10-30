# imports
from pyspark import SparkSession
from config.config import configuration

# Check if the script is being run directly (not imported as a module).
if __name__ == "__main__":

    # Start building a new SparkSession
    # and set the application name to 'AWS_Spark_Unstructured'.
    spark = (SparkSession.builder.appName('AWS_Spark_Unstructured')
             # Specify the necessary Hadoop and AWS packages for S3 integration.
             .config('spark.jars.packages', 
                     'org.apache.hadoop:hadoop-aws:3.3.1',
                     'com.amazonaws:aws-java-sdk:1.11.469',)
             # Specify the S3 filesystem implementation that Spark will use.
             .config('spark.hadoop.fs.s3.impl', 'org.apache.hadoop.fs.s3a.S3AFileSystem')
             # Set the AWS access key, obtained from the configuration variable.
             .config('spark.hadoop.fs.s3a.access.key', configuration.get('AWS_ACCESS_KEY'))
             # Set the AWS secret key, obtained from the configuration variable.
             .config('spark.hadoop.fs.s3a.secret.key', configuration.get('AWS_SECRET_KEY'))
             # Define the AWS credentials provider to be used.
             .config('spark.hadoop.fs.s3a.aws.credentials.provider',
                     'org.apache.hadoop.fs.s3a.SimpleAWSCredentialsProvider')
             .getOrCreate()
             )