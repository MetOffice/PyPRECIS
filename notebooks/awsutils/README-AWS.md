
## AWS

### Create an EC2 instance

* Select Eu-west2 (London) region from the top right of navigation bar
* Click on Launch instance
* Choose Amazon Linux 2 AMI (HVM) kARNEL 5.10 64-bit (- X86) machine, click select
* Choose t2.2xlarge and click next: configure instance details
* Choose subnet default eu-west-2c
* In IAM role choose existing trainings-ec2-dev role and click next: storage
* 8 gb is fine, click next: add tags
* Add following tags
  * Name: [Unique Instance name]
  * Tenable: FA
  * ServiceOwner: [firstname.lastname]
  * ServiceCode: PABCLT
* add securitygroup, select an existing security group: IAStrainings-ec2-mo
* Review and Launch and then select launch
* It will prompt to set a key pair (to allow ssh). create a new key and download it.

It will create the instance. To see the running instance goto instances and instacne state will be "Running"

### SSH instance on VDI


* Save the key (.pem)  to .ssh and set the permission: chmod 0400 ~/.ssh/your_key.pem
* Open ~/.ssh/config and add following:

```
Host ec2-*.eu-west-2.compute.amazonaws.com
    IdentityFile ~/.ssh/your_key.pem
    User ec2-user

```

* Find the public IPv4 DNS and ssh in using it ssh ec2-<ip address>.eu-west-2.compute.amazonaws.com, public IPv4 DNS can be found in instance detail on AWS. Click on your instance and it will open the details.

* Remember to shutdown the instance when not using it. It will save the cost.
### create s3 bucket

* goto s3 service and press "create bucket"
* name the bucket
* set region to EU (London) eu-west-2
* add tags:
  * Name: [name of bucket or any unique name]
  * ServiceOwner: [your-name]
  * ServiceCode: PABCLT
  * Tenable: FA
* click on "create bucket"

### Key configurations


The above script run only when config files contains latest keys. In order to update the keys:

* go to AB climate training dev --> Administrator access --> command line or programmatic access
* Copy keys in "Option 1: Set AWS environment variables"
* In VDI, paste (/replace existing) these keys in ~/.aws/config
* add [default] in first line
* Copy keys in "Option 2: Add a profile to your AWS credentials file"
* In VDI, Paste the keys in credentials file: ~/.aws/credentials (remove the first copied line, looks somethings like: [198477955030_AdministratorAccess])
* add [default] in first line

The config and credentials file should look like (with own keys):

```
[default]
export AWS_ACCESS_KEY_ID="ASIAS4NRVH7LD2RRGSFB"
export AWS_SECRET_ACCESS_KEY="rpI/dxzQWhCul8ZHd18n1VW1FWjc0LxoKeGO50oM"
export AWS_SESSION_TOKEN="IQoJb3JpZ2luX2VjEGkaCWV1LXdlc3QtMiJH"
```

### Loading data on s3 bucket from VDI (using boto3)

to upload the file(s) on S3 use: /aws-scripts/s3_file_upload.py
to upload the directory(s) on S3 use: /aws-scripts/s3_bulk_data_upload.py

### AWS Elastic container repository

Following instructions are for creating image repo on ECR and uploading container image

* ssh to the previously created EC2 instance, make an empty Git repo:

```
sudo yum install -y git
git init
```
* On VDI, run the following command to push the PyPrecis repo containing the docker file to the EC2 instance:
```
git push <ec2 host name>:~
```

* Now checkout the branch on EC2: git checkout [branch-name]
* Install docker and start docker service

```
sudo amazon-linux-extras install docker
sudo service docker start
```

* build docker image:

```
sudo docker build .
```

* goto AWS ECR console and "create repository", make it private and name it

* Once created, press "push commands"

* copy the command and run it on EC2 instance, it will push the container image on record. if get "permission denied" error, please add "sudo" before "docker" in the command.



### AWS Sagemaker: Run notebook using custom kernel
The instructions below follow the following tutorial:
https://aws.amazon.com/blogs/machine-learning/bringing-your-own-custom-container-image-to-amazon-sagemaker-studio-notebooks/

* goto Sagemaker and "open sagemaker domain"
* add user
  * Name and and select Amazonsagemaker-executionrole (dafult one)

* Once user is created, goto "attach image"
* Select "New Image" and add image URI (copy from image repo)
* Give new image name, display name, sagmaker-executionrole and add tags and attach the image
* add kernel name and display name (both can be same)
* Now, launch app -> Studio and it will open the Notebook dashboard.
* Select python notebook and add your custom named Kernel
