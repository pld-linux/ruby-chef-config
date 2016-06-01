#
# Conditional build:
%bcond_without	tests		# build without tests

%define	pkgname	chef-config
Summary:	Chef's default configuration and config loading
Name:		ruby-%{pkgname}
Version:	12.10.24
Release:	0.1
License:	Apache v2.0
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{pkgname}-%{version}.gem
# Source0-md5:	c0515424c9122e4e0c561d6a4b267123
URL:		https://github.com/chef/chef
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
%if %{with tests}
BuildRequires:	ruby-rake < 11
BuildRequires:	ruby-rake >= 10.0
BuildRequires:	ruby-rspec-core < 4
BuildRequires:	ruby-rspec-core >= 3.2
BuildRequires:	ruby-rspec-expectations < 4
BuildRequires:	ruby-rspec-expectations >= 3.2
BuildRequires:	ruby-rspec-mocks < 4
BuildRequires:	ruby-rspec-mocks >= 3.2
%endif
Requires:	ruby-fuzzyurl < 0.9
Requires:	ruby-fuzzyurl >= 0.8.0
Requires:	ruby-mixlib-config < 3
Requires:	ruby-mixlib-config >= 2.0
Requires:	ruby-mixlib-shellout < 3
Requires:	ruby-mixlib-shellout >= 2.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Chef's default configuration and config loading.


%prep
%setup -q -n %{pkgname}-%{version}

%build
# write .gemspec
%__gem_helper spec


%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
cp -p %{pkgname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_vendorlibdir}/%{pkgname}.rb
%{ruby_vendorlibdir}/%{pkgname}
%{ruby_specdir}/%{pkgname}-%{version}.gemspec
