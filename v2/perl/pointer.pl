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
print $p," ============================== pointer.h/.cpp ADD";

my ($x,$y) = (10,30);
my $res=9999;
$res = SimpleDS::execute_op($x, $y ,$SimpleDS::ADD);
print "\n res = $res";

print $p," ============================== ";
print $p," perl code ended here\n\n";
print $p," ==============================\n";
# namespce, int* , class*, int(), class(), int arr[10] , class[10] , vector, string, map

exit;
