from troposphere import Tags, GetAZs, Select
from troposphere import Parameter, Output, Ref, Template, ImportValue
import troposphere.ec2 as ec2
import os



class AddressMatchingServiceInstance(ec2.Instance):
    InstanceType = "t2.micro"
    ImageId = "ami-b6daced2"
    KeyName = "default"
    SecurityGroupIds = ["launch-wizard-2"]

def generate():
    template = Template()
    template.add_description("Company Name Matching Service")
    template.add_version("2010-09-09")
    template.add_resource(AddressMatchingServiceInstance("AddrMatchingServiceInst1"))

    stack_name, _ = os.path.splitext(os.path.basename(__file__))

    print template.to_json()


if __name__ == "__main__":
    generate()
