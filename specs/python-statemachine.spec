# Tests are disabled in RHEL 9 because really old tox
# Specify --with tests to enable them.
%bcond_with tests

%global pypi_name python_statemachine
%global short_name statemachine

Name:           %{pypi_name}
Version:        3.1.2
Release:        1%{?dist}
Summary:        Expressive statecharts and FSMs for modern Python.

License:        MIT
URL:            https://github.com/fgmacedo/python-statemachine
Source0:        %{pypi_source}

BuildArch:      noarch

%description
Welcome to python-statemachine, an intuitive and powerful state machine
library designed for a great developer experience. Define flat state
machines or full statecharts with compound states, parallel regions,
and history — all with a clean, pythonic, declarative API that works in
both sync and async Python codebases.

%package -n     python%{python3_pkgversion}-%{short_name}
Summary:        %{summary}

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}dist(tomli)
BuildRequires:  python%{python3_pkgversion}dist(hatchling)
BuildRequires:  python%{python3_pkgversion}dist(pydot)
BuildRequires:  python%{python3_pkgversion}dist(docutils)
BuildRequires:  python%{python3_pkgversion}dist(sphinx)
BuildRequires:  pyproject-rpm-macros
BuildRequires:  python%{python3_pkgversion}dist(typing-extensions)
%if %{with tests}
BuildRequires:  python%{python3_pkgversion}dist(pytest)
%endif

%{?python_provide:%python_provide python%{python3_pkgversion}-%{short_name}}

%description -n python%{python3_pkgversion}-%{short_name}
Welcome to python-statemachine, an intuitive and powerful state machine
library designed for a great developer experience. Define flat state
machines or full statecharts with compound states, parallel regions,
and history — all with a clean, pythonic, declarative API that works in
both sync and async Python codebases.

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
%pyproject_save_files -L statemachine

%check
%pyproject_check_import
%if %{with tests}
%pytest -vv test/
%endif

%files -n python%{python3_pkgversion}-statemachine -f %{pyproject_files}
%doc README.md AGENTS.md
%license LICENSE

%changelog
* Tue May 26 2026 Stephen Arnold <nerdboy@gentoo.org> - 3.1.2
- New package
