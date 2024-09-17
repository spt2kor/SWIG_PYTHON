#!/opt/perl_5.18.2/bin/perl

BEGIN {
    push ( @INC,"./generated_files/");
    push ( @INC,"./perl/");
}
use Data::Dumper;
use SimpleDS;
use Scalar::Util qw(reftype);

my $p = "\n[PERL CODE]:\t";

print $p,"\n perl code started here";
print $p," ==============================";
print $p," ============================== SimpleDS::Singleton::count() and  1ST getInstance()\n";

print $p,"calling SimpleDS::Singleton::count() \n" ;
my $c = SimpleDS::Singleton::count();
print $p,"Singleton::count() =  $c \n" ;   #[PERL CODE]:	Singleton::count() =  _p_uint=HASH(0x2559758)


print $p," calling SimpleDS::Singleton::getInstance() \n";
my $inst = SimpleDS::Singleton::getInstance();
print $p," inst = $inst";
                            
print $p," calling SimpleDS::Singleton::count() \n";
$c = SimpleDS::Singleton::count();
print $p,"Singleton::count() =  $c \n" ;

print $p," ============================== inst->set(20,50)\n";
$inst->set(20,50);

print $p," calling inst->show()\n";
$inst->show();

print $p," ============================== 2nd - SimpleDS::Singleton::getInstance()\n";
my $inst2 = SimpleDS::Singleton::getInstance();
print "\n instr2 = $inst2 \n";

print $p," calling SimpleDS::Singleton::count() \n";
$c = SimpleDS::Singleton::count();
print $p,"Singleton::count() =  $c \n" ;

print $p," calling inst2->show() \n";
$inst2->show();

print $p," ============================== SimpleDS::Singleton::DestroyInstance()\n ";

print $p," SimpleDS::Singleton::destroyInstance() \n";
#SimpleDS::Singleton::destroyInstance();#RuntimeError Usage: Singleton_destroyInstance(self); at perl/Singleton.pl line 50.
#$inst->destroyInstance();# not working
SimpleDS::Singleton::destroyInstance($inst);#Works

print $p," calling SimpleDS::Singleton::count() \n";
$c = SimpleDS::Singleton::count();
print $p,"Singleton::count() =  $c \n" ;

print $p," calling inst2->show() \n";
$inst2->show();

print $p," ============================== inst->DESTROY()\n ";
#$inst->DESTROY();

print $p," perl code ended here\n\n";
print $p," ==============================\n";


#NOTE: check function scope calls DTOR(), 
#PERL class object, get DTOR by default, at func exit.



exit;
