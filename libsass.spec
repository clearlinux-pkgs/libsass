#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libsass
Version  : 3.5.4
Release  : 9
URL      : https://github.com/sass/libsass/archive/3.5.4.tar.gz
Source0  : https://github.com/sass/libsass/archive/3.5.4.tar.gz
Summary  : A C/C++ implementation of a Sass compiler
Group    : Development/Tools
License  : MIT
Requires: libsass-lib
Requires: libsass-license
Patch1: build.patch
Patch2: cve-2018-11696.patch

%description
LibSass is a C/C++ port of the Sass engine. The point is to be simple, fast, and easy to integrate.

%package dev
Summary: dev components for the libsass package.
Group: Development
Requires: libsass-lib
Provides: libsass-devel

%description dev
dev components for the libsass package.


%package lib
Summary: lib components for the libsass package.
Group: Libraries
Requires: libsass-license

%description lib
lib components for the libsass package.


%package license
Summary: license components for the libsass package.
Group: Default

%description license
license components for the libsass package.


%prep
%setup -q -n libsass-3.5.4
%patch1 -p1
%patch2 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1531954364
export CFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FCFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export FFLAGS="$CFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
export CXXFLAGS="$CXXFLAGS -fstack-protector-strong -mzero-caller-saved-regs=used "
%reconfigure --disable-static
make  %{?_smp_mflags} BUILD=shared

%install
export SOURCE_DATE_EPOCH=1531954364
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/libsass
cp LICENSE %{buildroot}/usr/share/doc/libsass/LICENSE
cp COPYING %{buildroot}/usr/share/doc/libsass/COPYING
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/include/sass/base.h
/usr/include/sass/context.h
/usr/include/sass/functions.h
/usr/include/sass/values.h
/usr/include/sass/version.h
/usr/lib64/libsass.so
/usr/lib64/pkgconfig/libsass.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsass.so.1
/usr/lib64/libsass.so.1.0.0

%files license
%defattr(-,root,root,-)
/usr/share/doc/libsass/COPYING
/usr/share/doc/libsass/LICENSE
