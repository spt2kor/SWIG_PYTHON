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

print $p," creating Rectangle object , rect = new SimpleDS::Rectangle(5,6)\n";
my $rect = new SimpleDS::Rectangle(5,6);
print $p," ==============================";
print $p," calling rect->show(), rect => $rect\n";
$rect->show();
print $p," ==============================";
print $p," calling rect->area() :returned result value = ",$rect->area(),"     \n";
print $p," ==============================";
print $p," calling Rectangle::classInfo()\n";
#Rectangle::classInfo();           #=>Undefined subroutine &Rectangle::classInfo called at perl/client.pl line 45.
#$rect->classInfo();  # RuntimeError Usage: Rectangle_classInfo(); at perl/client.pl line 47.
#Rectangle::Rectangle_classInfo();       # Undefined subroutine &Rectangle::Rectangle_classInfo called at perl/client.pl line 49.
SimpleDS::Rectangle::classInfo();
print $p," ============================== clone()"; 
print $p," calling rect2 = rect->clone()\n";
my $rect2 = $rect->clone();
print $p," ============================== copy()"; 
print $p,' calling $rect2->copy($rect);',"\n";
$rect2->copy($rect);
print $p," ============================== show()";
print $p," calling rect2->show(), rect2 => $rect2\n";
$rect2->show();
print $p," ==============================";
print $p," =============================="; 
print $p," calling rect3 = new SimpleDS::Rectangle(rect), rect => $rect\n";
my $rect3 = new SimpleDS::Rectangle($rect);
print $p," ==============================";
print $p," calling rect3->show(), rect3 => $rect3\n";
$rect3->show();
print $p," ============================== operator=(), shallow copy"; 
print $p," calling rect3 = rect\n";
$rect3 = $rect;
print $p," ==============================";
#NOTE: object copy does not call C++ operator=(), it clone in PERL alsone, and deref/delete C++ object
print $p," ============================== show()";
print $p," calling rect3->show(), rect3 => $rect3\n";
$rect3->show();
print $p," calling rect->show(), rect => $rect\n";
$rect->show();
print $p," ============================== Dumper(rect)\n";

print Dumper(\%$rect);

print "\n","@{[%rect]}";

print $p," ============================== DESTROY(), ~DTOR()";

print $p," calling rect->DESTROY(), rect => $rect\n";
$rect->DESTROY();
print $p," after rect->DESTROY(), rect => $rect\n";
$rect->DESTROY();
print $p," after rect->DESTROY(), rect => $rect\n";

print $p," ============================== show()";
print $p," calling rect3->show(), rect3 => $rect3\n";
$rect3->show();
print $p," calling rect->show(), rect => $rect\n";
$rect->show();
print $p," ============================== char* passCharPtr(char*)\n";

my $str1 = "[its a PERL string]";
print $p, "str1 = ",$str1,", \\str1 = ",\$str1;

print $p," calling SimpleDS::passCharPtr( str1 )\n";

my $str2 = SimpleDS::passCharPtr( $str1 );
print $p, "str2 = ",$str2,", \\str2 = ",\$str2;

print $p ,"reftype(str1): " , reftype($str1) ,"ref(str1): " , ref($str1) , "\n";
print $p, "base type of str2: " . reftype($str2) . "\n";

print $p," ============================== privateFunc()";
#$rect3->privateFunc();
#Can't locate object method "privateFunc" via package "SimpleDS::Rectangle" at perl/class.pl line 88.

print $p," ============================== protctedFunc()";
#$rect3->protctedFunc();
#Can't locate object method "protctedFunc" via package "SimpleDS::Rectangle" at perl/class.pl line 92.


print $p," ============================== Rectangle* = createRectangle()";
my $rect4 = createRectangle(20,30);
#print $p ,"reftype(rect4): " , reftype($rect4) ,"ref(rect4): " , ref($rect4) , ", rect4 = ",$rect4,"\n";
$rect4->show();

print $p," ==============================";

print $p," perl code ended here\n\n";







exit;