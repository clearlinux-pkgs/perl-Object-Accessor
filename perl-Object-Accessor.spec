#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v21
# autospec commit: 94c6be0
#
Name     : perl-Object-Accessor
Version  : 0.48
Release  : 16
URL      : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Object-Accessor-0.48.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Object-Accessor-0.48.tar.gz
Summary  : 'Per object accessors'
Group    : Development/Tools
License  : Artistic-1.0-Perl
Requires: perl-Object-Accessor-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
object accessors.
Please refer to 'perldoc Object::Accessor' after installation for
details.

%package dev
Summary: dev components for the perl-Object-Accessor package.
Group: Development
Provides: perl-Object-Accessor-devel = %{version}-%{release}
Requires: perl-Object-Accessor = %{version}-%{release}

%description dev
dev components for the perl-Object-Accessor package.


%package perl
Summary: perl components for the perl-Object-Accessor package.
Group: Default
Requires: perl-Object-Accessor = %{version}-%{release}

%description perl
perl components for the perl-Object-Accessor package.


%prep
%setup -q -n Object-Accessor-0.48
cd %{_builddir}/Object-Accessor-0.48

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Object::Accessor.3

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
