

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
#=================================================

print $p,"perl code started here";
print $p," ==============================";
print $p," ==============================  read global variable STDLib::moduleName \n";

print $p, " STDLib::moduleName = ", $STDLib::moduleName;
$STDLib::moduleName = "STD_LIB";
print $p, " STDLib::moduleName = ", $STDLib::moduleName;

print $p," ==============================  read CONST global variable STDLib::fileName \n";

print $p, " STDLib::fileName = ", $STDLib::fileName;

# $STDLib::fileName = "STR.CPP";    #ERROR : Value is read-only. at perl/str.pl line 28.
                                    #[PERL CODE]:	 STDLib::fileName = str.hmake: *** [str] Error 255

print $p, " STDLib::fileName = ", $STDLib::fileName;


print $p," ==============================  STDLib::UpdateStr(\"{My PERL text}\") \n";
my $perltxt= "{My PERL text}";
my $cpptxt = STDLib::UpdateStr($perltxt);
print $p, " returned cpptxt = ", $cpptxt;

print $p," ==============================  STDLib::PrintStr(\"{My PERL text}\") \n";
STDLib::PrintStr($perltxt);


print $p," ==============================  STDLib::changePerlStr(\"{My PERL text-2}\") \n";
my $perltxt2= "{My PERL text-2}";
print $p, " my  perltxt2 = ", $perltxt2;

# my $cpptxt2 = STDLib::changePerlStr($perltxt2);
#ERROR: TypeError in method 'changePerlStr', argument 1 of type 'std::string &' at perl/str.pl line 44.
#[PERL CODE]:	 my  perltxt2 = {My PERL text-2}make: *** [str] Error 255


#print $p, " returned cpptxt2 = ", $cpptxt2;
#print $p, " after STDLib::changePerlStr()-  perltxt2 = ", $perltxt2;



print $p," ==============================  STDLib::changePerlStrPtr(\"{My PERL text-2}\") \n";
my $perltxt2= "{My PERL text-2}";
print $p, " my  perltxt2 = ", $perltxt2,"\n";

my $cpptxt2 = STDLib::changePerlStrPtr($perltxt2);

print $p, " returned cpptxt2 = ", $cpptxt2,"\n";
print $p, " after STDLib::changePerlStr()-  perltxt2 = ", $perltxt2,"\n";

print $p," ==============================  my s1 = new STDLib::StrTest() and s1->{m_perltxt}\n";
my $s1 = new STDLib::StrTest();

print $p," ==============================  s1->{m_perltxt} \n";
print $p, " s1->m_perltxt = ", $s1->{m_perltxt};

$s1->{m_perltxt} = "new PERL String";

print $p, " s1->m_perltxt = ", $s1->{m_perltxt};

print $p," ==============================  cpptxt = s1->UpdateStr(perltxt); \n";
$cpptxt = $s1->UpdateStr($perltxt);

print $p, " returned cpptxt = ", $cpptxt;

print $p," ==============================  STDLib::StrTest::m_fileName \n";

print $p, " STDLib::StrTest::m_fileName = ", $STDLib::StrTest::m_fileNam,"\n";

#$STDLib::StrTest::m_fileName= "STR.CPP";
# eRROR: Value is read-only. at perl/str.pl line 82.


print $p, " STDLib::StrTest::m_fileName = ", $STDLib::StrTest::m_fileName,"\n";



print $p," ==============================\n";
print $p," perl code ended here\n\n";
print $p," ==============================\n";




exit;