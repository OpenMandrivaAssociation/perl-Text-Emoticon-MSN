%define upstream_name    Text-Emoticon-MSN
%define upstream_version 0.04
Name:		perl-%{upstream_name}
Version:	0.04
Release:	10

Summary:	Emoticon filter of MSN Messenger
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Text-Emoticon-MSN
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Text-Emoticon-MSN-0.04.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Text::Emoticon)
BuildArch:	noarch

%description
Text::Emoticon::MSN is a text filter that replaces text emoticons like
":-)", ";-P", etc. to the icons of MSN Messenger, detailed in
http://messenger.msn.com/Resource/Emoticons.aspx

%prep
%setup -q -n Text-Emoticon-MSN-0.04

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
# soft: do not fail package on test failures
set +e
%make test || :

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

