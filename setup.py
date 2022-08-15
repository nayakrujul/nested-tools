from setuptools import setup, find_packages

long_description = 'A file-based version of SQL for the command line.'

setup(
  name = 'badsql-tools',
  version = '5.1',
  license='Apache',
  description = 'SQL but worse for the command line',
  author = 'Rujul Nayak',
  author_email = 'rujulnayak@outlook.com',
  url = 'https://github.com/nayakrujul/badsql-tools',
  download_url = 'https://github.com/nayakrujul/badsql-tools/archive/refs/tags/v_01.tar.gz',
  keywords = ['database', 'SQL', 'file'],
  install_requires=[
          'badsql'
      ],
  classifiers=[
    'Development Status :: 3 - Alpha', 
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
  ],
  long_description=long_description,
  long_description_content_type='text/x-rst',
  packages = find_packages(),
  entry_points ={
            'console_scripts': [
                'badsql_mkdb = badsql_tools.badsql_tools:mkdb',
                'badsql_insertrow = badsql_tools.badsql_tools:insertrow',
                'badsql_select = badsql_tools.badsql_tools:select',
                'badsql_display = badsql_tools.badsql_tools:display',
                'badsql_removerow = badsql_tools.badsql_tools:removerow',
            ]
  }
)
