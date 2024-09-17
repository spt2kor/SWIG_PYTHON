ds2: all
	echo "its FAST3 Python v2"
	python python/SimpleDS2.py

#ds1: all
#	echo "its FAST3 Python v1"
#	python python/SimpleDS1.py


#inh1: python/inheritance1.py generated_files/_SimpleDS.so
#	echo "its FAST v2 Python"
#	python python/inheritance1.py


sin: python/singleton.py all
	echo "its FAST v2"
	python python/singleton.py

#arr: perl/array_hash.pl all
#	perl perl/array_hash.pl

inh1: python/inheritance1.py all
	echo "its FAST3 Python v2"
	python python/inheritance1.py


inh2: python/inheritance2.py all
	echo "its FAST3 Python v2"
	python python/inheritance2.py


inh3: python/inheritance3.py all
	echo "its FAST3 Python v2"
	python python/inheritance3.py


strc1: python/struct1.py all
	echo "its FAST3 Python v2"
	python python/struct1.py


#class: perl/class.pl all
#	perl perl/class.pl

#array: perl/array.pl all
#	perl perl/array.pl

ptr1: python/pointer1.py all
	python python/pointer1.py

#ptr1: perl/Pointer1.pl all
#	perl perl/Pointer1.pl


#==============================================================================================================
#generated_files/SimpleDS_wrap.cpp: cpp/SimpleDS.h
#	swig -c++ -perl -module SimpleDS -outdir generated_files -o generated_files/SimpleDS_wrap.cpp cpp/SimpleDS.h

generated_files/obj/inheritance1.o: cpp/inheritance1.cpp cpp/inheritance1.h
	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/inheritance1.cpp -o generated_files/obj/inheritance1.o

generated_files/obj/Pointer.o: cpp/Pointer.cpp cpp/Pointer.h
	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/Pointer.cpp -o generated_files/obj/Pointer.o

#generated_files/obj/Pointer1.o: cpp/Pointer1.cpp cpp/Pointer1.h
#	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/Pointer1.cpp -o generated_files/obj/Pointer1.o


generated_files/obj/Singleton.o: cpp/Singleton.cpp cpp/Singleton.h
	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/Singleton.cpp -o generated_files/obj/Singleton.o

generated_files/obj/DataTypes.o: cpp/DataTypes.cpp cpp/DataTypes.h
	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/DataTypes.cpp -o generated_files/obj/DataTypes.o


generated_files/obj/Shape.o: cpp/Shape.cpp cpp/Shape.h
	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/Shape.cpp -o generated_files/obj/Shape.o


generated_files/obj/SimpleDS.o: cpp/SimpleDS.cpp cpp/SimpleDS.h cpp/Shape.h
	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/SimpleDS.cpp -o generated_files/obj/SimpleDS.o
#==============================================================================================================

generated_files/SimpleDS_wrap.cpp: swig/SimpleDS.i
	swig -c++ -python  -outdir generated_files -o generated_files/SimpleDS_wrap.cpp swig/SimpleDS.i


# -I/usr/include/python3.8   =>    /opt/python/3.11/linux/RHEL70/include/python3.11/ (location of Python.h file)
generated_files/obj/SimpleDS_wrap.o: generated_files/SimpleDS_wrap.cpp
	g++ -c -Wno-literal-suffix -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64 -I /opt/python/3.11/linux/RHEL70/include/python3.11/ generated_files/SimpleDS_wrap.cpp -I cpp/ -o generated_files/obj/SimpleDS_wrap.o
	
#--------------------------------------------------------------------------------------------------------------------
generated_files/inheritance1_wrap.cpp: swig/inheritance1.i
	swig -c++ -python -outdir generated_files -o generated_files/inheritance1_wrap.cpp swig/inheritance1.i

generated_files/obj/inheritance1_wrap.o: generated_files/inheritance1_wrap.cpp
	g++ -c -Wno-literal-suffix -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64 -I /opt/python/3.11/linux/RHEL70/include/python3.11/ generated_files/inheritance1_wrap.cpp -I cpp/ -o generated_files/obj/inheritance1_wrap.o

#==============================================================================================================

#generated_files/SimpleDS.so: generated_files/obj/Pointer1.o generated_files/obj/Singleton.o generated_files/obj/Pointer.o generated_files/obj/Shape.o generated_files/obj/SimpleDS.o generated_files/obj/SimpleDS_wrap.o  generated_files/obj/DataTypes.o 
#	g++ -shared generated_files/obj/Pointer1.o generated_files/obj/Singleton.o generated_files/obj/Pointer.o generated_files/obj/Shape.o generated_files/obj/SimpleDS.o generated_files/obj/SimpleDS_wrap.o generated_files/obj/DataTypes.o -o generated_files/SimpleDS.so -L/opt/perl_5.18.2/linux50_64/lib/CORE -lperlifx

generated_files/_SimpleDS.so: generated_files/obj/Singleton.o generated_files/obj/Pointer.o generated_files/obj/DataTypes.o generated_files/obj/Shape.o generated_files/obj/SimpleDS.o generated_files/obj/SimpleDS_wrap.o
	g++ -shared generated_files/obj/Singleton.o generated_files/obj/Pointer.o generated_files/obj/Shape.o generated_files/obj/DataTypes.o generated_files/obj/SimpleDS.o generated_files/obj/SimpleDS_wrap.o -o generated_files/_SimpleDS.so -L/opt/python/3.11/linux/RHEL70/lib -lpython3.11

generated_files/INHRT.so:  generated_files/obj/inheritance1_wrap.o generated_files/obj/inheritance1.o
	g++ -shared generated_files/obj/inheritance1_wrap.o generated_files/obj/inheritance1.o -o generated_files/_INHRT.so -L/opt/python/3.11/linux/RHEL70/lib -lpython3.11

#==============================================================================================================
all: generated_files/_SimpleDS.so generated_files/INHRT.so

#all: generated_files/SimpleDS_wrap.cpp cpp/SimpleDS.cpp cpp/SimpleDS.h
#	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/SimpleDS.cpp -o generated_files/obj/SimpleDS.o

#	g++ -c -Wno-literal-suffix -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64 -I /opt/perl_5.18.2/linux50_64/lib/CORE/ generated_files/SimpleDS_wrap.cpp -I cpp/ -o generated_files/obj/SimpleDS_wrap.o

#	g++ -shared generated_files/obj/SimpleDS.o generated_files/obj/SimpleDS_wrap.o -o generated_files/SimpleDS.so -L/opt/perl_5.18.2/linux50_64/lib/CORE -lperlifx

#==============================================================================================================

clean:
	rm -f generated_files/obj/Pointer1.o generated_files/obj/Singleton.o generated_files/obj/Pointer.o generated_files/obj/Shape.o generated_files/obj/SimpleDS.o  generated_files/obj/DataTypes.o  
	rm -f generated_files/obj/SimpleDS_wrap.o generated_files/_SimpleDS.so generated_files/SimpleDS_wrap.cpp generated_files/SimpleDS.py
	rm -f generated_files/obj/inheritance1.o
	rm -f generated_files/_INHRT.so generated_files/inheritance1_wrap.cpp generated_files/obj/inheritance1_wrap.o generated_files/inheritance1.pm 

#==============================================================================================================



#========================================================
# https://www.cs.swarthmore.edu/~newhall/unixhelp/howto_makefiles.html
# https://web.mit.edu/gnu/doc/html/make_3.html
# https://www.gnu.org/software/make/manual/make.html
#==========================================================