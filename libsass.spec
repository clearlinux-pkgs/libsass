#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : libsass
Version  : 3.6.5
Release  : 25
URL      : https://github.com/sass/libsass/archive/3.6.5/libsass-3.6.5.tar.gz
Source0  : https://github.com/sass/libsass/archive/3.6.5/libsass-3.6.5.tar.gz
Summary  : A C/C++ implementation of a Sass compiler
Group    : Development/Tools
License  : MIT
Requires: libsass-lib = %{version}-%{release}
Requires: libsass-license = %{version}-%{release}
Patch1: build.patch

%description
LibSass is a C/C++ port of the Sass engine. The point is to be simple, fast, and easy to integrate.

%package dev
Summary: dev components for the libsass package.
Group: Development
Requires: libsass-lib = %{version}-%{release}
Provides: libsass-devel = %{version}-%{release}
Requires: libsass = %{version}-%{release}

%description dev
dev components for the libsass package.


%package lib
Summary: lib components for the libsass package.
Group: Libraries
Requires: libsass-license = %{version}-%{release}

%description lib
lib components for the libsass package.


%package license
Summary: license components for the libsass package.
Group: Default

%description license
license components for the libsass package.


%prep
%setup -q -n libsass-3.6.5
cd %{_builddir}/libsass-3.6.5
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1664932547
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%reconfigure --disable-static
make  %{?_smp_mflags}  BUILD=shared

%install
export SOURCE_DATE_EPOCH=1664932547
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/libsass
cp %{_builddir}/libsass-%{version}/COPYING %{buildroot}/usr/share/package-licenses/libsass/dc6b6d4b9ae804ab0dd95d46d148ee533bec260f || :
cp %{_builddir}/libsass-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/libsass/4d640cc322117dec7f97632e6ed4319131a16ad2 || :
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/sass.h
/usr/include/sass/base.h
/usr/include/sass/context.h
/usr/include/sass/functions.h
/usr/include/sass/values.h
/usr/include/sass/version.h
/usr/include/sass2scss.h
/usr/lib64/libsass.so
/usr/lib64/pkgconfig/libsass.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libsass.so.1
/usr/lib64/libsass.so.1.0.0

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/libsass/4d640cc322117dec7f97632e6ed4319131a16ad2
/usr/share/package-licenses/libsass/dc6b6d4b9ae804ab0dd95d46d148ee533bec260f
