from setuptools import setup, find_packages
import sys, os

version = '0.2'
shortdesc = 'Stanbol Semantic Engine: RESTful Plone Integration.'
longdesc = open(os.path.join(os.path.dirname(__file__), 'README.rst')).read()  + "\n" + open(os.path.join("docs", "HISTORY.txt")).read()
tests_require = ['interlude']

setup(name='stanbol.plone',
      version=version,
      description=shortdesc,
      long_description=longdesc,
      classifiers=[
            'Development Status :: 5 - Production/Stable',
            'License :: OSI Approved :: GNU General Public License (GPL)',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Topic :: Software Development',
            "Framework :: Plone",
      ],
      keywords='Stanbol',
      author='Jens Klein    ',
      author_email='jens@bluedynamics.com',
      url=u'http://github.com/collective/stanbol.plone',
      license='GPLv2',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['stanbol'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
            'setuptools',
            'stanbol.client',
            'Plone',
            'plone.app.registry',
            'jquery.pyproxy'
      ],
      setup_requires=["PasteScript"],
      paster_plugins=["ZopeSkel"],
      tests_require=tests_require,
      test_suite="stanbol.client.tests.test_suite",
      extras_require = dict(
          test=tests_require,
      ),
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
)
