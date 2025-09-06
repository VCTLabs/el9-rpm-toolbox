# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name diskcache

Name:           python-%{pypi_name}
Version:        5.6.3
Release:        1%{?dist}
Summary:        Disk and file backed persistent cache

License:        ASL 2.0
URL:            http://www.grantjenks.com/docs/diskcache/
Source0:        %{pypi_source}
BuildArch:      noarch

%description
DiskCache is an Apache 2 licensed disk and file backed cache library,
written in pure-Python, and compatible with Django. The cloud-based
computing of 2019 puts a premium on memory. Gigabytes of empty space
is left on disks asprocesses vie for memory. Among these processes is
Memcached (and sometimes Redis) which is used as a cache. Wouldn't it
be nice to leverage.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools
BuildRequires:  python%{python3_pkgversion}-wheel
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
DiskCache is an Apache 2 licensed disk and file backed cache library,
written in pure-Python, and compatible with Django. The cloud-based
computing of 2019 puts a premium on memory. Gigabytes of empty space
is left on disks asprocesses vie for memory. Among these processes is
Memcached (and sometimes Redis) which is used as a cache. Wouldn't it
be nice to leverage.

%prep
%autosetup -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%check
%if %{with tests}
%{__python3} setup.py test
%endif

%files -n python3-%{pypi_name}
%license LICENSE
%doc README.rst
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/

%changelog
* Fri Sep 05 2025 Stephen Arnold <nerdboy@gentoo.org> - 5.6.3-1
- rebuild for testing

* Thu Jul 24 2025 Stephen Arnold <nerdboy@gentoo.org> - 5.6.3
- big version bump

* Sun Jan 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.0-2
- Address issues (rhbz#1795068)

* Sun Jan 26 2020 Fabian Affolter <mail@fabian-affolter.ch> - 4.1.0-1
- Initial package
