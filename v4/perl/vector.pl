

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
    my $vi = $_[0];
    print $p," ==============================  print vector \n";
    for($i = 1; $i <=5 ; $i++)
    {
        print $p , "$i , value = " , $vi->get($i-1);
    } 
    print "\n";
}
#=================================================

print $p,"perl code started here";
print $p," ==============================";
print $p," ==============================  create STDLib::vectori \n";
my $vi1 = new STDLib::vectori(5);
print $p, " vi1 = ", $vi1 , "\n";
print $p, " vi1.size() = ", $vi1->size() , "\n";

print $p," ==============================  add values to vector \n";

for($i = 1; $i <=5 ; $i++)
{
    #vi1[$i] = $i+ 5;
    $vi1->set($i-1 , $i+5  );
}

Print($vi1);

my $vi2 = new STDLib::vectori($vi1);
Print($vi2);

print $p," ==============================   double average(std::vector<int> v); \n";

print $p, " average(vi1) = ", STDLib::average($vi1) , "\n";

print $p," ==============================   std::vector<double> half(const std::vector<double>& v) ; \n";
my $vd1 = new STDLib::vectord(5);
for($i = 1; $i <=5 ; $i++)
{
    #vi1[$i] = $i+ 5;
    $vd1->set($i-1 , $i+20  );
}

Print($vd1);

my $vd2 = STDLib::half($vd1);

#Print($vd2);
#Can't call method "get" on unblessed reference at perl/vector.pl line 18.
#make: *** [vec] Error 255



print $p," ==============================   void halve_in_place(std::vector<double>& v) ; \n";

my $vd3 = new STDLib::vectord(5);
for($i = 1; $i <=5 ; $i++)
{
    #vi1[$i] = $i+ 5;
    $vd3->set($i-1 , $i+10  );
}

Print($vd3);

STDLib::halve_in_place($vd3);

Print($vd3);

print $p," ==============================   passing PERL array's ; \n";
my @arr1 = (20,30,40,50);
print $p," arr1 = ", @arr1, "\n";
#print $p, " average(arr1) = ", STDLib::average(@arr1) , "\n";
#RuntimeError Usage: average(v); at perl/vector.pl line 86.
#make: *** [vec] Error 255

#my $vd10 = STDLib::half(@arr1);
#RuntimeError Usage: half(v); at perl/vector.pl line 88.
#make: *** [vec] Error 255


#STDLib::halve_in_place(@arr1);
#RuntimeError Usage: halve_in_place(v); at perl/vector.pl line 90.
#make: *** [vec] Error 255

print $p," ==============================   passing PERL's List  ; \n";
#print $p, " average(arr1) = ", STDLib::average( 10,20,30,40 ) , "\n";
#RuntimeError Usage: average(v); at perl/vector.pl line 100.
#make: *** [vec] Error 255


#print $p," ==============================   bool operator==(const std::vector<double>& v1 , const std::vector<double>& v2 ) ;  \n";
#my $vd10 = new STDLib::vectord(5);
#for($i = 1; $i <=5 ; $i++)
#{
    #vi1[$i] = $i+ 5;
#    $vd10->set($i-1 , $i+20  );
#}
#my $compRes = STDLib::operator==($vd1 , $vd10);
#print $p, " STDLib::operator==(vd1 , vd10); = ", $compRes , "\n";
# not working

print $p," ==============================\n";
print $p," perl code ended here\n\n";
print $p," ==============================\n";




exit;