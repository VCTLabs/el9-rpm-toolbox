# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name stoppy

Name:           python-%{pypi_name}
Version:        1.0.5
Release:        1%{?dist}
Summary:        A precise and lightweight stopwatch built on top of perf_counter.

License:        MIT
URL:            http://github.com/morefigs/stoppy
Source0:        %{pypi_source}
BuildArch:      noarch

%description
A precise and lightweight stopwatch built on top of perf_counter, which can
be used as a replacement for perf_counter that returns absolute time starting
from zero.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}dist(tomli)
BuildRequires:  python%{python3_pkgversion}dist(poetry-core)
BuildRequires:  pyproject-rpm-macros
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
A precise and lightweight stopwatch built on top of perf_counter, which can
be used as a replacement for perf_counter that returns absolute time starting
from zero.

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
%pyproject_save_files -L stoppy

%check
%pyproject_check_import
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-stoppy -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Thu Jul 17 2025 Stephen Arnold <nerdboy@gentoo.org> - 1.0.5
- New package
