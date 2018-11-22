from distutils.core import setup

setup(
    name='pyqtlet',
    packages=[
        'pyqtlet',
        'pyqtlet.web',
        'pyqtlet.web.modules.leaflet',
        'pyqtlet.web.modules.leaflet.images',
        'pyqtlet.web.modules.leafletdraw',
        'pyqtlet.web.modules.leafletdraw.draw',
        'pyqtlet.web.modules.leafletdraw.draw.handler',
        'pyqtlet.web.modules.leafletdraw.edit',
        'pyqtlet.web.modules.leafletdraw.edit.handler',
        'pyqtlet.web.modules.leafletdraw.images',
        'pyqtlet.web.modules.leafletdraw.ext',
        'pyqtlet.leaflet',
        'pyqtlet.leaflet.control',
        'pyqtlet.leaflet.core',
        'pyqtlet.leaflet.layer',
        'pyqtlet.leaflet.layer.marker',
        'pyqtlet.leaflet.layer.tile',
        'pyqtlet.leaflet.layer.vector',
        'pyqtlet.leaflet.map',
    ],
    package_data={
        'pyqtlet.web': ['*'], 'pyqtlet.web.modules': ['*'],
        'pyqtlet.web.modules.leaflet': ['*'],
        'pyqtlet.web.modules.leaflet.images': ['*'],
        'pyqtlet.web.modules.leafletdraw': ['*'],
        'pyqtlet.web.modules.leafletdraw.draw': ['*'],
        'pyqtlet.web.modules.leafletdraw.draw.handler': ['*'],
        'pyqtlet.web.modules.leafletdraw.edit': ['*'],
        'pyqtlet.web.modules.leafletdraw.edit.handler': ['*'],
        'pyqtlet.web.modules.leafletdraw.images': ['*'],
        'pyqtlet.web.modules.leafletdraw.ext': ['*'],
    },
    version='0.3.3',
    description='Bringing leaflet maps to PyQt',
    author='Samarth Hattangady',
    author_email='samhattangady@gmail.com',
    url='https://github.com/skylarkdrones/pyqtlet',
    keywords=['leaflet', 'pyqt', 'maps'],
    classifiers=[],
)
