from setuptools import setup


setup(
    name='indico_example',
    version='0.1',
    packages=['indico_example'],
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    install_requires=[
        'indico>=1.9'
    ],
    entry_points={'indico.plugins': {'example = indico_example:ExamplePlugin'}}
)
