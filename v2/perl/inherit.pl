#!/opt/perl_5.18.2/bin/perl

BEGIN {
    push ( @INC,"./generated_files/");
    push ( @INC,"./perl/");
}
use Data::Dumper;
use SimpleDS;
use Scalar::Util qw(reftype);

my $p = "\n[PERL CODE]:\t";

print $p,"perl code started here";
print $p," ==============================";

print $p,' creating Rectangle object , rect = new SimpleDS::Rectangle("Rect-0",5,6)',"\n";
my $rect = new SimpleDS::Rectangle("Rect-0",5,6);
print $p," ==============================";
print $p," calling rect->show(), rect => $rect\n";
$rect->show();
print $p," ==============================";
print $p," calling Rectangle::classInfo()\n";
SimpleDS::Rectangle::classInfo();
print $p," ============================== copy CTOR()"; 
print $p,' creating Rectangle object , my $rect1 = new SimpleDS::Rectangle($rect);',"\n";
my $rect1 = new SimpleDS::Rectangle($rect);


print $p,' calling , $rect1->show();',"\n";
$rect1->show();
print $p,' calling , $rect1->setName("Rect-1");',"\n";
$rect1->setName("Rect-1"); #Can't locate object method "setName" via package "SimpleDS::Rectangle" at perl/inherit.pl line 30.
print $p,' calling , $rect1->show();',"\n";
$rect1->show();

print $p," ============================== clone()"; 
print $p," calling rect2 = rect->clone()\n";
my $rect2 = $rect->clone();
$rect2->show();
$rect2->setName("Rect-2");
$rect2->show();
print $p," ============================== copy()"; 
print $p,' calling $rect2->copy($rect);',"\n";
$rect2->copy($rect);
$rect2->show();
$rect2->setName("Rect-2");
$rect2->show();

print $p," ============================== copy CTOR()"; 
print $p," calling rect3 = new SimpleDS::Rectangle(rect), rect => $rect\n";
my $rect3 = new SimpleDS::Rectangle($rect);
print $p," calling rect3->show(), rect3 => $rect3\n";
$rect3->show();
$rect3->setName("Rect-3");
$rect3->show();

print $p," ============================== operator=(), shallow copy"; 
print $p," calling rect3 = rect\n";
$rect3 = $rect;
$rect3->show();
$rect3->setName("Rect-3");
$rect3->show();

print $p," ==============================";
#NOTE: object copy does not call C++ operator=(), it clone in PERL alsone, and deref/delete C++ object
print $p," ============================== show()";
print $p," calling rect->show(), rect => $rect\n";
$rect->show();
print $p," ============================== DESTROY(), ~DTOR()";

print $p," calling rect->DESTROY(), rect => $rect\n";
$rect->DESTROY();
print $p," after rect->DESTROY(), rect => $rect\n";
$rect->DESTROY(); #didnot call the DTOR second time, but didnot report any error
print $p," after rect->DESTROY(), rect => $rect\n";

print $p," ============================== show() after destroy()";
print $p," calling rect3->show(), rect3 => $rect3\n";
#$rect3->show();#make: *** [inh] Segmentation fault , because rect3 & rect both are already destroyed, 
print $p," calling rect->show(), rect => $rect\n";
#$rect->show();#make: *** [inh] Segmentation fault , because rect3 & rect both are already destroyed, 

print $p," ============================== privateFunc()";
#$rect3->privateFunc();
#Can't locate object method "privateFunc" via package "SimpleDS::Rectangle" at perl/class.pl line 88.

print $p," ============================== protctedFunc()";
#$rect3->protctedFunc();
#Can't locate object method "protctedFunc" via package "SimpleDS::Rectangle" at perl/class.pl line 92.

print $p,' ============================== returnSelfRef() ',"\n";
print $p," calling rect2->show(), rect2 => $rect2\n";
$rect2->show();
print $p,' calling my $rect4 = $rect2->returnSelfRef(); ',"\n";
my $rect4 = $rect2->returnSelfRef();
print $p," calling rect4->show(), rect3 => $rect4\n";
$rect4->show();

print $p,' ============================== returnSelfPtr() ',"\n";
print $p,' calling my $rect5 = $rect2->returnSelfPtr(); ',"\n";
my $rect5 = $rect2->returnSelfPtr();
print $p," calling rect5->show(), rect5 => $rect5\n";
$rect5->show();

print $p,' ============================== Rectangle* createRectangle() ',"\n";
print $p,' calling my $rect6 = SimpleDS::createRectangle( "Rect-6", 22 , 44 ); ',"\n";

{# not working
    my $rect6 = SimpleDS::createRectangle( "Rect-6", 22 , 44 );
    print $p," calling rect6->show(), rect6 => $rect6\n";
    $rect6->show();
}

#NOTE 
# by default at the end of perl code, perl objects/ref deleted, they delete there c++ counterpart objects(only)
#perl object who holds C++ ref/ptr, dont trigger DTOR
#so if c++ code return ptr/ref, he has to take care of deletion

print $p," ==============================";

print "\n SimpleDS::arr = $SimpleDS::arr";
print "\n SimpleDS::arr = $SimpleDS::arr[2]";
print "\n SimpleDS::arr = @SimpleDS::arr";
my @arr1 = $SimpleDS::arr;
print "\n arr1 = @arr1";
print "\n arr1[1] = $arr1[1]";

#Accumulate
print $p," perl code ended here\n\n";
print $p," ==============================\n";






exit;
