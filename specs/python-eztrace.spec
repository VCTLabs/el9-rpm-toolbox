# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global srcname pyeztrace

Name:           python-%{srcname}
Version:        0.0.14
Release:        1%{?dist}
Summary:        A dependency-free, lightweight Python tracing and logging library.

License:        MIT
URL:            https://github.com/jeffersonaaron25/PyEzTrace
Source0:        %{pypi_source}

BuildArch:      noarch

BuildRequires: python%{python3_pkgversion}-devel
BuildRequires: pyproject-rpm-macros
BuildRequires: python%{python3_pkgversion}dist(tomli)
BuildRequires: python%{python3_pkgversion}dist(wheel)
BuildRequires: python%{python3_pkgversion}dist(setuptools)
BuildRequires: python%{python3_pkgversion}dist(setuptools-scm[toml])
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif

%description
A dependency-free, lightweight Python tracing and logging library with
hierarchical logging, context management, and performance metrics.

%package -n python%{python3_pkgversion}-%{srcname}
Summary:        %{summary}

%description -n python%{python3_pkgversion}-%{srcname}
A dependency-free, lightweight Python tracing and logging library with
hierarchical logging, context management, and performance metrics.

%prep
%autosetup -p1 -n %{srcname}-%{version}

# using pyproject macros
%generate_buildrequires
%pyproject_buildrequires

%build
%pyproject_wheel

%install
%pyproject_install

# Use -l to assert a %%license file is found (PEP 639).
# note the last argument is the top-level module directory name
%pyproject_save_files -l pyeztrace

%check
%pyproject_check_import
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-pyeztrace -f %{pyproject_files}
%doc README.md
%license LICENSE

%changelog
* Mon Dec 22 2025 Stephen Arnold <nerdboy@gentoo.org> - v0.0.14
- Initial package
