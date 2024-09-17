

#!/opt/perl_5.18.2/bin/perl

BEGIN {
    push ( @INC,"./generated_files/");
    push ( @INC,"./perl/");
}
use Data::Dumper;
use Perl5ToCpp;
use Scalar::Util qw(reftype);
my $p = "\n[PERL CODE]:\t";

#=================================================
#=================================================

print $p,"perl code started here";
print $p," ==============================";
print $p," ==============================  new Perl5ToCpp::new_IntTransformer() \n";
my $a = new_IntTransformer(3);           # Create an array
$a[0] =100;
$a[1] =200;
$a[2] =300;
print $p," ==============================  new Perl5ToCpp::Transform() \n";
Perl5ToCpp::Transform($a);                    # Pass to C

print $p," a[1] = $a[1] ";
print $p," ==============================  new Perl5ToCpp::delete_IntTransformer() \n";

delete_IntTransformer($a);             # Destroy array

print $p," perl code ended here\n\n";
print $p," ==============================\n";




exit;