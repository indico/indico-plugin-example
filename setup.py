from setuptools import setup, find_packages


setup(
    name='indico_example',
    version='0.4',
    packages=find_packages(),
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'indico>=1.9.10.dev0'
    ],
    entry_points={'indico.plugins': {'example = indico_example:ExamplePlugin'}}
)
