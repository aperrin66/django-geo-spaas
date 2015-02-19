NUMTHREADS=2
if [[ -f /sys/devices/system/cpu/online ]]; then
    # Calculates 1.5 times physical threads
    NUMTHREADS=$(( ( $(cut -f 2 -d '-' /sys/devices/system/cpu/online) + 1 ) * 15 / 10  ))
fi
#NUMTHREADS=1 # disable MP
export NUMTHREADS

cd /vagrant
svn co https://github.com/google/libkml/trunk libkml
cd libkml
./autogen.sh
./configure

make -j $NUMTHREADS
sudo make install

cd
