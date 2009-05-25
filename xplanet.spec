%define	name	xplanet 
%define version 1.2.1
%define release %mkrel 1

Summary:	OpenGL based planet renderer
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://freefr.dl.sourceforge.net/sourceforge/xplanet/%{name}-%{version}.tar.gz
Patch0:		xplanet-1.2.1-fix-gcc44.patch
URL:		http://xplanet.sourceforge.net/
License:	GPLv2+
Group:		Toys
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	png-devel pango-devel jpeg-devel tiff-devel X11-devel  

%description
Xplanet is similar to Xearth, where an image of the earth is rendered into
an X window. Azimuthal, Mercator, Mollweide, orthographic, or rectangular
projections can be displayed as well as a window with a globe the user can
rotate interactively. The other planets and some satellites may also be
displayed. The latest version, as well as maps for other planets can be
found at http://xplanet.sourceforge.net. Xplanet can support separate
night and day maps, as well as a separate cloud map.

%prep
%setup -q
%patch0 -p0

%build
# the macro break X output
./configure --with-xscreensaver --with-x --prefix=%_prefix
%make

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall

#mkdir -p $RPM_BUILD_ROOT/%_prefix/man/man1
#mv $RPM_BUILD_ROOT/%_prefix/man/*.1 $RPM_BUILD_ROOT/%_prefix/man/man1/
#bzip2 $RPM_BUILD_ROOT/%_mandir/man1/*

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog INSTALL
%{_mandir}/man1/%{name}.1.*
%{_bindir}/*
%{_datadir}/*
