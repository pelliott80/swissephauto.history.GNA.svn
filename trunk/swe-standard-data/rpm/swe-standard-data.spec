#
# spec file for package swe-standard-data
#




Name:           swe-standard-data
Version:        1.77.00.0001
Release:        1
License:        GPL2+
Summary:        Standerd Data for the Swiss Ephemeris
Url:            http://swissephauto.blackpatchpanel.com/
Group:          Productivity/Scientific/Astronomy
Source0:        http://download.berlios.de/swissephauto/%{name}-%{version}.tar.bz2

BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch


%description
standard data for the Swiss Ephemeris
all of the standard data, i.e. the usual .se1 files, for the Swiss Ephemeris.
All of the .se1 files located here: 
  ftp://ftp.astro.com/pub/swisseph/ephe/*.se1
are in the package. This data can be used with the Swiss Ephemeris library,
libswe0. This package uses 36 meg. It contains 54 .se1 files.
Installed in /usr/share/libswe/users/ephe/
The Swiss Ephemeris library has been patched so that it looks to this location
by default.

%prep
%setup -q

%build
#defines make install actions
%configure 
# does nothing....Now
# Hey! Have you ever heard of pro-forma?
make 
cp COPYING copyright

%install
make DESTDIR=%{buildroot} install


%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc copyright  AUTHORS README.TXT README.Linux LICENSE.TXT
%dir %{_datadir}/libswe
%dir %{_datadir}/libswe/users
%dir %{_datadir}/libswe/users/ephe
%{_datadir}/libswe/users/ephe/*


%changelog
