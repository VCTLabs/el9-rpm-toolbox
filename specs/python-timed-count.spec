# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name timed_count

Name:           python-%{pypi_name}
Version:        2.0.0
Release:        1%{?dist}
Summary:        timed-count provides an iterator with a specified delay period.

License:        MIT
URL:            http://github.com/morefigs/timed-count
Source0:        %{pypi_source}
BuildArch:      noarch

%description
timed-count provides an iterator that delays each iteration by a specified
time period. It can be used to repeatedly execute code at a precise frequency.

%package -n     python%{python3_pkgversion}-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}dist(tomli)
BuildRequires:  python%{python3_pkgversion}dist(poetry-core)
BuildRequires:  pyproject-rpm-macros
# this is not really "extra"
BuildRequires:  python%{python3_pkgversion}dist(stoppy)
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{pypi_name}}

%description -n python%{python3_pkgversion}-%{pypi_name}
timed-count provides an iterator that delays each iteration by a specified
time period. It can be used to repeatedly execute code at a precise frequency.

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
%pyproject_save_files -L timed_count

%check
%pyproject_check_import
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-timed_count -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Thu Jul 17 2025 Stephen Arnold <nerdboy@gentoo.org> - 2.0.0
- New package
