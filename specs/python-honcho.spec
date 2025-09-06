# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name honcho

Name:           python-%{pypi_name}
Version:        2.0.0.2
Release:        1%{?dist}
Summary:        A Python clone of Foreman, a tool for managing Procfile-based applications.

License:        MIT
URL:            http://github.com/VCTLabs/honcho
Source0:        %{url}/releases/download/v%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
For more detail and an explanation of the circumstances in which Honcho might
be useful, consult https://honcho.readthedocs.io/

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
For more detail and an explanation of the circumstances in which Honcho might
be useful, consult https://honcho.readthedocs.io/

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
%pyproject_save_files -l honcho

%check
%pyproject_check_import -e '*.export'
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-honcho -f %{pyproject_files}
%doc README.rst CHANGELOG.rst AUTHORS.rst
%license LICENSE
%{_bindir}/honcho

%changelog
* Mon Jul 14 2025 Stephen Arnold <nerdboy@gentoo.org> - 2.0.0.1
- New package
