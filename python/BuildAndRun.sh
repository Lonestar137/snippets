pythonHotReloadingBuild(){
  # NPM: Using nodemon to build your project automatically.
  npm install -g nodemon
  nodemon myapp.py

  # ALT: Using custom watchdog script
  python -m scripts/watchdogHotReloader.py
}

pythonRunAsModule(){
  #myproject
  # my_module/
  #   main.py
  python -m my_module/main.py
}

pythonBuild(){
  python setup.py bdist_wheel sdist # bdist = binary wheel, sdist = source distribution
  pip install . # install your build locally.

  twine check dist/* # Check to see if all the necessary files are there.
  twint upload -r testpypi dist/* # upload to test pypi
  twine upload dist/*             # production pypi
}

