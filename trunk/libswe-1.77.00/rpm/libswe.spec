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

BuildRequires:  pkg-config
 
#suse version uses fdupes
%if 0%{?suse_version} || 0%{?sles_version}
BuildRequires:  fdupes
#BuildRequires:	libreoffice-converter
BuildRequires:	htmldoc

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

%package -n libswe0
Summary:        Shared library for libswe
Group:          Productivity/Scientific/Astronomy
Recommends:	swe-basic-data, swe-standard-data

%description -n libswe0
This package contains the shared library needed for libswe.

%package        devel
Summary:        Development files for libswe
Group:          Development/Libraries/C and C++
Requires:       %{name} = %{version}

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
mkdir -p %{_builddir}%{_defaultdocdir}/libswe-devel
%configure WPCONVERT=htmldoc --disable-static --docdir=%{_defaultdocdir}/libswe-devel 
make %{?jobs:-j %jobs}

%install
ls -lR %{buildroot}
mkdir -p %{buildroot}%{_defaultdocdir}/libswe-devel
mkdir -p %{buildroot}%{_defaultdocdir}/swe-basic-data
make DESTDIR=%{buildroot} install
rm $RPM_BUILD_ROOT/%_libdir/libswe*.la
cp COPYING %{buildroot}%{_defaultdocdir}/libswe-devel/copyright
rm %{buildroot}%{_defaultdocdir}/libswe-devel/COPYING
cp COPYING %{buildroot}%{_defaultdocdir}/swe-basic-data/copyright


%if 0%{?suse_version} || 0%{?sles_version}
%fdupes -s %{buildroot}%{_mandir}
%endif





%clean
rm -rf $RPM_BUILD_ROOT

%post -n libswe0 -p /sbin/ldconfig
%postun -n libswe0 -p /sbin/ldconfig
 


%files -n libswe0
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_defaultdocdir}/libswe-devel
%{_includedir}/*.h
%{_libdir}/libswe.so
%{_libdir}/pkgconfig/*.pc
%{_mandir}/man1/*.1*
%{_mandir}/man3/*.3*
%{_bindir}/*

%files -n swe-basic-data
%defattr(-,root,root,-)
%{_defaultdocdir}/swe-basic-data
%dir %{_datadir}/libswe
%dir %{_datadir}/libswe/users
%dir %{_datadir}/libswe/users/ephe
%{_datadir}/libswe/users/ephe/*


%changelog
