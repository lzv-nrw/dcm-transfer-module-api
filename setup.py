import os
from setuptools import setup

setup(
    version="2.1.0",
    name="dcm-transfer-module-api",
    description="api for transfer-module-containers",
    author="LZV.nrw",
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
