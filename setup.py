import os

from setuptools import setup


install_requires = [
    "tokenizer_tools",
    "pathlib",
    "pymongo==3.10.1",
]

setup(name='data_expend',
      version='1.5',
      description='data_expend',
      url='https://github.com/shfshf/data_expend',
      author='SHF',
      author_email='1316478299@qq.com',
      packages=['data_expend'],
      install_requires=install_requires,
      )
