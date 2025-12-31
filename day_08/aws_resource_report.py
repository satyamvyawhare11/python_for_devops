import json
import boto3
from botocore.exceptions import NoCredentialsError, ClientError


def list_s3_buckets():
    try:
        s3 = boto3.client("s3")
        response = s3.list_buckets()
        return [bucket["Name"] for bucket in response["Buckets"]]
    except NoCredentialsError:
        print("AWS credentials not configured.")
        return []
    except ClientError as error:
        print(f"S3 error: {error}")
        return []


def list_ec2_instances():
    try:
        ec2 = boto3.client("ec2")
        response = ec2.describe_instances()

        instances = []
        for reservation in response["Reservations"]:
            for instance in reservation["Instances"]:
                instances.append({
                    "InstanceId": instance["InstanceId"],
                    "State": instance["State"]["Name"]
                })
        return instances
    except NoCredentialsError:
        print("AWS credentials not configured.")
        return []
    except ClientError as error:
        print(f"EC2 error: {error}")
        return []


def main():
    report = {
        "S3_Buckets": list_s3_buckets(),
        "EC2_Instances": list_ec2_instances()
    }

    print("\n--- AWS Resource Report ---")
    print(json.dumps(report, indent=4))

    with open("aws_report.json", "w") as file:
        json.dump(report, file, indent=4)


if __name__ == "__main__":
    main()
