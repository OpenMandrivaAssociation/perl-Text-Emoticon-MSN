%define upstream_name    Text-Emoticon-MSN
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	6

Summary:	Emoticon filter of MSN Messenger
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/Text-Emoticon-MSN
Source0:	https://cpan.metacpan.org/authors/id/M/MI/MIYAGAWA/Text-Emoticon-MSN-%{upstream_version}.tar.gz

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
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 655232
- rebuild for updated spec-helper

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 471418
- import perl-Text-Emoticon-MSN


* Sun Nov 29 2009 cpan2dist 0.04-1mdv
- initial mdv release, generated with cpan2dist
