import os
from glob import glob
from setuptools import setup

package_name = 'amr_description'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/amr_visualize.launch.py']),
        ('share/' + package_name + '/urdf', ['urdf/amr.urdf']),
        ('share/' + package_name + '/rviz', ['rviz/amr.rviz'])
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='rodrigo',
    maintainer_email='rodrigo.vela@indt.org.br',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
        ],
    },
)
