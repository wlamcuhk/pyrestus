def configuration(parent_package='',top_path=None):
      from numpy.distutils.misc_util import Configuration
      config = Configuration('dataprocessing', parent_package, top_path)
      config.add_subpackage('compareimages/src/distance')
      config.add_subpackage('usv/utils/colorconversion')
      return config



if __name__ == '__main__':
    from numpy.distutils.core import setup
    setup(**configuration(top_path='').todict())
