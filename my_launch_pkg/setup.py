from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'my_launch_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
            glob('launch/*.launch.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='kjs',
    maintainer_email='doduck101@gmail.com',
    description='TODO: Package description',
    license='Apache-2.0',
    entry_points={
        'console_scripts': [
            'srv_driver1 = my_launch_pkg.srv_driver1:main',
            'start_stop_client = my_launch_pkg.start_stop_client:main'
        ],
    },
)
