Summary:	A general purpose ide for constructing gui applications using VDK
Summary(pl):	IDE do konstruowania aplikacji graficznych u�ywaj�cych VDK
Name:		vdkbuilder
Version:	2.0.1
Release:	2
License:	GPL
Group:		Development/Tools
Source0:	http://dl.sourceforge.net/vdkbuilder/%{name}-%{version}.tar.gz
# Source0-md5:	6a004c7a8ed51a30722383eb50ee69f8
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
Visual Development Kit", a C++ framework that wraps famous GTK+ widget
set library.

%description -l pl
VDKBuilder jest narz�dziem RAD bazuj�cym na VDK, bibliotece wrapuj�cej
znan� bibliotek� widget�w - GTK+.

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
