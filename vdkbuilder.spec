%define		_tutver	1.1
Summary:	A general purpose ide for constructing gui applications using VDK
Summary(pl.UTF-8):	IDE do konstruowania aplikacji graficznych używających VDK
Name:		vdkbuilder
Version:	2.4.0
Release:	1
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/vdkbuilder/%{name}2-%{version}.tar.gz
# Source0-md5:	91216ce6659e447862b2bdc7335074fc
Source1:	http://dl.sourceforge.net/vdkbuilder/vdktutorial-%{_tutver}.pdf.gz
# Source1-md5:	06d2e9b1dab6bec28d7ea3b6819dfb67
Source2:	%{name}.desktop
Patch0:		%{name}-ac_FLAGS.patch
URL:		http://vdkbuilder.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	vdk-devel >= 2.4.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
VDKBuilder is a Rapid Application Development tool based on VDK - "The
Visual Development Kit", a C++ framework that wraps famous GTK+ widget
set library.

%description -l pl.UTF-8
VDKBuilder jest narzędziem RAD bazującym na VDK, bibliotece wrapującej
znaną bibliotekę widgetów - GTK+.

%package devel
Summary:	Header files for vdkbuilder
Summary(pl.UTF-8):	Pliki nagłówkowe bibliotek vdkbuilder
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
vdkbuilder header files.

%description devel -l pl.UTF-8
Pliki nagłówkowe blibliotek vdkbuilder.

%prep
%setup -q -n %{name}2-%{version}
%patch0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install %{SOURCE1} .
install -D %{SOURCE2} $RPM_BUILD_ROOT%{_desktopdir}/%{name}.desktop

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO example/nls_HOWTO* example/hello vdktutorial-%{_tutver}.pdf.gz
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so*
%{_mandir}/man1/*
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/*.png
%{_datadir}/vdkb2

%files devel
%defattr(644,root,root,755)
%{_libdir}/lib*.la
%{_includedir}/vdkb2
