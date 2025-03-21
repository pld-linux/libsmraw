#
# Conditional build:
%bcond_without	python	# Python (3) bindings
%bcond_without	python3	# CPython 3.x bindings
#
%if %{without python}
%undefine	with_python3
%endif
# see m4/${libname}.m4 />= for required version of particular library
%define		libbfio_ver	20201125
%define		libcdata_ver	20230108
%define		libcerror_ver	20120425
%define		libcfile_ver	20160409
%define		libclocale_ver	20120425
%define		libcnotify_ver	20120425
%define		libcpath_ver	20180716
%define		libcsplit_ver	20120701
%define		libcthreads_ver	20160404
%define		libfcache_ver	20191109
%define		libfdata_ver	20201129
%define		libfvalue_ver	20200711
%define		libhmac_ver	20200104
%define		libuna_ver	20230702
Summary:	Library to access the storage media (SM) (split) RAW format
Summary(pl.UTF-8):	Biblioteka służąca do dostępu do surowego (dzielonego) formatu nośnika danych (SM)
Name:		libsmraw
Version:	20240506
Release:	2
License:	LGPL v3+
Group:		Libraries
#Source0Download: https://github.com/libyal/libsmraw/releases
Source0:	https://github.com/libyal/libsmraw/releases/download/%{version}/%{name}-alpha-%{version}.tar.gz
# Source0-md5:	e49d54d43a5c45cbca218df5849589ca
URL:		https://github.com/libyal/libsmraw/
BuildRequires:	autoconf >= 2.71
BuildRequires:	automake >= 1.6
BuildRequires:	gettext-tools >= 0.21
BuildRequires:	libbfio-devel >= %{libbfio_ver}
BuildRequires:	libcdata-devel >= %{libcdata_ver}
BuildRequires:	libcerror-devel >= %{libcerror_ver}
BuildRequires:	libcfile-devel >= %{libcfile_ver}
BuildRequires:	libclocale-devel >= %{libclocale_ver}
BuildRequires:	libcnotify-devel >= %{libcnotify_ver}
BuildRequires:	libcpath-devel >= %{libcpath_ver}
BuildRequires:	libcsplit-devel >= %{libcsplit_ver}
BuildRequires:	libcthreads-devel >= %{libcthreads_ver}
BuildRequires:	libfcache-devel >= %{libfcache_ver}
BuildRequires:	libfdata-devel >= %{libfdata_ver}
# or libfuse >= 2.6
BuildRequires:	libfuse3-devel >= 3.0
BuildRequires:	libfvalue-devel >= %{libfvalue_ver}
BuildRequires:	libhmac-devel >= %{libhmac_ver}
BuildRequires:	libuna-devel >= %{libuna_ver}
BuildRequires:	libtool >= 2:2
BuildRequires:	openssl-devel >= 1.0
BuildRequires:	pkgconfig
%{?with_python3:BuildRequires:	python3-devel >= 1:3.7}
Requires:	libbfio >= %{libbfio_ver}
Requires:	libcdata >= %{libcdata_ver}
Requires:	libcerror >= %{libcerror_ver}
Requires:	libcfile >= %{libcfile_ver}
Requires:	libclocale >= %{libclocale_ver}
Requires:	libcnotify >= %{libcnotify_ver}
Requires:	libcpath >= %{libcpath_ver}
Requires:	libcsplit >= %{libcsplit_ver}
Requires:	libcthreads >= %{libcthreads_ver}
Requires:	libfcache >= %{libfcache_ver}
Requires:	libfdata >= %{libfdata_ver}
Requires:	libfvalue >= %{libfvalue_ver}
Requires:	libuna >= %{libuna_ver}
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
Requires:	libbfio-devel >= %{libbfio_ver}
Requires:	libcdata-devel >= %{libcdata_ver}
Requires:	libcerror-devel >= %{libcerror_ver}
Requires:	libcfile-devel >= %{libcfile_ver}
Requires:	libclocale-devel >= %{libclocale_ver}
Requires:	libcnotify-devel >= %{libcnotify_ver}
Requires:	libcpath-devel >= %{libcpath_ver}
Requires:	libcsplit-devel >= %{libcsplit_ver}
Requires:	libcthreads-devel >= %{libcthreads_ver}
Requires:	libfcache-devel >= %{libfcache_ver}
Requires:	libfdata-devel >= %{libfdata_ver}
Requires:	libfvalue-devel >= %{libfvalue_ver}
Requires:	libuna-devel >= %{libuna_ver}

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
Requires:	libfuse3 >= 3.0
Requires:	libhmac >= %{libhmac_ver}

%description tools
Tools for libsmraw library.

%description tools -l pl.UTF-8
Narzędzia do biblioteki smraw.

%package -n python3-pysmraw
Summary:	Python 3 bindings for libsmraw library
Summary(pl.UTF-8):	Wiązania Pythona 3 do biblioteki libsmraw
Group:		Libraries/Python
Requires:	%{name} = %{version}-%{release}

%description -n python3-pysmraw
Python 3 bindings for libsmraw library.

%description -n python3-pysmraw -l pl.UTF-8
Wiązania Pythona 3 do biblioteki libsmraw.

%prep
%setup -q

%build
%{__gettextize}
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	PYTHON_VERSION=3 \
	%{?with_python3:--enable-python}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# obsoleted by pkg-config
%{__rm} $RPM_BUILD_ROOT%{_libdir}/libsmraw.la

%if %{with python3}
%{__rm} $RPM_BUILD_ROOT%{py3_sitedir}/pysmraw.{la,a}
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

%if %{with python3}
%files -n python3-pysmraw
%defattr(644,root,root,755)
%attr(755,root,root) %{py3_sitedir}/pysmraw.so
%endif
