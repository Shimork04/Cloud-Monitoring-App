import boto3        # type: ignore # python aws sdk to use aws services

ecr_client = boto3.client("ecr")

repository_name = "cloud-native-app"

#  using create-repository api - check boto3 documentation

response = ecr_client.create_repository(repositoryName=repository_name)
repository_uri = response['repository']['repositoryUri']
print(repository_uri)


