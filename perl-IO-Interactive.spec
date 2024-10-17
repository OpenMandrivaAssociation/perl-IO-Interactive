%define upstream_name    IO-Interactive
%define upstream_version 0.0.6

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Utilities for interactive I/O
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Test::More)
BuildRequires:	perl(version)
BuildArch:	noarch

%description
This module provides three utility subroutines that make it easier to
develop interactive applications...

* 'is_interactive()'

  This subroutine returns true if '*ARGV' and the currently selected
  filehandle (usually '*STDOUT') are connected to the terminal. The test is
  considerably more sophisticated than:

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
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Funda Wang <fwang@mandriva.org> 0.0.6-2mdv2011.0
+ Revision: 654222
- rebuild for updated spec-helper

* Sat Nov 14 2009 Jérôme Quelin <jquelin@mandriva.org> 0.0.6-1mdv2011.0
+ Revision: 465995
- update to 0.0.6

* Fri Jul 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.0.5-1mdv2010.0
+ Revision: 394290
- import perl-IO-Interactive


* Fri Jul 10 2009 cpan2dist 0.0.5-1mdv
- initial mdv release, generated with cpan2dist
