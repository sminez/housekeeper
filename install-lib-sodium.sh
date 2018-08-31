#!/bin/sh
mkdir -p /source-checkouts
cd /source-checkouts
wget https://download.libsodium.org/libsodium/releases/libsodium-1.0.12.tar.gz
tar xzvf libsodium-1.0.12.tar.gz
cd libsodium-1.0.12
./autogen.sh
./configure --prefix=$BUILD_PREFIX
make check
sudo make install
