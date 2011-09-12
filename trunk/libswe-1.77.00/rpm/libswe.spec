#
# spec file for package libswe

# norootforbuild

Name:           libswe
Summary:        Swiss Ephemeris Library
Version:        1.77.00.0001
Release:        1
License:        GPL2+
Group:          Productivity/Scientific/Astronomy
Url:            http://swissephauto.blackpatchpanel.com/

BuildRequires:  libtool 

%define sonum 0

%define do_docs --enable-docs
 
#suse version uses fdupes
%if 0%{?suse_version} || 0%{?sles_version}
BuildRequires:  fdupes
BuildRequires:  pkg-config


BuildRequires:	libreoffice-converter
BuildRequires:  libreoffice-ure, libreoffice-writer,  libreoffice-base
BuildRequires:  procps
%define wpconvert loconvert

#BuildRequires:	htmldoc

%endif

%if %{defined fedora}

#BuildRequires:	libreoffice-converter
#BuildRequires:  libreoffice-ure, libreoffice-writer,   libreoffice-base
#BuildRequires:  procps
%define wpconvert loconvert


BuildRequires:  pkgconfig

#loconvert does not work under fedora
#neither does unoconv
#suppress docs untill something fixed.

%define do_docs --disable-docs


%endif

Source0:        http://download.berlios.de/swissephauto/%{name}-%{version}.tar.bz2
Source1:	ftp://ftp.astro.com/pub/swisseph/swe_unix_src_1.77.00.tar.gz
Source2:	http://download.berlios.de/swissephauto/swe_unix_docsrc_1.77.00.tar.bz2

#fix a location of data applies to distros
#upstream does not need.
Patch0:		ephepath-fix
#fix a simple spelling error
#upstream has been notified.
Patch1:		swetest.spelling.calender.patch

BuildRoot:      %{_tmppath}/%{name}-%{version}-build



%description
libswe is a C library for the Swiss Ephemeris

The Swiss Ephemeris is based upon the latest planetary and lunar
ephemeris, DE405/406, developed by NASA's Jet Propulsion
Laboratory. The original integration, DE405, covered the years 3000 BC
to 3000 AD and required 550 Mb of disk space. DE406 is a compressed
version of DE405 which requires 200 MB while maintaining a precision
of better than 1 m for the moon and 25 m for the planets.

%package -n %{name}%{sonum}
Summary:        Shared library for libswe
Group:          Productivity/Scientific/Astronomy
%if 0%?suse_version >= 1010
Recommends:	swe-basic-data, swe-standard-data
%endif

%description -n %{name}%{sonum}
This package contains the shared library needed for libswe.

%package        devel
Summary:        Development files for libswe
Group:          Development/Libraries/C and C++
Requires:       %{name}%{sonum} = %{version}

%description    devel
The libswe-devel package contains libraries and header files, man pages,
and documentation for developing applications that use libswe.

%package -n swe-basic-data
BuildArch: noarch
Summary:	Basic data required to use libswe
Group:          Productivity/Scientific/Astronomy
%description    -n swe-basic-data
basic data files for the libswe package
This package includes basic data files needed by libswe, the Swiss Ephemeris.
The basic data consists of these files:
/usr/share/libswe/users/ephe/sedeltat.txt.inactive
/usr/share/libswe/users/ephe/sefstars.txt
/usr/share/libswe/users/ephe/seleapsec.txt
/usr/share/libswe/users/ephe/seorbel.txt
/usr/share/libswe/users/ephe/fixstars.cat
The Swiss Ephemeris library can be used without installed data,
if the user provides that data in her own private directory
and points to it with SE_EPHE_PATH.



%prep
%setup -q -T -D -a 1 -c -n %{name}-%{version}/astrodienst
%setup -q -T -D -a 2 -c -n %{name}-%{version}/astrodocsrc
%setup -q -D -T -b 0

%patch0 -p1
%patch1 -p1







%build
cp COPYING copyright
mkdir -p %{_builddir}%{_defaultdocdir}/libswe-devel
%configure WPCONVERT=$(wpconvert) --disable-static \
--docdir=%{_defaultdocdir}/libswe-devel \
%{do_docs}
make 

%install
mkdir -p %{buildroot}%{_defaultdocdir}/libswe-devel
mkdir -p %{buildroot}%{_defaultdocdir}/swe-basic-data
make DESTDIR=%{buildroot} install
rm $RPM_BUILD_ROOT/%_libdir/libswe*.la
rm -r %{buildroot}%{_defaultdocdir}/libswe-devel



%if 0%{?suse_version} || 0%{?sles_version}
%fdupes -s %{buildroot}%{_mandir}
%endif





%clean
rm -rf $RPM_BUILD_ROOT

%post -n %{name}%{sonum} -p /sbin/ldconfig
%postun -n %{name}%{sonum} -p /sbin/ldconfig
 


%files -n %{name}%{sonum}
%defattr(-,root,root,-)
%doc copyright
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%doc README 
%doc NEWS 
%doc AUTHORS 
%doc copyright 
%doc astrodienst/src/swemini.c 
%doc astrodienst/src/swetest.c 
%doc astrodienst/doc/sweph.gif 
%doc astrodienst/doc/swephin.gif 
%if 0%{?suse_version} || 0%{?sles_version}
%doc doc/swephprg.html 
%doc doc/swephprg.pdf 
%doc doc/swisseph.html 
%doc doc/swisseph.pdf
%endif
%{_includedir}/*.h
%{_libdir}/libswe.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_bindir}/*


%files -n swe-basic-data
%defattr(-,root,root,-)
%doc copyright README NEWS AUTHORS
%dir %{_datadir}/libswe
%dir %{_datadir}/libswe/users
%dir %{_datadir}/libswe/users/ephe
%{_datadir}/libswe/users/ephe/*


%changelog
