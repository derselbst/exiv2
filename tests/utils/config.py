import os
import sys


class Config:
    """
    Contains configuration parameters for the test suite.
    When you run the test cases through `python3 runner.py`, the function configure_suite() in system_tests.py will override these parameters.
    """
    exiv2_dir         = os.path.normpath(os.path.join(os.path.abspath(__file__), '../../../'))
    bin_dir           = os.environ.get('EXIV2_BINDIR', os.path.join(exiv2_dir, 'build/bin'))
    dyld_library_path = os.path.join(bin_dir, '../lib')
    ld_library_path   = os.path.join(bin_dir, '../lib')
    data_dir          = os.path.join(exiv2_dir, 'test/data')
    tmp_dir           = os.path.join(exiv2_dir, 'test/tmp')

    exiv2_echo        = os.environ.get('EXIV2_ECHO', '')
    verbose           = os.environ.get('VERBOSE', '')
    valgrind          = os.environ.get('VALGRIND', '')
    encoding          = 'utf-8'
    
    # Identify the platform
    platform          = sys.platform.lower() or 'unknown'    # It could be linux, win32, msys, cygwin, darwin, etc.
    if os.name == 'nt' and 'GCC' in sys.version:
        platform = 'mingw'

    # set http and port for io_test
    if platform   in ['cygwin']:
        exiv2_port  = '12762'
    elif platform in ['mingw', 'msys']:
        exiv2_port  = '12761'
    else:
        exiv2_port  = '12760'
    exiv2_port  = os.environ.get('EXIV2_PORT', exiv2_port)
    exiv2_http  = os.environ.get('EXIV2_HTTP', 'http://127.0.0.1')

