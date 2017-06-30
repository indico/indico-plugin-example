from setuptools import setup, find_packages


setup(
    name='indico_example',
    version='1.0.dev0',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    install_requires=[
        'indico>=2.0.dev0'
    ],
    entry_points={'indico.plugins': {'example = indico_example:ExamplePlugin'}}
)
