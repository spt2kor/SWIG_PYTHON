#online links : https://makefiletutorial.com/
hello:
	echo "its FAST2 - v4, try commands [ str , vec ]  "

str: python/str.py all
	python python/str.py

vec: python/vector.py all
	python python/vector.py

map: python/map.py all
	python python/map.py

#umap: perl/umap.pl all
#	perl perl/umap.p
#=========================================== test code compilation

generated_files/obj/str.o: cpp/str.cpp cpp/str.h
	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/str.cpp -o generated_files/obj/str.o


generated_files/obj/vect.o: cpp/vect.cpp cpp/vect.h
	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/vect.cpp -o generated_files/obj/vect.o


generated_files/obj/map.o: cpp/map.cpp cpp/map.h
	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/map.cpp -o generated_files/obj/map.o

#generated_files/obj/umap.o: cpp/umap.cpp cpp/umap.h
#	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/umap.cpp -o generated_files/obj/umap.o

#=========================================== SWIG file compilation
generated_files/STDLib_wrap.cpp: swig/STDLib.i cpp/str.cpp cpp/str.h
	swig -c++ -python -outdir generated_files -o generated_files/STDLib_wrap.cpp swig/STDLib.i

generated_files/obj/STDLib_wrap.o: generated_files/STDLib_wrap.cpp
	g++ -c -Wno-literal-suffix -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64 -I /opt/python/3.11/linux/RHEL70/include/python3.11/ generated_files/STDLib_wrap.cpp -I cpp/ -o generated_files/obj/STDLib_wrap.o

#generated_files/STDLib.so: generated_files/obj/umap.o generated_files/obj/map.o generated_files/obj/vect.o generated_files/obj/str.o  generated_files/obj/STDLib_wrap.o
#	g++ -shared generated_files/obj/umap.o generated_files/obj/map.o generated_files/obj/vect.o generated_files/obj/str.o generated_files/obj/STDLib_wrap.o -o generated_files/STDLib.so -L/opt/perl_5.18.2/linux50_64/lib/CORE -lperlifx

generated_files/_STDLib.so: generated_files/obj/str.o generated_files/obj/STDLib_wrap.o generated_files/obj/vect.o generated_files/obj/map.o
	g++ -shared generated_files/obj/map.o generated_files/obj/str.o generated_files/obj/STDLib_wrap.o generated_files/obj/vect.o -o generated_files/_STDLib.so -L/opt/python/3.11/linux/RHEL70/lib -lpython3.11

#=========================================== generic phony
all: generated_files/_STDLib.so

clean:
	rm -f generated_files/obj/umap.o generated_files/obj/map.o generated_files/obj/vect.o generated_files/obj/str.o 
	rm -f generated_files/_STDLib.so generated_files/STDLib_wrap.cpp generated_files/STDLib.py generated_files/obj/STDLib_wrap.o

#========================================================
# file:///C:/src/swigwin-4.1.1/Examples/perl5/callback/index.html
# 
# 
#==========================================================