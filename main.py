# imports
from pyspark import SparkSession
from pyspark.sql.types import StructType, StructField, StringType, DoubleType, DateType
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

csv_input_dir = 'file:///home/v11s3rkr/repos/aws_spark/input/input_csv'
img_input_dir = 'file///home/v11s3rkr/repos/aws_spark/input/input_img'
json_input_dir = 'file///home/v11s3rkr/repos/aws_spark/input/input_json'
pdf_input_dir = 'file///home/v11s3rkr/repos/aws_spark/input/input_pdf'
video_input_dir = 'file///home/v11s3rkr/repos/aws_spark/input/input_video'
text_input_dir = 'file///home/v11s3rkr/repos/aws_spark/input/inut_text'

data_schema = StructType([
    StructField(name: 'file_name', StringType(), nullable: True),
    StructField(name: 'position', StringType(), nullable: True),
    StructField(name: 'classcode', StringType(), nullable: True),
    StructField(name: 'salary_start', DoubleType(), nullable: True),
    StructField(name: 'salary_end', DoubleType(), nullable: True),
    StructField(name: 'start_date', DateType(), nullable: True),
    StructField(name: 'end_date', DateType(), nullable: True),
    StructField(name: 'req', StringType(), nullable: True),
    StructField(name: 'notes', StringType(), nullable: True),
    StructField(name: 'duties', StringType(), nullable: True),
    StructField(name: 'selection', StringType(), nullable: True),
    StructField(name: 'experience_length', StringType(), nullable: True),
    StructField(name: 'job_type', StringType(), nullable: True),
    StructField(name: 'education_length', StringType(), nullable: True),
    StructField(name: 'school_type', StringType(), nullable: True),
    StructField(name: 'application_location', StringType(), nullable: True)
])