# cloudformation-substacks
Demo to define multiple stack from same cloudformation template

	testing push

##    Command testing firsts
- set first yml on s3 bucket (--profile used if have multiple profile on aws clim check: https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-profiles.html)

	aws s3 cp testing-substack.yml s3://gitlab-cicd
	aws cloudformation package --template-file testing-mainstack.yml --s3-bucket gitlab-cicd --output-template testing-packstack.yaml
    aws cloudformation deploy --force-upload --template-file packaged_dev.yaml --stack-name Testing-deploy --profile tokiotest --capabilities CAPABILITY_AUTO_EXPAND CAPABILITY_IAM
