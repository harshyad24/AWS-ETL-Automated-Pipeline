import boto3
import json
import time

def lambda_handler(event, context):
    glue = boto3.client('glue')
    job_name = 's3-glue-s3'
    max_retries = 5  # how many times to retry if job is already running
    wait_interval = 60  # seconds between retries

    try:
        for attempt in range(max_retries):
            # Check if there is an active run
            runs = glue.get_job_runs(JobName=job_name, MaxResults=1)
            if runs['JobRuns']:
                latest_status = runs['JobRuns'][0]['JobRunState']
                print(f"Latest Glue job status: {latest_status}")

                if latest_status in ('RUNNING', 'STARTING', 'STOPPING'):
                    print(f"Job {job_name} is currently {latest_status}. Waiting {wait_interval}s before retrying...")
                    time.sleep(wait_interval)
                    continue  # retry after wait

            # Start a new Glue job if none are active
            response = glue.start_job_run(JobName=job_name)
            job_run_id = response['JobRunId']

            print(f"Glue job '{job_name}' started successfully! JobRunId: {job_run_id}")

            return {
                'statusCode': 200,
                'body': json.dumps({
                    'message': f"Glue job '{job_name}' started successfully.",
                    'JobRunId': job_run_id
                })
            }

        # If all retries exhausted
        return {
            'statusCode': 429,
            'body': json.dumps(f"Job '{job_name}' is still running after {max_retries} retries.")
        }

    except glue.exceptions.ConcurrentRunsExceededException as e:
        print(f"Too many concurrent runs for job {job_name}: {str(e)}")
        return {
            'statusCode': 429,
            'body': json.dumps({
                'error': f"Too many concurrent runs for job {job_name}.",
                'details': str(e)
            })
        }

    except Exception as e:
        print(f"Error starting Glue job '{job_name}': {str(e)}")
        return {
            'statusCode': 500,
            'body': json.dumps(f"Error starting job {job_name}: {str(e)}")
        }