import versioner
import setuptools

setuptools.setup(
	name=versioner.__name__,
	version=versioner.__version__,
	description='A simple versioning module, with the ability to customise to any version-system.',
	keywords=["versioner.py", "versioner"],
	packages=setuptools.find_packages(),
	author_email=versioner.__email__,
	url='https://github.com/romanin-rf/versioner.py',
	author=versioner.__author__,
	license='MIT',
	install_requires=["vbml"],
    setup_requires=["vbml"]
)
