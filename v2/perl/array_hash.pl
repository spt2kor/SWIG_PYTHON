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
print $p," ============================== C++ int arr[5]";

print "\n SimpleDS::arr = $SimpleDS::arr";
print "\n SimpleDS::arr = $SimpleDS::arr[2]";
print "\n SimpleDS::arr = @SimpleDS::arr";
my @arr1 = $SimpleDS::arr;
print "\n arr1 = @arr1";
print "\n arr1[1] = $arr1[1]";

print $p," ============================== C++ Accumulate(int arr[5]);";
my @ar = (3,6,9,12,15);
print $p, "\n PERL ar = @ar \n";
print $p,' calliung  my $sum = $SimpleDS::Accumulate(@ar) ',"\n";
#my $sum = $SimpleDS::Accumulate(@ar);
#print $p, "\n PERL sum = $sum \n";

print $p," ============================== Struct Algo";
print $p,' calling my $a1 = new SimpleDS::Algo(); ',"\n";
my $a1 = new SimpleDS::Algo(10);
# my $a2 = SimpleDS::Algo(10); # NOTE: does it work?

print $p,' calling  a1->print(); , a1 = ', $a1,"\n";
$a1->print();

print $p,' calling  a1->pub =  ', $a1->{pub},"\n";

print $p," ============================== check Array\n";
#my $a1 = malloc_SimpleDS(5);

print $p," ============================== Factory base class\n";
#C:\src\swigwin-4.1.1\Lib\typemaps\factory.swg

#my $cir1 = SimpleDS::Geometry::create(SimpleDS::Geometry::GeomType::CIRCLE);
#TypeError in method 'Geometry_create', argument 1 of type 'Geometry::GeomType' at perl/array_hash.pl line 44.
my $cir1 = SimpleDS::Geometry::create(2); #Geometry* -> Circle();
print $p,"calling cir1->draw(), return value = ",$cir1->draw()," \n";


print $p,"calling SimpleDS::Geometry::destroy(\$cir1) \n";
SimpleDS::Geometry::destroy($cir1);

print $p," ============================== implicit conversion\n";
print $p,"calling SimpleDS::getAii(5000), return value = ",SimpleDS::getAii(5000)," \n";

print $p," ==============================\n";
$a1->DESTROY();

print $p," perl code ended here\n\n";
print $p," ==============================\n";


#NOTE: check function scope calls DTOR(), 
#PERL class object, get DTOR by default, at func exit.



exit;
