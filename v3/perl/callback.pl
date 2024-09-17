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
{
    package PlCallback;
    #use base 'Perl5ToCpp::Callback';
    our @ISA = qw(Perl5ToCpp::Callback);

    sub run {
        print "\n[PERL CODE]:\t","Inside PlCallback->run() \n";
    }
    sub new {
        print "\n[PERL CODE]:\t","PlCallback::PlCallback() Enter\n";
        my $class = shift;
        #my $self = {};
        my $self = $class->SUPER::new( ); # calling base class CTOR
        
        bless $self, $class;
        print "\n[PERL CODE]:\t","PlCallback::PlCallback() Exit\n";
        return $self;
    }   
    sub DESTROY {
        print "\n[PERL CODE]:\t","PlCallback::DESTROY() Enter\n";
        my $class = shift;
        my $self = $class->SUPER::run( ); # calling base class CTOR # //TEST
        $class->SUPER::DESTROY();
        print "\n[PERL CODE]:\t","PlCallback::DESTROY() Exit\n";
    }

}
#=================================================

print $p,"perl code started here";
print $p," ==============================";
print $p," ==============================  new Perl5ToCpp::Callback() \n";
my $cb1 = new Perl5ToCpp::Callback();
#$cb1 = Perl5ToCpp::Callback;
print $p,"cb1 = $cb1 \n ";
print $p,"address(cb1) = ", \$cb1 , "\n";

print $p,"calling cb1->run() \n ";
#$cb1.run(); #Undefined subroutine &main::run called at perl/callback.pl line 31.
$cb1->run();

print $p," ==============================  cb1->DISOWN() \n";
$cb1->DISOWN();

print $p," ==============================  new Perl5ToCpp::Caller() \n";
my $clr = new Perl5ToCpp::Caller();
print $p,"clr = $clr \n ";

print $p,"calling clr->setCallback(cb1); \n ";
$clr->setCallback($cb1);

print $p,"calling clr->call() \n ";
$clr->call();

print $p," ==============================  new PlCallback::Callback() \n";
#my $cb2 = new PlCallback::Callback();

my $cb2 = PlCallback->new(); # calling c++ bsae class CTOR, but not executing PlCallback::Run()

#------------------------------------------------------------------------
#my $cb2 = new PlCallback(); 
# with PlCallback::new(), calling its own CTOR, but not calling base CTOR, but 
#ypeError in method 'Caller_setCallback', argument 2 of type 'Callback *' at perl/callback.pl line 67.

print $p,"cb2 = $cb2 \n ";

print $p,"calling cb2->run() \n ";
$cb2->run();

print $p," ==============================  cb2->DISOWN() \n";
$cb2->DISOWN();

print $p,"calling clr->setCallback(cb2); \n ";
$clr->setCallback($cb2);

print $p,"calling clr->call() \n ";
$clr->call();
#print $p," ============================== cb1->DESTROY() \n";
#$cb1->DESTROY();
#$cb2->DESTROY(); //does not call base class DTOR

print $p," ==============================  using namespace \n";

print $p,"calling res = Perl5ToCpp::Math::add(10,20); \n ";
#my $res = Perl5ToCpp::Math::add(10,20);
#Undefined subroutine &Perl5ToCpp::Math::add called at perl/callback.pl line 96.
#print $p," res = $res\n ";

my $res = Perl5ToCpp::add(10,20);
print $p," res = $res\n ";

print $p,"calling a1 = new Perl5ToCpp::Math::Add(); \n ";
my $a1 = new Perl5ToCpp::Add();

print $p,"calling res = a1->add(40,50); \n ";
$res = $a1->add(40,50);
print $p," res = $res\n ";

print $p,"calling a1->{m_sum} = $a1->{m_sum}; \n ";

print $p," perl code ended here\n\n";
print $p," ==============================\n";




exit;
