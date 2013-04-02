Name:		xplanet
Version:	1.3.0
Release:	3
Summary:	OpenGL based planet renderer
Source0:	http://freefr.dl.sourceforge.net/sourceforge/xplanet/%{name}-%{version}.tar.gz
Patch1:		xplanet-1.3.0-giflib5.patch
URL:		http://xplanet.sourceforge.net/
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
%patch1 -p0

%build
# the macro break X output
%configure2_5x --with-xscreensaver --with-x
%make

%install
%makeinstall_std

%files
%doc COPYING ChangeLog
%{_mandir}/man1/%{name}.1*
%{_bindir}/*
%{_datadir}/%{name}

