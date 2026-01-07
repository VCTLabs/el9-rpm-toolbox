# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name pyserv

Name:           python-%{pypi_name}
Version:        1.9.1
Release:        1%{?dist}
Summary:        Threaded wsgi, http, tftp server classes, entry points and daemon scripts.

License:        MIT
URL:            http://github.com/sarnold/pyserv
Source0:        %{url}/releases/download/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Pyserv is a collection of threaded Python server bits, including custom
HTTP server and WSGI classes, along with corresponding console entry
points and some daemon scripts. The latest addition includes a new
async daemon script based on the py3tftp package.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(tomli)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml])
# these are not really "extra"
BuildRequires:  python%{python3_pkgversion}dist(py3tftp)
BuildRequires:  python%{python3_pkgversion}dist(daemonizer)
BuildRequires:  python%{python3_pkgversion}dist(logwatcher)
BuildRequires:  python%{python3_pkgversion}dist(tftpy)
BuildRequires:  python%{python3_pkgversion}dist(picotui)
BuildRequires:  python%{python3_pkgversion}dist(platformdirs)
BuildRequires:  python%{python3_pkgversion}-scapy
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Pyserv is a collection of threaded Python server bits, including custom
HTTP server and WSGI classes, along with corresponding console entry
points and some daemon scripts. The latest addition includes a new
async daemon script based on the py3tftp package.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}

# using pyproject macros
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Use -l to assert a %%license file is found (PEP 639).
# note the last argument is the top-level module directory name
%pyproject_save_files -l pyserv

%check
%pyproject_check_import -e '*.export'
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-pyserv -f %{pyproject_files}
%doc README.rst CHANGELOG.rst
%license LICENSE REUSE.toml
%{_bindir}/*

%changelog
* Sat Nov 22 2025 Stephen Arnold <nerdboy@gentoo.org> - 1.9.0
- Migrate to logwatcher
* Sat Nov 22 2025 Stephen Arnold <nerdboy@gentoo.org> - 1.8.11
- Transitional deps release
* Tue Aug 19 2025 Stephen Arnold <nerdboy@gentoo.org> - 1.8.7
- New upstream release
* Fri Aug 15 2025 Stephen Arnold <nerdboy@gentoo.org> - 1.8.6
- New upstream release
* Sat Aug 09 2025 Stephen Arnold <nerdboy@gentoo.org> - 1.8.5
- New upstream release
* Mon Jul 21 2025 Stephen Arnold <nerdboy@gentoo.org> - 1.8.4
- New package
