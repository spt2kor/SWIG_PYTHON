

#!/opt/perl_5.18.2/bin/perl

BEGIN {
    push ( @INC,"./generated_files/");
    push ( @INC,"./perl/");
}
use Data::Dumper;
use STDLib;
use Scalar::Util qw(reftype);
my $p = "\n[PERL CODE]:\t";

#=================================================
sub Print {
    my $map = $_[0];
    print $p," ==============================  print map =", $map , "\n";
    for($i = 1; $i <=5 ; $i++)
    {
        print $p , "key = $i , value = " , $map->get($i);
    } 
    print "\n";
}

sub PrintMap {
    my $keys1 = $_[0];
    my @keys = @$keys1;
    my $map = $_[1];
    print $p," ==============================  print map =", $map , "\n";
    for($i = 1; $i <=5 ; $i++)
    {
        my $key = $keys[$i-1];
        #print $p , " $i, key = $key  \n";
        #print $p , ", value = " , $map->get( $key );
        print $p , " $i, key = $key  , value = " , $map->get( $key );

    } 

    print "\n";
}

#=================================================

print $p,"perl code started here";
print $p," ==============================";
print $p," ==============================  create STDLib::map_ii() \n";
my $vi1 = new STDLib::map_ii();
print $p, " vi1 = ", $vi1 , "\n";
print $p, " vi1.size() = ", $vi1->size() , "\n";

print $p," ==============================  add values to map_ii \n";

for($i = 1; $i <=5 ; $i++)
{
    
    $vi1->set($i , $i+55  );
}
print $p, " vi1.size() = ", $vi1->size() , "\n";
Print($vi1);

print $p," ==============================   int printMapII(map<int,int> mp);; \n";

print $p, " printMapII(vi1) = ", STDLib::printMapII($vi1) , "\n";

print $p," ==============================\n";
print $p," ==============================\n";
print $p," ==============================  create STDLib::map_sd() \n";
my $vi2 = new STDLib::map_sd();
print $p, " vi2 = ", $vi2 , "\n";
print $p, " vi2.size() = ", $vi2->size() , "\n";

print $p," ==============================  add values to map_sd \n";

my @keys = ("k1", "k5", "k4", "k3", "k2");
for($i = 1; $i <=5 ; $i++)
{
    $vi2->set($keys[$i -1] , $i+55 + ($i * 0.7) );
}
print $p, " vi2.size() = ", $vi2->size() , "\n";
PrintMap(\@keys , $vi2);

print $p," ==============================   map<string,double> PrintMapCR(const map<string,double> & mp) ; \n";

print $p, " calling printMapII(vi2) = \n";
my $vi3 = STDLib::PrintMapCR($vi2) ;
print $p, " vi3.size() = ", $vi3->size() , "\n";
PrintMap(\@keys , $vi3);




print $p," ==============================\n";
print $p," perl code ended here\n\n";
print $p," ==============================\n";




exit;