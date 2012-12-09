Name:		xplanet
Version:	1.3.0
Release:	%mkrel 1
Summary:	OpenGL based planet renderer
Source0:	http://freefr.dl.sourceforge.net/sourceforge/xplanet/%{name}-%{version}.tar.gz
URL:		http://xplanet.sourceforge.net/
License:	GPLv2+
Group:		Toys
BuildRequires:	png-devel
BuildRequires:	jpeg-devel
BuildRequires:	tiff-devel
BuildRequires:	ungif-devel
BuildRequires:	libx11-devel
BuildRequires:	libxscrnsaver-devel
BuildRequires:	freetype2-devel
BuildRequires:	pango-devel

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

%build
# the macro break X output
%configure2_5x --with-xscreensaver --with-x
%make

%install
rm -rf %{buildroot}
%makeinstall_std


%files
%doc COPYING ChangeLog
%{_mandir}/man1/%{name}.1*
%{_bindir}/*
%{_datadir}/%{name}


%changelog

* Tue Jun 12 2012 eatdirt <eatdirt> 1.3.0-1.mga3
+ Revision: 260090
- Upgrade version to 1.3.0

* Sun Mar 04 2012 luigiwalser <luigiwalser> 1.2.2-4.mga2
+ Revision: 217657
- rebuild for netpbm

* Fri Dec 23 2011 mikala <mikala> 1.2.2-3.mga2
+ Revision: 186830
- Rebuild for new libtiff
- remove %%defattr() & %%clean section
- use %%{buildroot} macro instead of $RPM_BUILD_ROOT

* Sun Sep 18 2011 fwang <fwang> 1.2.2-2.mga2
+ Revision: 144965
- rebuild for new libpng
- new version 1.2.

* Sat Jan 22 2011 ahmad <ahmad> 1.2.1-6.mga1
+ Revision: 33307
- drop BR X11-devel
- add BR libxscrnsaver-devel libice-devel libnetpbm-devel
- imported package xplanet

