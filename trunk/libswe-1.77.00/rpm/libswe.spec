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
 
#suse version uses fdupes
%if 0%{?suse_version} || 0%{?sles_version}
BuildRequires:  fdupes
%endif


Source0:        http://download.berlios.de/swissephauto/%{name}-%{version}.tar.gz
Source1:	ftp://ftp.astro.com/pub/swisseph/swe_unix_src_1.77.00.tar.gz
Source2:	http://download.berlios.de/swissephauto/libswe_1.77.00.0001.orig-astrodocsrc.tar.gz
Patch0:		ephepath-fix
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


Author:
-------
    Dieter Koch and Alois Treindl of Astrodienst AG, Switzerland
    Paul Elliott <pelliott@blackpatchpanel.com>


%package -n libswe0
Summary:        Shared library for libswe
Group:          Productivity/Scientific/Astronomy

%description -n libswe0
This package contains the shared library needed for libswe.

Author:
-------
    Dieter Koch and Alois Treindl of Astrodienst AG, Switzerland
    Paul Elliott <pelliott@blackpatchpanel.com>


%package        devel
Summary:        Development files for libswe
Group:          Productivity/Scientific/Astronomy
Requires:       %{name} = %{version}

%description    devel
The libswe-devel package contains libraries and header files, man pages,
and documentation for developing applications that use libswe.

Author:
-------
    Dieter Koch and Alois Treindl of Astrodienst AG, Switzerland
    Paul Elliott <pelliott@blackpatchpanel.com>


%prep
%setup -q
%patch0 -p1 -z .deb
%patch1 -p1 -b .tar_header
# set correct version for .so build
%define ltversion %(echo %{version} | tr '.' ':')
sed -i 's/-rpath $(libdir)/-rpath $(libdir) -version-number %{ltversion}/' \
  lib/Makefile.in


%build
cp /usr/share/libtool/config/config.sub /usr/share/libtool/config/ltmain.sh autoconf
%configure --disable-static
# Don't use rpath!
cp /usr/bin/libtool .
sed -i 's|^hardcode_libdir_flag_spec=.*|hardcode_libdir_flag_spec=""|g' libtool
sed -i 's|^runpath_var=LD_RUN_PATH|runpath_var=DIE_RPATH_DIE|g' libtool
make %{?jobs:-j %jobs}

%install
%makeinstall
# Without this we get no debuginfo and stripping
chmod +x $RPM_BUILD_ROOT%{_libdir}/libtar.so.%{version}
rm $RPM_BUILD_ROOT%{_libdir}/*.la
rm $RPM_BUILD_ROOT%{_libdir}/*.a
%fdupes -s %{buildroot}%{_mandir}

%clean
rm -rf $RPM_BUILD_ROOT

%post -n libtar1 -p /sbin/ldconfig
%postun -n libtar1 -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYRIGHT TODO README ChangeLog*
%{_bindir}/%{name}

%files -n libtar1
%defattr(-,root,root,-)
%{_libdir}/lib*.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/libtar.h
%{_includedir}/libtar_listhash.h
%{_libdir}/lib*.so
%{_mandir}/man3/*.3*


%changelog
