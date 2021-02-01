import PyInstaller.__main__
import os
from VERSION import SOFTWARE_VERSION


release_name = "best_wishes_" + SOFTWARE_VERSION
script_name = "best_wishes.py"


PyInstaller.__main__.run([
    '--name=%s' % release_name,
    '--onefile',
    '--console',
    '--specpath=./pyinstaller/spec',
    '--workpath=./pyinstaller/build',
    '--distpath=./REALEASE',
    # '--add-data="README;."',
    # '--add-data="image1.png;img"',
    # '--add-binary="libfoo.so;lib"',
    # '--hidden-import=secret1',
    # '--hidden-import=secret2',
    '--icon=%s' % os.path.join('D:/myStudyProject/py_project/', 'icon.ico'),
    os.path.join('D:/myStudyProject/py_project/', script_name),
])



# pyinstaller -F best_wishes.py --icon=D:/myStudyProject/py_project/icon.ico
# pyinstaller -F best_wishes.py --clean
"""
usage: setup.py [-h] [-v] [-D] [-F] [--specpath DIR] [-n NAME]
                  [--add-data <SRC;DEST or SRC:DEST>]
                  [--add-binary <SRC;DEST or SRC:DEST>] [-p DIR]
                  [--hidden-import MODULENAME]
                  [--additional-hooks-dir HOOKSPATH]
                  [--runtime-hook RUNTIME_HOOKS] [--exclude-module EXCLUDES]
                  [--key KEY] [-d {all,imports,bootloader,noarchive}] [-s]
                  [--noupx] [--upx-exclude FILE] [-c] [-w]
                  [-i <FILE.ico or FILE.exe,ID or FILE.icns or "NONE">]
                  [--version-file FILE] [-m <FILE or XML>] [-r RESOURCE]
                  [--uac-admin] [--uac-uiaccess] [--win-private-assemblies]
                  [--win-no-prefer-redirects]
                  [--osx-bundle-identifier BUNDLE_IDENTIFIER]
                  [--runtime-tmpdir PATH] [--bootloader-ignore-signals]
                  [--distpath DIR] [--workpath WORKPATH] [-y]
                  [--upx-dir UPX_DIR] [-a] [--clean] [--log-level LEVEL]
                  scriptname [scriptname ...]
setup.py: error: the following arguments are required: scriptname
"""
