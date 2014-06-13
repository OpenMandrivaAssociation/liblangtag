%define major	1
%define libname	%mklibname langtag %{major}
%define devname	%mklibname langtag -d

Summary:	An interface library to access tags for identifying languages
Name:		liblangtag
Version:	0.4.0
Release:	6
Group:		System/Internationalization
License:	LGPLv3+
Url:		https://github.com/tagoh/liblangtag/
Source0:	https://github.com/downloads/tagoh/%{name}/%{name}-%{version}.tar.bz2
Patch0:		0001-Fix-build-issues-with-MSVC.patch
Patch1:		fix-format-not-a-string-literal.diff
Patch2:		fix-linking.diff

BuildRequires:	gtk-doc
BuildRequires:	libtool
BuildRequires:	pkgconfig(libxml-2.0)

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

%package -n %{libname}
Summary:	An interface library to access tags for identifying languages
Group:		System/Libraries

%description -n %{libname}
%{name} is an interface library to access tags for identifying
languages.

%package -n %{devname}
Summary:	Development files for %{name}
Group:		Development/C
Requires:	%{libname} = %{version}-%{release}

%description -n %{devname}
This package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q
%apply_patches

%build
%configure2_5x \
	--disable-static \
	--enable-shared \
	--disable-introspection

%make

%install
%makeinstall_std

%files -n %{libname}
%doc AUTHORS COPYING NEWS README
%{_libdir}/%{name}.so.%{major}*
%{_libdir}/%{name}/*.so
%{_datadir}/%{name}

%files -n %{devname}
%doc COPYING
%doc %{_datadir}/gtk-doc/html/%{name}
%{_includedir}/%{name}
%{_libdir}/%{name}.so
%{_libdir}/pkgconfig/%{name}.pc

