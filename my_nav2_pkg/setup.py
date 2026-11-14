from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_nav2_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Jun-Sik Kim',
    maintainer_email='doduck101@gmail.com',
    description='ROS2 연습용 패키지 — nav2',
    license='Apache-2.0',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'nav2_pose = my_nav2_pkg.nav2_pose:main'
        ],
    },
)
