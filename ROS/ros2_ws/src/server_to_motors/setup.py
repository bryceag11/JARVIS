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
            'local_server_talker = server_to_motors.local_server_publisher:main',
            'motor_control_listener = server_to_motors.motor_control_subscriber:main',
            'object_detection_talker = server_to_motors.object_detection_publisher:main',
        ],
    },
)
