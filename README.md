# PyRolL Basic Meta Package

This package does not introduce any new functionality, it works just as a meta-package to simplify the installation of
the PyRolL core and a couple of basic plugins through its dependencies.

The following packages are installed alongside their own dependencies:

- `pyroll`
- `pyroll-integral-thermal`
- `pyroll-hensel-power-and-labour`
- `pyroll-wusatowski-spreading`
- `pyroll-zouhar-contact`
- `pyroll-freiberg-flow-stress`
- `pyroll-hitchcock-roll-flattening`

By importing this package with `import pyroll.basic`, all listed packages are imported and thus registered as active
plugins.
The public API of this package is the union of all those packages.
So with `import pyroll.basic as pr` one has access to all public APIs of those packages under one single alias.