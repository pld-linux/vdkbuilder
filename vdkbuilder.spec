Summary:	A general purpose ide for constructing gui applications using VDK
Summary(pl):	IDE do konstruowania aplikacji graficznych u¿ywaj±cych VDK
Name:		vdkbuilder
Version:	2.0.1
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/vdkbuilder/%{name}-%{version}.tar.gz
URL:		http://vdkbuilder.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel >= 2.0.0
BuildRequires:	glib2-devel >= 2.0.0
BuildRequires:	libtool
BuildRequires:	vdk-devel >= 2.0.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_omf_dest_dir	%(scrollkeeper-config --omfdir)

%description
VDKBuilder is a Rapid Application Development tool based on VDK - "The
Visual Development Kit", a C++ framework that wraps famous Gtk+ widget
set library.

%description -l pl
VDKBuilder jest narzêdziem RAD bazuj±cym na VDK, bibliotece wrapuj±cej
znan± bibliotekê widgetów - Gtk+.

%prep
%setup  -q

%build
#CXXFLAGS="%{rpmcflags} -fno-rtti -fno-exceptions"
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

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS BUGS ChangeLog NEWS README TODO TUTOR* example/nls_HOWTO* example/hello
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so*
%{_libdir}/lib*.la
%{_includedir}/vdkb2
%{_mandir}/man1/*
%{_pixmapsdir}/*.png
%{_datadir}/vdkb2
