# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name hexdump

Name:           python-%{pypi_name}
Version:        3.5.3
Release:        1%{?dist}
Summary:        view/edit your binary with any text editor.

License:        LGPL-2.1-or-later
URL:            http://github.com/sarnold/hexdump
Source0:        %{url}/releases/download/%{version}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch

%description
Hexdump is both a library and command line tool, and can dump your binary
to hex and restore it back. Hexdump can run on all major platforms, eg,
Linux, Windows, MacOS, using any non-ancient Python 3 release.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(tomli)
BuildRequires:  python%{python3_pkgversion}dist(wheel)
BuildRequires:  python%{python3_pkgversion}dist(setuptools)
BuildRequires:  python%{python3_pkgversion}dist(setuptools-scm[toml])
BuildRequires:  python%{python3_pkgversion}dist(importlib-resources)
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
Hexdump is both a library and command line tool, and can dump your binary
to hex and restore it back. Hexdump can run on all major platforms, eg,
Linux, Windows, MacOS, using any non-ancient Python 3 release.

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
%pyproject_save_files -l hexdump

# Use -t to only import top-level module
%check
%pyproject_check_import
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-hexdump -f %{pyproject_files}
%doc README.rst CHANGELOG.rst
%license LICENSE REUSE.toml
%{_bindir}/hexdump

%changelog
* Wed Sep 03 2025 Stephen Arnold <nerdboy@gentoo.org> - 3.5.3
- Bump package release number for spec change
* Mon Aug 18 2025 Stephen Arnold <nerdboy@gentoo.org> - 3.5.3
- New upstream release
* Mon Jul 21 2025 Stephen Arnold <nerdboy@gentoo.org> - 3.5.2
- New package
