from setuptools import find_packages, setup

package_name = 'webcam_pubsub'

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
    maintainer='martinchassard_adm',
    maintainer_email='martinchassard_adm@todo.todo',
    description='TODO: Package description',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'talker                = webcam_pubsub.pub_webcam:main',
            'listener              = webcam_pubsub.sub_webcam:main',
        ],
    },
)
