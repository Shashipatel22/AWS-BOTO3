Import boto3
region_list = []
regions = boto3.client('ec2',region_name='us-east-1')
myregions = regions.describe_regions().get('Regions')
for region in myregions:
    region_list.append(region ['RegionName'])
print (region_list)
for new_region in region_list:
    print(f'Retriving VPCs from Region {new_region}')
    client =  boto3.client('ec2',region_name=new_region)
    resp = client.describe_vpcs().get('Vpcs','Key Not Found')
    for VPC_INFO in resp: 
        print(VPC_INFO['VpcId'],'-->',VPC_INFO['CidrBlock'])
        print(50*'-')
