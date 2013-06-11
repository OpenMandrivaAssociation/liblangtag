Name: liblangtag
Version: 0.4.0
Release: %mkrel 2
Summary: An interface library to access tags for identifying languages

Group:   System/Internationalization
License: LGPLv3+
URL: https://github.com/tagoh/liblangtag/
Source0: https://github.com/downloads/tagoh/%{name}/%{name}-%{version}.tar.bz2
Patch0: 0001-Fix-build-issues-with-MSVC.patch
Patch1: fix-format-not-a-string-literal.diff
Patch2: fix-linking.diff

BuildRequires: gtk-doc
BuildRequires: libtool
BuildRequires: libxml2-devel

%description
%{name} is an interface library to access tags for identifying
languages.

Features:
* several subtag registry database supports:
  - language
  - extlang
  - script
  - region
  - variant
  - extension
  - grandfathered
  - redundant
* handling of the language tags
  - parser
  - matching
  - canonicalizing

%package devel
Summary: Development files for %{name}
Group: Development/C
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%package doc
Summary: Documentation of %{name} API
Group: Documentation
BuildArch: noarch

%description doc
The %{name}-doc package contains documentation files for %{name}.


%prep
%setup -q
%apply_patches


%build
%configure --disable-static --enable-shared --disable-introspection
sed -i \
    -e 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' \
    -e 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' \
    libtool
%make V=1 \
    LD_LIBRARY_PATH=`pwd`/liblangtag/.libs${LD_LIBRARY_PATH:+:${LD_LIBRARY_PATH}}


%install
%makeinstall_std
rm -f %{buildroot}/%{_libdir}/*.la %{buildroot}/%{_libdir}/%{name}/*.la

%files
%doc AUTHORS COPYING NEWS README
%{_libdir}/%{name}.so.*
%{_libdir}/%{name}/*.so
%{_datadir}/%{name}

%files devel
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

%files doc
%doc COPYING
%{_datadir}/gtk-doc/html/%{name}




%changelog

* Sat Jan 12 2013 umeabot <umeabot> 0.4.0-2.mga3
+ Revision: 357623
- Mass Rebuild - https://wiki.mageia.org/en/Feature:Mageia3MassRebuild

* Mon Dec 17 2012 tv <tv> 0.4.0-1.mga3
+ Revision: 331952
- fix group
- patch 2: fix linking
- fix format litteral errors
- imported package liblangtag

