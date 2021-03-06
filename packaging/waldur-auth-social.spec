Name: waldur-auth-social
Summary: Waldur plugin for social authentication.
Group: Development/Libraries
Version: 0.7.9
Release: 1.el7
License: MIT
Url: http://waldur.com
Source0: %{name}-%{version}.tar.gz

Requires: waldur-core >= 0.151.0

BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires: python-setuptools

Obsoletes: nodeconductor-auth-social

%description
Waldur plugin for social authentication.

%prep
%setup -q -n %{name}-%{version}

%build
%{__python} setup.py build

%install
rm -rf %{buildroot}
%{__python} setup.py install -O1 --root=%{buildroot}

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{python_sitelib}/*

%changelog
* Mon Feb 26 2018 Jenkins <jenkins@opennodecloud.com> - 0.7.9-1.el7
- New upstream release

* Sat Feb 3 2018 Jenkins <jenkins@opennodecloud.com> - 0.7.8-1.el7
- New upstream release

* Sat Jan 13 2018 Jenkins <jenkins@opennodecloud.com> - 0.7.7-1.el7
- New upstream release

* Fri Dec 1 2017 Jenkins <jenkins@opennodecloud.com> - 0.7.6-1.el7
- New upstream release

* Mon Nov 27 2017 Jenkins <jenkins@opennodecloud.com> - 0.7.5-1.el7
- New upstream release

* Mon Nov 6 2017 Jenkins <jenkins@opennodecloud.com> - 0.7.4-1.el7
- New upstream release

* Sat Sep 16 2017 Jenkins <jenkins@opennodecloud.com> - 0.7.3-1.el7
- New upstream release

* Mon Jul 3 2017 Jenkins <jenkins@opennodecloud.com> - 0.7.2-1.el7
- New upstream release
