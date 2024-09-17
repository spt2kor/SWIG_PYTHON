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
print $p," ============================== pointer.h/.cpp ADD\n";

my ($x,$y) = (100,20);
my $res=9999;
#SimpleDS::divide($x, $y ,$res);# TypeError in method 'divide', argument 1 of type 'int *' at perl/Pointer1.pl line 19.


my $xr = \$x;

SimpleDS::divide($xr, $y ,$res);

print "\n res = $res";

print $p," ============================== ";


print $p," ============================== ";


print $p," ============================== ";

print $p," ==============================\n";
#$a1->DESTROY();

print $p," perl code ended here\n\n";
print $p," ==============================\n";


# namespce, int* , class*, int(), class(), int arr[10] , class[10] , vector, string, map



exit;
