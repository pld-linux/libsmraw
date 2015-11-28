#
# Conditional build:
%bcond_without	python	# Python bindings
#
Summary:	Library to access the storage media (SM) (split) RAW format
Summary(pl.UTF-8):	Biblioteka służąca do dostępu do surowego (dzielonego) formatu nośnika danych (SM)
Name:		libsmraw
Version:	20150105
Release:	3
License:	LGPL v3+
Group:		Libraries
Source0:	https://github.com/libyal/libsmraw/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	0f40bc041ec5d22083cee46091ef6205
Patch0:		%{name}-system-libs.patch
URL:		https://github.com/libyal/libsmraw/
BuildRequires:	autoconf >= 2.59
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.18.1
BuildRequires:	libbfio-devel >= 20120426
BuildRequires:	libcdata-devel >= 20150102
BuildRequires:	libcerror-devel >= 20120425
BuildRequires:	libcfile-devel >= 20140503
BuildRequires:	libclocale-devel >= 20120425
BuildRequires:	libcnotify-devel >= 20120425
BuildRequires:	libcpath-devel >= 20120701
BuildRequires:	libcsplit-devel >= 20120701
BuildRequires:	libcstring-devel >= 20120425
BuildRequires:	libcsystem-devel >= 20141018
BuildRequires:	libcthreads-devel >= 20130509
BuildRequires:	libfcache-devel >= 20140601
BuildRequires:	libfdata-devel >= 20140915
BuildRequires:	libfuse-devel >= 2.6
BuildRequires:	libfvalue-devel >= 20130415
BuildRequires:	libhmac-devel >= 20130714
BuildRequires:	libuna-devel >= 20120425
BuildRequires:	libtool
BuildRequires:	openssl-devel >= 1.0
BuildRequires:	pkgconfig
%{?with_python:BuildRequires:	python-devel >= 1:2.5}
BuildRequires:	sed >= 4.0
Requires:	libbfio >= 20120426
Requires:	libcdata >= 20150102
Requires:	libcerror >= 20120425
Requires:	libcfile >= 20140503
Requires:	libclocale >= 20120425
Requires:	libcnotify >= 20120425
Requires:	libcpath >= 20120701
Requires:	libcsplit >= 20120701
Requires:	libcstring >= 20120425
Requires:	libcthreads >= 20130509
Requires:	libfcache >= 20140601
Requires:	libfdata >= 20140915
Requires:	libfvalue >= 20130415
Requires:	libuna >= 20120425
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
libsmraw is a library to access the storage media (SM) (split) RAW
format.

%description -l pl.UTF-8
libsmraw to biblioteka służąca do dostępu do surowego (dzielonego)
formatu nośnika danych (SM - Storage Media).

%package devel
Summary:	Header files for libsmraw library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libsmraw
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libbfio-devel >= 20120426
Requires:	libcdata-devel >= 20150102
Requires:	libcerror-devel >= 20120425
Requires:	libcfile-devel >= 20140503
Requires:	libclocale-devel >= 20120425
Requires:	libcnotify-devel >= 20120425
Requires:	libcpath-devel >= 20120701
Requires:	libcsplit-devel >= 20120701
Requires:	libcstring-devel >= 20120425
Requires:	libcthreads-devel >= 20130509
Requires:	libfcache-devel >= 20140601
Requires:	libfdata-devel >= 20140915
Requires:	libfvalue-devel >= 20130415
Requires:	libuna-devel >= 20120425

%description devel
Header files for libsmraw library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libsmraw.

%package static
Summary:	Static libsmraw library
Summary(pl.UTF-8):	Statyczna biblioteka libsmraw
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libsmraw library.

%description static -l pl.UTF-8
Statyczna biblioteka libsmraw.

%package tools
Summary:	Tools for libsmraw library
Summary(pl.UTF-8):	Narzędzia do biblioteki smraw
Group:		Applications/System
Requires:	%{name} = %{version}-%{release}
Requires:	libcsystem >= 20141018
Requires:	libfuse >= 2.6
Requires:	libhmac >= 20130714

%description tools
Tools for libsmraw library.

%description tools -l pl.UTF-8
Narzędzia do biblioteki smraw.

%package -n python-pysmraw
Summary:	Python bindings for libsmraw library
Summary(pl.UTF-8):	Wiązania Pythona do biblioteki libsmraw
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python-pysmraw
Python bindings for libsmraw library.

%description -n python-pysmraw -l pl.UTF-8
Wiązania Pythona do biblioteki libsmraw.

%prep
%setup -q
%patch0 -p1

%build
%{__gettextize}
%{__sed} -i -e 's/ po\/Makefile.in//' configure.ac
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	%{?with_python:--enable-python}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsmraw.la

%if %{with python}
%{__rm} $RPM_BUILD_ROOT%{py_sitedir}/pysmraw.{la,a}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README
%attr(755,root,root) %{_libdir}/libsmraw.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsmraw.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libsmraw.so
%{_includedir}/libsmraw
%{_includedir}/libsmraw.h
%{_pkgconfigdir}/libsmraw.pc
%{_mandir}/man3/libsmraw.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libsmraw.a

%files tools
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/smrawmount
%attr(755,root,root) %{_bindir}/smrawverify
%{_mandir}/man1/smrawmount.1*

%if %{with python}
%files -n python-pysmraw
%defattr(644,root,root,755)
%attr(755,root,root) %{py_sitedir}/pysmraw.so
%endif
