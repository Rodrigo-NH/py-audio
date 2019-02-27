#
#https://stackoverflow.com/questions/19768267/relocation-r-x86-64-32s-against-linking-error
# https://github.com/pytorch/ELF/issues/98
#from distutils.core import setup, Extension
from setuptools import setup, Extension



module1 = Extension('audiodev', sources = ['audiodev.cpp'],
                    include_dirs = ['rtaudio-4.0.8'],
                    libraries = ['pthread', 'asound'], extra_link_args = ['rtaudio-4.0.8/librtaudio.a'])
module2 = Extension('audiospeex', sources = ['audiospeex.cpp'],
                    include_dirs = ['speex-1.2rc1/include'],
                    library_dirs = ['speex-1.2rc1/libspeex/.libs'],
                    libraries = ['speex', 'speexdsp'], extra_link_args = ['-fPIC'])
import os
libdir = 'flite-1.4-release/build/%s-%s%s'%(os.uname()[-1], 
             os.uname()[0].lower(), os.uname()[2])

# flite needs be compiled with make CFLAGS=-fPIC in case of errors
module3 = Extension('audiotts', sources = ['audiotts.cpp'], include_dirs = ['flite-1.4-release/include'], library_dirs = [libdir], libraries = ['flite_cmu_us_kal', 'flite_cmu_us_awb', 'flite_cmu_us_rms', 'flite_cmu_us_slt', 'flite_usenglish', 'flite_cmulex', 'flite'], extra_link_args = ['-fPIC'])
setup (name = 'PackageName', python_requires='>3.5.2',  version = '1.0',
       description = 'audio device and codecs module',
       ext_modules = [module1, module2, module3])
       