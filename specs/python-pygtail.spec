# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name pygtail

Name:           python-%{pypi_name}
Version:        0.14.0.3
Release:        1%{?dist}
Summary:        Pygtail reads log file lines that have not been read.

License:        MIT
URL:            http://github.com/VCTLabs/pygtail
Source0:        %{url}/releases/download/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Pygtail reads log file lines that have not been read. It will even handle
log files that have been rotated. Based on logcheck's logtail2.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(tomli)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml])
# this is not really "extra"
BuildRequires:  python%{python3_pkgversion}dist(jinja2)
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Pygtail reads log file lines that have not been read. It will even handle
log files that have been rotated. Based on logcheck's logtail2.

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
%pyproject_save_files -l pygtail

%check
%pyproject_check_import -e '*.export'
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-pygtail -f %{pyproject_files}
%doc README.rst
%license LICENSE
%{_bindir}/pygtail

%changelog
* Tue Aug 19 2025 Stephen Arnold <nerdboy@gentoo.org> - 0.14.0.3
- New upstream release
* Fri Jul 18 2025 Stephen Arnold <nerdboy@gentoo.org> - 0.14.0.2
- New package
