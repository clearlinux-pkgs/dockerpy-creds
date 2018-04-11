#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : dockerpy-creds
Version  : 0.2.2
Release  : 3
URL      : https://github.com/shin-/dockerpy-creds/archive/0.2.2.tar.gz
Source0  : https://github.com/shin-/dockerpy-creds/archive/0.2.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0
Requires: dockerpy-creds-python3
Requires: dockerpy-creds-python
Requires: six
BuildRequires : attrs-python
BuildRequires : coverage-python
BuildRequires : flake8-python
BuildRequires : mccabe-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : pluggy-python
BuildRequires : py-python
BuildRequires : pycodestyle-python
BuildRequires : pyflakes-python
BuildRequires : pytest-cov-python
BuildRequires : pytest-python
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : six
BuildRequires : six-python
Patch1: 0001-Use-latest-version-of-requirements.patch

%description
# docker-pycreds
Python bindings for the docker credentials store API
## Credentials store info

%package python
Summary: python components for the dockerpy-creds package.
Group: Default
Requires: dockerpy-creds-python3

%description python
python components for the dockerpy-creds package.


%package python3
Summary: python3 components for the dockerpy-creds package.
Group: Default
Requires: python3-core

%description python3
python3 components for the dockerpy-creds package.


%prep
%setup -q -n dockerpy-creds-0.2.2
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1523474573
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
