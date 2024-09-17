#!/opt/perl_5.18.2/bin/perl

BEGIN {
    push ( @INC,"./generated_files/");
    push ( @INC,"./perl/");
}
use SimpleDS;

my $p = "\n[PERL CODE]:\t";
print $p ," perl code started here";
print $p ," ==============================";

print $p ," ============================== calling global variable SimpleDS::pi" ;
print $p ," global variable SimpleDS::pi = $SimpleDS::pi";

$SimpleDS::pi = 311983;

print $p ," global variable  SimpleDS::pi = $SimpleDS::pi";

print $p ," ============================== calling global macro SimpleDS::RED" ;
print $p ," global macro  SimpleDS::RED = $SimpleDS::RED";

print $p ," ============================== calling global cunction  SimpleDS::calculateArea()";


my $width = 10;
my $height = 7;
my $area1 = SimpleDS::calculateArea( 11 , 22 );
print $p ," SimpleDS::calculateArea($width, $height) = $area1";
#my $area = $SimpleDS::calculateArea( $width , $height );
print $p ," SimpleDS::calculateArea($width, $height) = $area1";
print $p ," ==============================";
print $p ," perl code ended here\n\n";







exit;