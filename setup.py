from setuptools import setup

setup(
    name = 'torrent-web-tools',
    version = '0.0.1',
    packages = [
        'torrent_web_tools',
        'bencode',
    ],
    entry_points = {
        'console_scripts': [
            'generate-web-torrent = torrent_web_tools.generator:main',
        ],
    },
)
