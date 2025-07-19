# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name py3tftp

Name:           python-%{pypi_name}
Version:        1.3.0
Release:        1%{?dist}
Summary:        Py3tftp is an asynchronous TFTP server written in Python.

License:        MIT
URL:            http://github.com/sirMackk/py3tftp
Source0:        %{pypi_source}
BuildArch:      noarch

%description
Py3tftp implements RFC 1350 (except mail mode), RFC 2347 (options),
RFC 2348 (blksize option), RFC 2349 (timeout, tsize), and RFC 7440
(windowsize) for RRQ. Additionally, it supports block number roll
over, so files of any size can be transferred over.

%package -n     python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
Py3tftp implements RFC 1350 (except mail mode), RFC 2347 (options),
RFC 2348 (blksize option), RFC 2349 (timeout, tsize), and RFC 7440
(windowsize) for RRQ. Additionally, it supports block number roll
over, so files of any size can be transferred over.

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
%doc README.md
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/
%{_bindir}/py3tftp

%changelog
* Sat Jul 19 2025 Stephen Arnold <nerdboy@gentoo.org> - 1.3.0
- Initial package
