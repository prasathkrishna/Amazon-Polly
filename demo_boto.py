import boto3
aws_mg_con=boto3.session.Session(profile_name='20bcs320_user')
iam_con=aws_mg_con.resource('iam')
for each_user in iam_con.users.all():
    print(each_user.name)