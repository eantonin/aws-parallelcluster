"""
    ParallelCluster

    ParallelCluster API  # noqa: E501

    The version of the OpenAPI document: 3.0.0
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import pcluster.client
from pcluster.client.model.cloud_formation_status import CloudFormationStatus
from pcluster.client.model.ec2_ami_info import Ec2AmiInfo
from pcluster.client.model.image_build_status import ImageBuildStatus
from pcluster.client.model.image_builder_image_status import ImageBuilderImageStatus
from pcluster.client.model.image_configuration_structure import ImageConfigurationStructure
globals()['CloudFormationStatus'] = CloudFormationStatus
globals()['Ec2AmiInfo'] = Ec2AmiInfo
globals()['ImageBuildStatus'] = ImageBuildStatus
globals()['ImageBuilderImageStatus'] = ImageBuilderImageStatus
globals()['ImageConfigurationStructure'] = ImageConfigurationStructure
from pcluster.client.model.describe_image_response_content import DescribeImageResponseContent


class TestDescribeImageResponseContent(unittest.TestCase):
    """DescribeImageResponseContent unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testDescribeImageResponseContent(self):
        """Test DescribeImageResponseContent"""
        # FIXME: construct object with mandatory attributes with example values
        # model = DescribeImageResponseContent()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()