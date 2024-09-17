#online links : https://makefiletutorial.com/
hello:
	echo "its v3"

nam1: python/namespace1.py all
	python python/namespace1.py

#std: perl/std_lib.pl all
#	perl perl/std_lib.pl


#ptr1: perl/pointers1.pl all
#	perl perl/pointers1.pl

#cb: perl/callback.pl all
#	perl perl/callback.pl

#=========================================== test code compilation

generated_files/obj/Callback.o: cpp/Callback.cpp cpp/Callback.h
	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/Callback.cpp -o generated_files/obj/Callback.o

generated_files/obj/std_lib.o: cpp/std_lib.cpp cpp/std_lib.h
	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/std_lib.cpp -o generated_files/obj/std_lib.o

generated_files/obj/pointers1.o: cpp/pointers1.cpp cpp/pointers1.h
	g++ -c -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64  cpp/pointers1.cpp -o generated_files/obj/pointers1.o



#=========================================== SWIG file compilation
generated_files/Perl5ToCpp_wrap.cpp: swig/Perl5ToCpp.i
	swig -c++ -python -outdir generated_files -o generated_files/Perl5ToCpp_wrap.cpp swig/Perl5ToCpp.i

generated_files/obj/Perl5ToCpp_wrap.o: generated_files/Perl5ToCpp_wrap.cpp
	g++ -c -Wno-literal-suffix -D_REENTRANT -D_GNU_SOURCE -DPERL_USE_SAFE_PUTENV -fno-strict-aliasing -pipe -fstack-protector -D_LARGEFILE_SOURCE -D_FILE_OFFSET_BITS=64 -O2 -fPIC -m64 -I /opt/python/3.11/linux/RHEL70/include/python3.11/ generated_files/Perl5ToCpp_wrap.cpp -I cpp/ -o generated_files/obj/Perl5ToCpp_wrap.o

generated_files/_Perl5ToCpp.so: generated_files/obj/pointers1.o generated_files/obj/std_lib.o generated_files/obj/Callback.o generated_files/obj/Perl5ToCpp_wrap.o
	g++ -shared generated_files/obj/std_lib.o generated_files/obj/Callback.o generated_files/obj/Perl5ToCpp_wrap.o -o generated_files/_Perl5ToCpp.so -L/opt/python/3.11/linux/RHEL70/lib -lpython3.11

#=========================================== generic phony
all: generated_files/_Perl5ToCpp.so

clean:
	rm -f generated_files/obj/Callback.o generated_files/obj/std_lib.o generated_files/obj/pointers1.o
	rm -f generated_files/_Perl5ToCpp.so generated_files/Perl5ToCpp_wrap.cpp generated_files/Perl5ToCpp.py generated_files/obj/Perl5ToCpp_wrap.o

#========================================================
# file:///C:/src/swigwin-4.1.1/Examples/perl5/callback/index.html
# 
# 
#==========================================================