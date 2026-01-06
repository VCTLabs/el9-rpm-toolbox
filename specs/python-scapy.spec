Name:           scapy
Version:        2.7.0
Release:        1%{?dist}
Summary:        Interactive packet manipulation tool and network scanner

License:        GPLv2
URL:            http://www.secdev.org/projects/scapy/
Source0:        https://github.com/secdev/scapy/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz
Patch0:         scapy-2.7.0-rhel9.patch

%global         common_desc %{expand:
Scapy is a powerful interactive packet manipulation program built on top
of the Python interpreter. It can be used to forge or decode packets of
a wide number of protocols, send them over the wire, capture them, match
requests and replies, and much more.}


# By default build with python3 subpackage
%bcond_without     python3
%bcond_with        python2
%bcond_with        doc

BuildArch:      noarch

BuildRequires:  make
BuildRequires:  sed

BuildRequires:  python%{python3_pkgversion}-devel
BuildRequires:  python%{python3_pkgversion}-setuptools

Recommends:     tcpdump
# Using database of manufactures /usr/share/wireshark/manuf
Recommends:     wireshark-cli

%description %{common_desc}

%package -n python%{python3_pkgversion}-%{name}
Summary:        Interactive packet manipulation tool and network scanner

%{?python_provide:%python_provide python%{python3_pkgversion}-%{name}}
Provides:       %{name} = %{version}-%{release}

Recommends:     PyX
Recommends:     python%{python3_pkgversion}-matplotlib
Recommends:     ipython3

%description -n python%{python3_pkgversion}-%{name}
%{common_desc}


%prep
%autosetup -p 1 -n %{name}-%{version}

# Remove shebang
# https://github.com/secdev/scapy/pull/2332
SHEBANGS=$(find ./scapy -name '*.py' -print | xargs grep -l -e '^#!.*env python')
for FILE in $SHEBANGS ; do
    sed -i.orig -e 1d "${FILE}"
    touch -r "${FILE}.orig" "${FILE}"
    rm "${FILE}.orig"
done

%build
%py3_build

%install
install -dp -m0755 %{buildroot}%{_mandir}/man1
install -Dp -m0644 doc/scapy.1* %{buildroot}%{_mandir}/man1/

%py3_install
rm -f %{buildroot}%{python3_sitelib}/*egg-info/requires.txt

# Rename the executables
mv -f %{buildroot}%{_bindir}/scapy   %{buildroot}%{_bindir}/scapy3

# Link the default to the python3 version of executables
ln -s %{_bindir}/scapy3   %{buildroot}%{_bindir}/scapy

# check
# TODO: Need to fix/remove slow/failed test
# cd test/
# ./run_tests_py2 || true
# ./run_tests_py3 || true


%files -n python%{python3_pkgversion}-%{name}
%license LICENSE
%doc %{_mandir}/man1/scapy.1*
%{_bindir}/scapy
%{_bindir}/scapy3
%{python3_sitelib}/scapy/
%{python3_sitelib}/scapy-*.egg-info
%exclude %{python3_sitelib}/test


%changelog
* Tue Jan 06 2026 Stephen Arnold <nerdboy@gentoo.org> - 2.7.0
- New/upgraded package
