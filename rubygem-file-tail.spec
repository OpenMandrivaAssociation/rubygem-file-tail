# Generated from file-tail-1.0.5.gem by gem2rpm5 -*- rpm-spec -*-          
%define	rbname	file-tail

Summary:	File::Tail for Ruby
Name:		rubygem-%{rbname}

Version:	1.0.5
Release:	1
Group:		Development/Ruby
License:	GPLv2+ or Ruby
URL:		http://flori.github.com/file-tail
Source0:	http://rubygems.org/gems/%{rbname}-%{version}.gem
BuildRequires:	rubygems 
BuildArch:	noarch

%description
Library to tail files in Ruby

%package	doc
Summary:	Documentation for %{name}
Group:		Books/Computer books
Requires:	%{name} = %{EVRD}

%description	doc
Documents, RDoc & RI documentation for %{name}.

%prep
%setup -q

%build
%gem_build -f '(examples|tests)/'

%install
%gem_install

%files
%{_bindir}/rtail
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/bin
%{ruby_gemdir}/gems/%{rbname}-%{version}/bin/rtail
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/file
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/file/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/lib/file/tail
%{ruby_gemdir}/gems/%{rbname}-%{version}/lib/file/tail/*.rb
%{ruby_gemdir}/specifications/%{rbname}-%{version}.gemspec

%files doc
%{ruby_gemdir}/gems/%{rbname}-%{version}/README
%{ruby_gemdir}/doc/%{rbname}-%{version}
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/tests
%{ruby_gemdir}/gems/%{rbname}-%{version}/tests/*.rb
%dir %{ruby_gemdir}/gems/%{rbname}-%{version}/examples
%{ruby_gemdir}/gems/%{rbname}-%{version}/examples/*.rb

