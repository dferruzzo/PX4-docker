from setuptools import setup
from glob import glob
import os

package_name = 'px4_telemetry'

setup(
    name=package_name,
    version='0.1.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='PX4 developer',
    maintainer_email='diego.ferruzzo@ufabc.edu.br',
    description='Read and display PX4 SITL telemetry using ROS 2.',
    license='Apache-2.0',
    entry_points={'console_scripts': ['telemetry_node = px4_telemetry.telemetry_node:main']},
)
