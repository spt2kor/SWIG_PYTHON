ds2: all
	echo "its FAST3 Python v1"
	python python/SimpleDS2.py

ds1: all
	echo "its FAST3 Python v1"
	python python/SimpleDS1.py


#=========================================== test code compilation

generated_files/obj/SimpleDS.o: cpp/SimpleDS.cpp cpp/SimpleDS.h
	g++ -std=c++11 -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/SimpleDS.cpp -o generated_files/obj/SimpleDS.o

#=========================================== SWIG file compilation
#swig -c++ -python -docstrings -outdir generated_files -o generated_files/SimpleDS_wrap.cpp swig/SimpleDS.i
generated_files/SimpleDS_wrap.cpp: swig/SimpleDS.i
	swig -c++ -python -outdir generated_files -o generated_files/SimpleDS_wrap.cpp swig/SimpleDS.i

#generated_files/obj/SimpleDS_wrap.o: generated_files/SimpleDS_wrap.cpp
#	g++ -c -Wno-literal-suffix -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64 -I /opt/perl_5.18.2/linux50_64/lib/CORE/ generated_files/SimpleDS_wrap.cpp -I cpp/ -o generated_files/obj/SimpleDS_wrap.o
	
# -I/usr/include/python3.8   =>    /opt/python/3.11/linux/RHEL70/include/python3.11/ (location of Python.h file)
generated_files/obj/SimpleDS_wrap.o: generated_files/SimpleDS_wrap.cpp
	g++ -c -Wno-literal-suffix -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64 -I /opt/python/3.11/linux/RHEL70/include/python3.11/ generated_files/SimpleDS_wrap.cpp -I cpp/ -o generated_files/obj/SimpleDS_wrap.o


#generated_files/_SimpleDS.so: generated_files/obj/SimpleDS.o  generated_files/obj/SimpleDS_wrap.o
#	g++ -shared generated_files/obj/SimpleDS.o generated_files/obj/SimpleDS_wrap.o -o generated_files/_SimpleDS.so -L/opt/perl_5.18.2/linux50_64/lib/CORE -lperlifx

#  -L/opt/perl_5.18.2/linux50_64/lib/CORE -lperlifx   =>   -L/opt/python/3.11/linux/RHEL70/lib -lpython3.11
generated_files/_SimpleDS.so: generated_files/obj/SimpleDS.o  generated_files/obj/SimpleDS_wrap.o
	g++ -shared generated_files/obj/SimpleDS.o generated_files/obj/SimpleDS_wrap.o -o generated_files/_SimpleDS.so -L/opt/python/3.11/linux/RHEL70/lib -lpython3.11
#=========================================== generic phony
all: generated_files/_SimpleDS.so

clean:
	rm -f generated_files/obj/SimpleDS.o 
	rm -f generated_files/_SimpleDS.so generated_files/SimpleDS_wrap.cpp generated_files/SimpleDS.py generated_files/obj/SimpleDS_wrap.o

#========================================================
# file:///C:/src/swigwin-4.1.1/Examples/perl5/callback/index.html
# 
# 
#==========================================================