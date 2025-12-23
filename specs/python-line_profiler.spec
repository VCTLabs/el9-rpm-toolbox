%global pypi_name line_profiler

Name:           python-%{pypi_name}
Version:        5.0.0
Release:        1%{?dist}
Summary:        Line-by-line profiling for Python.

License:        BSD-3-Clause
URL:            http://github.com/pyutils/line_profiler
Source0:        %{pypi_source}
BuildArch:      noarch

%?python_enable_dependency_generator

%description
line_profiler is a module for doing line-by-line profiling of functions.
kernprof is a convenient script for running either line_profiler or the
Python standard library's cProfile or profile modules, depending on what
is available.

%package -n python3-%{pypi_name}
Summary:        Line-by-line profiling for Python.
BuildRequires:  python3-devel
BuildRequires:  python3-libs
BuildRequires:  python3-setuptools
BuildRequires:  python3-wheel
BuildRequires:  python3-tomli
%{?python_provide:%python_provide python3-%{pypi_name}}

%description -n python3-%{pypi_name}
line_profiler is a module for doing line-by-line profiling of functions.
kernprof is a convenient script for running either line_profiler or the
Python standard library's cProfile or profile modules, depending on what
is available.

%prep
%autosetup -p1 -n %{pypi_name}-%{version}
rm -rf %{pypi_name}.egg-info

%build
%py3_build

%install
%py3_install

%files -n python3-%{pypi_name}
%doc README.rst CHANGELOG.rst
%license LICENSE.txt
%{python3_sitelib}/%{pypi_name}/
%{python3_sitelib}/%{pypi_name}-%{version}-py*.egg-info/
%{python3_sitelib}/__pycache__
%{python3_sitelib}/*.py
%{_bindir}/kernprof

%changelog
* Tue Dec 23 2025 Stephen Arnold <nerdboy@gentoo.org> - 5.0.0
- New package
