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
print $p," ==============================  new Perl5ToCpp::new_intp() \n";
$a = Perl5ToCpp::new_intp();
$b = Perl5ToCpp::new_intp();
$c = Perl5ToCpp::new_intp();
print $p," ==============================  new Perl5ToCpp::intp_assign() \n";
Perl5ToCpp::intp_assign($a,37);
Perl5ToCpp::intp_assign($b,42);

print $p,"     a = $a\n";
print $p,"     b = $b\n";
print $p,"     c = $c\n";
print $p," ==============================  new Perl5ToCpp::addition() \n";
# Call the addition() function with some pointers
Perl5ToCpp::addition($a,$b,$c);
print $p," ==============================  new Perl5ToCpp::intp_value() \n";
# Now get the result
$r = Perl5ToCpp::intp_value($c);
print $p,"     37 + 42 = $r\n";
print $p," ==============================  new Perl5ToCpp::delete_intp() \n";
# Clean up the pointers
Perl5ToCpp::delete_intp($a);
Perl5ToCpp::delete_intp($b);
Perl5ToCpp::delete_intp($c);

# Now try the typemap library
# This should be much easier. Now how it is no longer
# necessary to manufacture pointers.
print $p," ==============================  new Perl5ToCpp::subtract() \n";
print $p,"Trying the typemap library\n";
$r = Perl5ToCpp::subtract(37,42);
print $p,"     37 - 42 = $r\n";

# Now try the version with multiple return values
print $p," ==============================  new Perl5ToCpp::divide() \n";
print $p,"Testing multiple return values\n";
($q,$r) = Perl5ToCpp::divide(42,37);
print $p,"     42/37 = $q remainder $r\n";

print $p," ==============================  cb1->DISOWN() \n";


print $p," ==============================  new Perl5ToCpp::new_double_p() \n";
# Clean up the pointers
$d1 = Perl5ToCpp::new_double_p();
Perl5ToCpp::double_p_assign($d1,42.987654);

print $p,"     d1 = $d1\n";
$dr1 = Perl5ToCpp::double_p_value($d1);
print $p,"     dr1 = $dr1\n";
Perl5ToCpp::delete_double_p($d1);



print $p," perl code ended here\n\n";
print $p," ==============================\n";




exit;
