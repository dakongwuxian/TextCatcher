# -*- mode: python ; coding: utf-8 -*-
from datetime import datetime

# 获取当前日期字符串，例如 20251222
today = datetime.now()
version_suffix = f"v{today.strftime('%y%m%d')}"
# 定义动态文件名
exe_name = f'TextCatcher-RegexTester_{version_suffix}'

a = Analysis(
    ['TextCatcher-RegexTester.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=exe_name,
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=False,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='TextCatcher-RegexTester.ico',
)

coll = COLLECT(
    exe,
    a.binaries,
    a.datas,
    strip=False,
    upx=False,
    upx_exclude=[],
    name=exe_name,
)
