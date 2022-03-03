from setuptools import setup


setup(name='cloudy',
      packages=['cloudy'],
      version=open('VERSION').read().strip(),
      author='Amador Pahim',
      author_email="amador@pahim.org",
      description='Demo Web Application',
      python_requires='>=3.6',
      license="GPLv2+",
      classifiers=[
          'Development Status :: 2 - Pre-Alpha',
          'Environment :: Web Environment',
          'Framework :: Flask',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: '
          'GNU General Public License v2 or later (GPLv2+)',
          'Natural Language :: English',
          'Operating System :: POSIX :: Linux',
          'Programming Language :: Python :: 3',
      ],
      install_requires=[
          'Flask~=2.0',
          'gunicorn~=20.1',
          'psycopg2-binary~=2.9',
      ],
      )
