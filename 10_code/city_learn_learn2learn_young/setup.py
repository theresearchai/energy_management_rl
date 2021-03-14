from setuptools import setup, find_packages
setup(name='citylearn',
      packages=find_packages(),
      include_package_data=True,
      package_data={
        '': ['*.csv', '*.npy'],
      },      
      version='0.0.1',
      install_requires=['gym', 'numpy', 'pandas', 'joblib']
)