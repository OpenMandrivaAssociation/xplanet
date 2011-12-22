Name:		xplanet
Version:	1.2.2
Release:	%mkrel 3
Summary:	OpenGL based planet renderer
Source0:	http://freefr.dl.sourceforge.net/sourceforge/xplanet/%{name}-%{version}.tar.gz
URL:		http://xplanet.sourceforge.net/
License:	GPLv2+
Group:		Toys
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	libx11-devel
BuildRequires:	libxscrnsaver-devel
BuildRequires:	freetype2-devel
BuildRequires:	ungif-devel
BuildRequires:	pango-devel
BuildRequires:	jpeg-devel
BuildRequires:	png-devel
BuildRequires:	tiff-devel

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
%configure2_5x --with-xscreensaver --with-x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING ChangeLog INSTALL
%{_mandir}/man1/%{name}.1.*
%{_bindir}/*
%{_datadir}/*
