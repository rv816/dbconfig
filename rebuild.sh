rm -rf build dbconfig.egg-info dist
python setup.py build
pip install -e . --no-deps --force-reinstall
