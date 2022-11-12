from setuptools import setup

package_name = 'server_to_motors'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='robb',
    maintainer_email='bradley.hargis@ymail.com',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker = server_to_motors.publisher_member_function:main',
            'listener = server_to_motors.subscriber_member_function:main',
            'object_talker = server_to_motors.publisher_object_detection:main',
        ],
    },
)
