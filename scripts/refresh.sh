#!/bin/bash
rm -rf dist build ossa_scanner.egg-info
python3 setup.py sdist bdist_wheel > scripts/build.log
pip3 uninstall ossbomer-schema > scripts/install.log
rm -rf /opt/homebrew/lib/python3.12/site-packages/ossbomer_schema/ >> scripts/install.log
pip3 install dist/ossbomer_schema-*-py3-none-any.whl --force-reinstall --no-deps >> scripts/install.log