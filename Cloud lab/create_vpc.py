import boto3

def create_vpc():
    ec2 = boto3.client('ec2')
    
    vpc = ec2.create_vpc(CidrBlock='10.0.0.0/16')
    vpc_id = vpc['Vpc']['VpcId']
    print(f"VPC created with ID: {vpc_id}")
    
    ec2.create_tags(Resources=[vpc_id], Tags=[{"Key": "Name", "Value": "MyVPC"}])
    
    subnet = ec2.create_subnet(VpcId=vpc_id, CidrBlock='10.0.1.0/24')
    subnet_id = subnet['Subnet']['SubnetId']
    print(f"Subnet created with ID: {subnet_id}")
    
    igw = ec2.create_internet_gateway()
    igw_id = igw['InternetGateway']['InternetGatewayId']
    ec2.attach_internet_gateway(InternetGatewayId=igw_id, VpcId=vpc_id)
    print(f"Internet Gateway created and attached: {igw_id}")
    
    route_table = ec2.create_route_table(VpcId=vpc_id)
    route_table_id = route_table['RouteTable']['RouteTableId']
    print(f"Route Table created with ID: {route_table_id}")
    
    ec2.create_route(
        RouteTableId=route_table_id,
        DestinationCidrBlock='0.0.0.0/0',
        GatewayId=igw_id
    )
    print(f"Route added to Route Table: {route_table_id}")
    
    ec2.associate_route_table(SubnetId=subnet_id, RouteTableId=route_table_id)
    print(f"Route Table {route_table_id} associated with Subnet {subnet_id}")
    
    return vpc_id, subnet_id, igw_id, route_table_id

if __name__ == "__main__":
    create_vpc()
