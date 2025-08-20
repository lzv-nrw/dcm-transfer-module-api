import os
from setuptools import setup

setup(
    version="2.2.0",
    name="dcm-transfer-module-api",
    description="specification of the DCM Transfer Module API",
    author="LZV.nrw",
    license="MIT",
    install_requires=[
    ],
    packages=[
        "dcm_transfer_module_api"
    ],
    package_data={
        "dcm_transfer_module_api": [
            "dcm_transfer_module_api/openapi.yaml",
        ],
    },
    include_package_data=True,
)
