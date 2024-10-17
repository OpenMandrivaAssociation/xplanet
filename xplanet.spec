Name:		xplanet
Version:	1.3.1
Release:	2
Summary:	OpenGL based planet renderer
Source0:	http://freefr.dl.sourceforge.net/sourceforge/xplanet/%{name}-%{version}.tar.gz
#fix new api calls to libgif5
Patch0:         xplanet-1.3.1-giflib5.patch
#Fix compilation with GCC 6
Patch1:		xplanet-1.3.1-gcc6.patch
URL:		https://xplanet.sourceforge.net/
License:	GPLv2+
Group:		Toys
BuildRequires:	jpeg-devel
BuildRequires:	tiff-devel
BuildRequires:	ungif-devel
BuildRequires:	pkgconfig(freetype2)
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(pango)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xscrnsaver)

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
%autopatch -p1

%build
export CC=gcc
export CXX=g++
autoreconf -vfi

%configure2_5x --with-xscreensaver --with-x
%make_build

%install
%make_install


%files
%doc COPYING ChangeLog
%{_mandir}/man1/%{name}.1*
%{_bindir}/*
%{_datadir}/%{name}

